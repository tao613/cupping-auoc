from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime, Text, Enum
from sqlalchemy.orm import relationship
from database import Base
import datetime
import enum

# 枚举类型定义
class UserRole(str, enum.Enum):
    ADMIN = "admin"
    CUPPER = "cupper"
    VIEWER = "viewer"

class SampleType(str, enum.Enum):
    ARABICA = "arabica"
    ROBUSTA = "robusta"
    BLEND = "blend"

class ProcessingMethod(str, enum.Enum):
    WASHED = "washed"
    NATURAL = "natural"
    HONEY = "honey"
    SEMI_WASHED = "semi_washed"

class RoastLevel(str, enum.Enum):
    LIGHT = "light"
    MEDIUM_LIGHT = "medium_light"
    MEDIUM = "medium"
    MEDIUM_DARK = "medium_dark"
    DARK = "dark"

class CuppingSessionStatus(str, enum.Enum):
    PLANNED = "planned"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

# 用户模型（品鉴师）
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    name = Column(String, nullable=True)
    hashed_password = Column(String)
    role = Column(Enum(UserRole), default=UserRole.CUPPER)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    
    # 联系信息
    phone = Column(String, nullable=True)  # 电话号码
    
    # 地址信息
    country = Column(String, nullable=True)  # 国家
    city = Column(String, nullable=True)  # 城市
    address = Column(String, nullable=True)  # 详细地址
    zip_code = Column(String, nullable=True)  # 邮政编码
    
    # 个人资料
    avatar = Column(String, nullable=True)  # 头像URL
    
    # 品鉴师相关信息
    certification_level = Column(String, nullable=True)  # Q Grader, SCA等认证
    experience_years = Column(Integer, nullable=True)
    bio = Column(Text, nullable=True)
    
    # 关系
    cupping_scores = relationship("CuppingScore", back_populates="cupper")
    cupping_sessions = relationship("CuppingSession", back_populates="head_cupper")

# 样品模型
class Sample(Base):
    __tablename__ = "samples"

    id = Column(Integer, primary_key=True, index=True)
    
    # 基础信息
    name = Column(String, index=True, nullable=False)
    code = Column(String, unique=True, index=True, nullable=False)  # 样品编号
    description = Column(Text, nullable=True)
    
    # 产地信息
    country = Column(String, nullable=False)
    region = Column(String, nullable=True)
    farm = Column(String, nullable=True)
    altitude = Column(Integer, nullable=True)  # 海拔米数
    
    # 咖啡品种信息
    variety = Column(String, nullable=True)  # 品种
    sample_type = Column(Enum(SampleType), nullable=False)
    processing_method = Column(Enum(ProcessingMethod), nullable=True)
    
    # 烘焙信息
    roast_date = Column(DateTime, nullable=True)
    roast_level = Column(Enum(RoastLevel), nullable=True)
    roaster = Column(String, nullable=True)
    
    # 样品状态
    harvest_year = Column(Integer, nullable=True)
    received_date = Column(DateTime, default=datetime.datetime.utcnow)
    expiry_date = Column(DateTime, nullable=True)
    
    # 质量信息
    moisture_content = Column(Float, nullable=True)  # 含水率
    density = Column(Float, nullable=True)  # 密度
    screen_size = Column(String, nullable=True)  # 筛网大小
    
    # 供应商信息
    supplier = Column(String, nullable=True)
    lot_number = Column(String, nullable=True)
    
    # 系统字段
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    is_active = Column(Boolean, default=True)
    
    # 关系
    cupping_scores = relationship("CuppingScore", back_populates="sample")
    session_samples = relationship("CuppingSessionSample", back_populates="sample")

# 品鉴会话模型
class CuppingSession(Base):
    __tablename__ = "cupping_sessions"

    id = Column(Integer, primary_key=True, index=True)
    
    # 基础信息
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    session_date = Column(DateTime, nullable=False)
    
    # 会话状态
    status = Column(Enum(CuppingSessionStatus), default=CuppingSessionStatus.PLANNED)
    
    # 负责人
    head_cupper_id = Column(Integer, ForeignKey("users.id"))
    
    # 品鉴参数
    water_temperature = Column(Float, nullable=True)
    grind_size = Column(String, nullable=True)
    coffee_to_water_ratio = Column(String, nullable=True)
    
    # 系统字段
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    
    # 关系
    head_cupper = relationship("User", back_populates="cupping_sessions")
    session_samples = relationship("CuppingSessionSample", back_populates="session")
    cupping_scores = relationship("CuppingScore", back_populates="session")

# 品鉴会话样品关联表
class CuppingSessionSample(Base):
    __tablename__ = "cupping_session_samples"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("cupping_sessions.id"))
    sample_id = Column(Integer, ForeignKey("samples.id"))
    
    # 品鉴顺序
    position = Column(Integer, nullable=True)
    
    # 样品准备信息
    preparation_notes = Column(Text, nullable=True)
    
    # 关系
    session = relationship("CuppingSession", back_populates="session_samples")
    sample = relationship("Sample", back_populates="session_samples")

# 品鉴评分模型
class CuppingScore(Base):
    __tablename__ = "cupping_scores"

    id = Column(Integer, primary_key=True, index=True)
    
    # 外键关系
    session_id = Column(Integer, ForeignKey("cupping_sessions.id"))
    sample_id = Column(Integer, ForeignKey("samples.id"))
    cupper_id = Column(Integer, ForeignKey("users.id"))
    
    # SCA标准品鉴评分项目
    fragrance_aroma = Column(Float, nullable=True)  # 干香/湿香
    flavor = Column(Float, nullable=True)  # 风味
    aftertaste = Column(Float, nullable=True)  # 余韵
    acidity = Column(Float, nullable=True)  # 酸质
    body = Column(Float, nullable=True)  # 醇厚度
    balance = Column(Float, nullable=True)  # 平衡感
    uniformity = Column(Float, nullable=True)  # 一致性
    clean_cup = Column(Float, nullable=True)  # 干净度
    sweetness = Column(Float, nullable=True)  # 甜感
    overall = Column(Float, nullable=True)  # 整体印象
    
    # 缺陷扣分
    defects = Column(Float, default=0)  # 缺陷扣分
    
    # 最终分数
    total_score = Column(Float, nullable=True)  # 总分
    
    # 品鉴笔记
    notes = Column(Text, nullable=True)
    tasting_notes = Column(Text, nullable=True)  # 风味描述
    
    # 系统字段
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    
    # 关系
    session = relationship("CuppingSession", back_populates="cupping_scores")
    sample = relationship("Sample", back_populates="cupping_scores")
    cupper = relationship("User", back_populates="cupping_scores")

# 咖啡产品模型（用于展示）
class Coffee(Base):
    __tablename__ = "coffees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    origin = Column(String, nullable=False)
    roast_level = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(Text, nullable=True)
    image_url = Column(String, nullable=True)
    
    # 系统字段
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    is_active = Column(Boolean, default=True) 