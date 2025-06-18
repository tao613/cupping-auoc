<<<<<<< HEAD
# Cupping AUOC 快速部署指南

## 📋 部署前准备

确保您的系统已安装：
- Docker 20.10+
- Docker Compose 2.0+
- 2GB+ 内存
- 10GB+ 磁盘空间

## 🚀 一键部署

### 1. 运行部署检查
```bash
chmod +x check-deployment.sh
./check-deployment.sh
```

### 2. 执行部署
```bash
chmod +x deploy.sh
./deploy.sh
```

### 3. 验证部署
```bash
# 检查服务状态
docker-compose ps

# 访问应用
# 前端: http://localhost
# 后端API: http://localhost:8000
# API文档: http://localhost:8000/docs
```

## 📁 部署文件结构

```
cupping-auoc/
├── 📂 backend/              # 后端代码
│   ├── main.py             # FastAPI应用
│   ├── Dockerfile          # 后端容器配置
│   ├── requirements.txt    # Python依赖
│   └── gunicorn.conf.py    # Web服务器配置
├── 📂 dist/                # 前端构建文件
│   ├── index.html          # 入口文件
│   └── assets/             # 静态资源
├── docker-compose.yml      # 容器编排配置
├── nginx.conf              # Web服务器配置
├── deploy.sh               # 部署脚本
├── check-deployment.sh     # 部署检查脚本
└── DEPLOYMENT.md          # 详细部署文档
```

## 🔧 常用命令

```bash
# 查看服务状态
docker-compose ps

# 查看日志
docker-compose logs -f

# 重启服务
docker-compose restart

# 停止服务
docker-compose down

# 完全重新部署
docker-compose down && docker-compose up -d --build
```

## 🛠️ 故障排除

1. **端口冲突**：确保端口 80、8000、5432 未被占用
2. **权限问题**：确保脚本有执行权限 `chmod +x *.sh`
3. **内存不足**：至少需要 2GB 可用内存
4. **磁盘空间**：确保有足够的磁盘空间存储镜像和数据

## 📞 获取帮助

如果遇到问题：
1. 查看详细部署文档：`DEPLOYMENT.md`
2. 检查服务日志：`docker-compose logs [service-name]`
3. 验证配置文件：`docker-compose config`

---
=======
# Cupping AUOC 快速部署指南

## 📋 部署前准备

确保您的系统已安装：
- Docker 20.10+
- Docker Compose 2.0+
- 2GB+ 内存
- 10GB+ 磁盘空间

## 🚀 一键部署

### 1. 运行部署检查
```bash
chmod +x check-deployment.sh
./check-deployment.sh
```

### 2. 执行部署
```bash
chmod +x deploy.sh
./deploy.sh
```

### 3. 验证部署
```bash
# 检查服务状态
docker-compose ps

# 访问应用
# 前端: http://localhost
# 后端API: http://localhost:8000
# API文档: http://localhost:8000/docs
```

## 📁 部署文件结构

```
cupping-auoc/
├── 📂 backend/              # 后端代码
│   ├── main.py             # FastAPI应用
│   ├── Dockerfile          # 后端容器配置
│   ├── requirements.txt    # Python依赖
│   └── gunicorn.conf.py    # Web服务器配置
├── 📂 dist/                # 前端构建文件
│   ├── index.html          # 入口文件
│   └── assets/             # 静态资源
├── docker-compose.yml      # 容器编排配置
├── nginx.conf              # Web服务器配置
├── deploy.sh               # 部署脚本
├── check-deployment.sh     # 部署检查脚本
└── DEPLOYMENT.md          # 详细部署文档
```

## 🔧 常用命令

```bash
# 查看服务状态
docker-compose ps

# 查看日志
docker-compose logs -f

# 重启服务
docker-compose restart

# 停止服务
docker-compose down

# 完全重新部署
docker-compose down && docker-compose up -d --build
```

## 🛠️ 故障排除

1. **端口冲突**：确保端口 80、8000、5432 未被占用
2. **权限问题**：确保脚本有执行权限 `chmod +x *.sh`
3. **内存不足**：至少需要 2GB 可用内存
4. **磁盘空间**：确保有足够的磁盘空间存储镜像和数据

## 📞 获取帮助

如果遇到问题：
1. 查看详细部署文档：`DEPLOYMENT.md`
2. 检查服务日志：`docker-compose logs [service-name]`
3. 验证配置文件：`docker-compose config`

---
>>>>>>> main
**注意**：生产环境部署前请修改默认密码和密钥！ 