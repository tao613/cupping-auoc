from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from database import get_db
from models import Sample, User
from schemas import SampleCreate, SampleUpdate, Sample as SampleSchema, SampleListResponse
from auth import get_current_user
import math
from datetime import datetime

router = APIRouter(prefix="/samples", tags=["samples"])

# 获取样品列表
@router.get("/", response_model=SampleListResponse)
async def get_samples(
    skip: int = Query(0, ge=0, description="跳过的记录数"),
    limit: int = Query(10, ge=1, le=100, description="每页记录数"),
    search: Optional[str] = Query(None, description="搜索关键词"),
    country: Optional[str] = Query(None, description="按国家筛选"),
    sample_type: Optional[str] = Query(None, description="按样品类型筛选"),
    is_active: bool = Query(True, description="是否只显示活跃样品"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """获取样品列表，支持分页、搜索和筛选"""
    
    # 构建查询
    query = db.query(Sample).filter(Sample.is_active == is_active)
    
    # 搜索功能
    if search:
        search_term = f"%{search}%"
        query = query.filter(
            Sample.name.ilike(search_term) |
            Sample.code.ilike(search_term) |
            Sample.description.ilike(search_term) |
            Sample.variety.ilike(search_term) |
            Sample.supplier.ilike(search_term)
        )
    
    # 筛选功能
    if country:
        query = query.filter(Sample.country.ilike(f"%{country}%"))
    
    if sample_type:
        query = query.filter(Sample.sample_type == sample_type)
    
    # 获取总数
    total = query.count()
    
    # 分页查询
    samples = query.order_by(Sample.created_at.desc()).offset(skip).limit(limit).all()
    
    # 计算分页信息
    total_pages = math.ceil(total / limit) if limit > 0 else 1
    current_page = (skip // limit) + 1 if limit > 0 else 1
    
    return {
        "data": samples,
        "pagination": {
            "total": total,
            "page": current_page,
            "limit": limit,
            "total_pages": total_pages,
            "has_next": current_page < total_pages,
            "has_prev": current_page > 1
        }
    }

# 获取单个样品
@router.get("/{sample_id}", response_model=SampleSchema)
async def get_sample(
    sample_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """获取单个样品详情"""
    
    sample = db.query(Sample).filter(
        Sample.id == sample_id,
        Sample.is_active == True
    ).first()
    
    if not sample:
        raise HTTPException(status_code=404, detail="Sample not found")
    
    return sample

# 创建样品
@router.post("/", response_model=SampleSchema)
async def create_sample(
    sample_data: SampleCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """创建新样品"""
    
    # 检查样品编号是否已存在
    existing_sample = db.query(Sample).filter(Sample.code == sample_data.code).first()
    if existing_sample:
        raise HTTPException(status_code=400, detail="Sample code already exists")
    
    # 创建样品
    sample = Sample(**sample_data.dict())
    db.add(sample)
    db.commit()
    db.refresh(sample)
    
    return sample

# 更新样品
@router.put("/{sample_id}", response_model=SampleSchema)
async def update_sample(
    sample_id: int,
    sample_data: SampleUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """更新样品信息"""
    
    sample = db.query(Sample).filter(
        Sample.id == sample_id,
        Sample.is_active == True
    ).first()
    
    if not sample:
        raise HTTPException(status_code=404, detail="Sample not found")
    
    # 更新字段
    update_data = sample_data.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(sample, field, value)
    
    sample.updated_at = datetime.utcnow()
    
    db.commit()
    db.refresh(sample)
    
    return sample

# 删除样品（软删除）
@router.delete("/{sample_id}")
async def delete_sample(
    sample_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """删除样品（软删除）"""
    
    sample = db.query(Sample).filter(
        Sample.id == sample_id,
        Sample.is_active == True
    ).first()
    
    if not sample:
        raise HTTPException(status_code=404, detail="Sample not found")
    
    # 软删除
    sample.is_active = False
    sample.updated_at = datetime.utcnow()
    
    db.commit()
    
    return {"message": "Sample deleted successfully"}

# 恢复样品
@router.patch("/{sample_id}/restore")
async def restore_sample(
    sample_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """恢复已删除的样品"""
    
    sample = db.query(Sample).filter(Sample.id == sample_id).first()
    
    if not sample:
        raise HTTPException(status_code=404, detail="Sample not found")
    
    sample.is_active = True
    sample.updated_at = datetime.utcnow()
    
    db.commit()
    db.refresh(sample)
    
    return sample

# 获取样品统计信息
@router.get("/stats/overview")
async def get_samples_stats(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """获取样品统计概览"""
    
    total_samples = db.query(Sample).filter(Sample.is_active == True).count()
    
    # 按类型统计
    type_stats = {}
    for sample_type in ['arabica', 'robusta', 'blend']:
        count = db.query(Sample).filter(
            Sample.sample_type == sample_type,
            Sample.is_active == True
        ).count()
        type_stats[sample_type] = count
    
    # 按国家统计（前5名）
    country_stats = db.query(Sample.country, db.func.count(Sample.id).label('count'))\
        .filter(Sample.is_active == True)\
        .group_by(Sample.country)\
        .order_by(db.text('count DESC'))\
        .limit(5)\
        .all()
    
    return {
        "total_samples": total_samples,
        "by_type": type_stats,
        "by_country": [{"country": country, "count": count} for country, count in country_stats]
    } 