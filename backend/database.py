from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 获取环境变量
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

if ENVIRONMENT == "production":
    # 生产环境：使用PostgreSQL
    DB_USER = os.getenv("DB_USER", "postgres")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_NAME = os.getenv("DB_NAME", "cupping_auoc")
    DB_PORT = os.getenv("DB_PORT", "5432")
    
    if not DB_PASSWORD:
        raise ValueError("DB_PASSWORD environment variable is required for production")
    
    SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    
    # PostgreSQL配置
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        pool_size=20,
        max_overflow=30,
        pool_pre_ping=True,
        echo=False  # 生产环境不输出SQL日志
    )
else:
    # 开发环境：使用SQLite
    SQLALCHEMY_DATABASE_URL = "sqlite:///./cupping_auoc.db"
    
    # SQLite配置
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        connect_args={"check_same_thread": False},
        echo=True  # 开发环境输出SQL日志便于调试
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# 依赖项：获取数据库会话
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 打印当前数据库配置信息
print(f"🗄️  Database: {ENVIRONMENT} environment")
print(f"🔗 URL: {SQLALCHEMY_DATABASE_URL.replace(os.getenv('DB_PASSWORD', ''), '*****') if 'postgresql' in SQLALCHEMY_DATABASE_URL else SQLALCHEMY_DATABASE_URL}") 