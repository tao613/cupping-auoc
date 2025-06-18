from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import coffee, users, samples
from database import engine
import models

# 创建数据库表
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Cupping AUOC API", description="专业咖啡品鉴应用API", version="2.0.0")

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173", 
        "http://localhost:5174",  # Vite可能使用的备用端口
        "http://127.0.0.1:5173",
        "http://127.0.0.1:5174"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 包含路由
app.include_router(coffee.router)
app.include_router(users.router)
app.include_router(samples.router)

@app.get("/")
async def root():
    return {
        "message": "Welcome to Cupping AUOC API",
        "description": "专业咖啡品鉴应用后端API",
        "version": "2.0.0",
        "features": [
            "用户认证与授权",
            "样品管理",
            "品鉴会话管理", 
            "品鉴评分系统"
        ]
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "database": "connected"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 