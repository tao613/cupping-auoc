from pydantic import BaseModel, validator
from typing import Optional, List
from datetime import datetime
from models import UserRole, SampleType, ProcessingMethod, RoastLevel, CuppingSessionStatus

# 用户相关schemas
class UserBase(BaseModel):
    email: str
    username: str
    name: Optional[str] = None
    role: UserRole = UserRole.CUPPER
    
    # 联系信息
    phone: Optional[str] = None
    
    # 地址信息
    country: Optional[str] = None
    city: Optional[str] = None
    address: Optional[str] = None
    zip_code: Optional[str] = None
    
    # 个人资料
    avatar: Optional[str] = None
    
    # 品鉴师相关信息
    certification_level: Optional[str] = None
    experience_years: Optional[int] = None
    bio: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None
    
    # 联系信息
    phone: Optional[str] = None
    
    # 地址信息
    country: Optional[str] = None
    city: Optional[str] = None
    address: Optional[str] = None
    zip_code: Optional[str] = None
    
    # 个人资料
    avatar: Optional[str] = None
    
    # 品鉴师相关信息
    certification_level: Optional[str] = None
    experience_years: Optional[int] = None
    bio: Optional[str] = None

class PasswordChange(BaseModel):
    current_password: str
    new_password: str
    
    @validator('new_password')
    def validate_password(cls, v):
        if len(v) < 6:
            raise ValueError('Password must be at least 6 characters long')
        return v

class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

# Coffee相关schemas（保持向后兼容）
class CoffeeBase(BaseModel):
    name: str
    description: Optional[str] = None
    origin: Optional[str] = None
    roast_level: Optional[str] = None
    price: Optional[float] = None
    image_url: Optional[str] = None

class CoffeeCreate(CoffeeBase):
    pass

class Coffee(CoffeeBase):
    id: int

    class Config:
        from_attributes = True

# 样品相关schemas
class SampleBase(BaseModel):
    name: str
    code: str
    description: Optional[str] = None
    
    # 产地信息
    country: str
    region: Optional[str] = None
    farm: Optional[str] = None
    altitude: Optional[int] = None
    
    # 咖啡品种信息
    variety: Optional[str] = None
    sample_type: SampleType
    processing_method: Optional[ProcessingMethod] = None
    
    # 烘焙信息
    roast_date: Optional[datetime] = None
    roast_level: Optional[RoastLevel] = None
    roaster: Optional[str] = None
    
    # 样品状态
    harvest_year: Optional[int] = None
    expiry_date: Optional[datetime] = None
    
    # 质量信息
    moisture_content: Optional[float] = None
    density: Optional[float] = None
    screen_size: Optional[str] = None
    
    # 供应商信息
    supplier: Optional[str] = None
    lot_number: Optional[str] = None

    @validator('altitude')
    def validate_altitude(cls, v):
        if v is not None and (v < 0 or v > 5000):
            raise ValueError('Altitude must be between 0 and 5000 meters')
        return v

    @validator('harvest_year')
    def validate_harvest_year(cls, v):
        if v is not None and (v < 1900 or v > datetime.now().year):
            raise ValueError('Harvest year must be between 1900 and current year')
        return v

class SampleCreate(SampleBase):
    pass

class SampleUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    country: Optional[str] = None
    region: Optional[str] = None
    farm: Optional[str] = None
    altitude: Optional[int] = None
    variety: Optional[str] = None
    sample_type: Optional[SampleType] = None
    processing_method: Optional[ProcessingMethod] = None
    roast_date: Optional[datetime] = None
    roast_level: Optional[RoastLevel] = None
    roaster: Optional[str] = None
    harvest_year: Optional[int] = None
    expiry_date: Optional[datetime] = None
    moisture_content: Optional[float] = None
    density: Optional[float] = None
    screen_size: Optional[str] = None
    supplier: Optional[str] = None
    lot_number: Optional[str] = None

class Sample(SampleBase):
    id: int
    received_date: datetime
    created_at: datetime
    updated_at: datetime
    is_active: bool

    class Config:
        from_attributes = True

# 品鉴会话相关schemas
class CuppingSessionBase(BaseModel):
    name: str
    description: Optional[str] = None
    session_date: datetime
    head_cupper_id: int
    water_temperature: Optional[float] = None
    grind_size: Optional[str] = None
    coffee_to_water_ratio: Optional[str] = None

class CuppingSessionCreate(CuppingSessionBase):
    sample_ids: List[int] = []

class CuppingSessionUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    session_date: Optional[datetime] = None
    status: Optional[CuppingSessionStatus] = None
    water_temperature: Optional[float] = None
    grind_size: Optional[str] = None
    coffee_to_water_ratio: Optional[str] = None

class CuppingSession(CuppingSessionBase):
    id: int
    status: CuppingSessionStatus
    created_at: datetime
    updated_at: datetime
    head_cupper: User

    class Config:
        from_attributes = True

# 品鉴评分相关schemas
class CuppingScoreBase(BaseModel):
    session_id: int
    sample_id: int
    
    # SCA标准品鉴评分项目
    fragrance_aroma: Optional[float] = None
    flavor: Optional[float] = None
    aftertaste: Optional[float] = None
    acidity: Optional[float] = None
    body: Optional[float] = None
    balance: Optional[float] = None
    uniformity: Optional[float] = None
    clean_cup: Optional[float] = None
    sweetness: Optional[float] = None
    overall: Optional[float] = None
    defects: float = 0
    
    # 品鉴笔记
    notes: Optional[str] = None
    tasting_notes: Optional[str] = None

    @validator('fragrance_aroma', 'flavor', 'aftertaste', 'acidity', 'body', 'balance', 'overall')
    def validate_main_scores(cls, v):
        if v is not None and (v < 0 or v > 10):
            raise ValueError('Score must be between 0 and 10')
        return v

    @validator('uniformity', 'clean_cup', 'sweetness')
    def validate_binary_scores(cls, v):
        if v is not None and (v < 0 or v > 10):
            raise ValueError('Score must be between 0 and 10')
        return v

    @validator('defects')
    def validate_defects(cls, v):
        if v < 0 or v > 10:
            raise ValueError('Defects must be between 0 and 10')
        return v

class CuppingScoreCreate(CuppingScoreBase):
    pass

class CuppingScoreUpdate(BaseModel):
    fragrance_aroma: Optional[float] = None
    flavor: Optional[float] = None
    aftertaste: Optional[float] = None
    acidity: Optional[float] = None
    body: Optional[float] = None
    balance: Optional[float] = None
    uniformity: Optional[float] = None
    clean_cup: Optional[float] = None
    sweetness: Optional[float] = None
    overall: Optional[float] = None
    defects: Optional[float] = None
    notes: Optional[str] = None
    tasting_notes: Optional[str] = None

class CuppingScore(CuppingScoreBase):
    id: int
    cupper_id: int
    total_score: Optional[float] = None
    created_at: datetime
    updated_at: datetime
    cupper: User
    sample: Sample

    class Config:
        from_attributes = True

# Token相关schemas（保持不变）
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# 响应schemas
class PaginatedResponse(BaseModel):
    data: List
    pagination: dict

class SampleListResponse(BaseModel):
    data: List[Sample]
    pagination: dict

class CuppingSessionListResponse(BaseModel):
    data: List[CuppingSession]
    pagination: dict 