<<<<<<< HEAD
# 🚀 Cupping AUOC 部署指南

## 📋 部署前准备

### 系统要求
- Docker 20.10+
- Docker Compose 2.0+
- 2GB+ 内存
- 10GB+ 磁盘空间

### 1. 安装Docker (Ubuntu/Debian)
```bash
# 更新包索引
sudo apt update

# 安装Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# 安装Docker Compose
sudo apt install docker-compose-plugin

# 将用户添加到docker组
sudo usermod -aG docker $USER
```

### 2. 安装Docker (CentOS/RHEL)
```bash
# 安装Docker
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo yum install docker-ce docker-ce-cli containerd.io

# 启动Docker
sudo systemctl start docker
sudo systemctl enable docker

# 安装Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

## 🎯 快速部署

### 1. 准备项目文件
```bash
# 1. 上传项目文件到服务器
# 2. 确保已生成前端构建文件 (dist目录)
# 3. 进入项目目录
cd /path/to/your/project
```

### 2. 配置环境变量
编辑 `docker-compose.yml` 中的环境变量：

```yaml
environment:
  SECRET_KEY: "your-super-secret-key-change-this-in-production"
  ALLOWED_ORIGINS: "http://your-domain.com,https://your-domain.com"
  POSTGRES_PASSWORD: "your-secure-database-password"
```

### 3. 一键部署
```bash
# 给部署脚本执行权限
chmod +x deploy.sh

# 执行部署
./deploy.sh
```

## 🔧 手动部署步骤

### 1. 构建前端
```bash
# 在本地或CI/CD中构建前端
npm install
npm run build

# 将dist目录上传到服务器
```

### 2. 启动服务
```bash
# 启动所有服务
docker-compose up -d

# 查看服务状态
docker-compose ps

# 查看日志
docker-compose logs -f
```

### 3. 验证部署
```bash
# 检查前端
curl http://localhost

# 检查后端API
curl http://localhost:8000/health

# 检查API文档
curl http://localhost:8000/docs
```

## 🗄️ 数据库管理

### 数据备份
```bash
# 备份数据库
docker-compose exec postgres pg_dump -U postgres cupping_auoc > backup_$(date +%Y%m%d_%H%M%S).sql
```

### 数据恢复
```bash
# 恢复数据库
docker-compose exec -T postgres psql -U postgres cupping_auoc < backup_file.sql
```

### 数据库迁移
```bash
# 进入后端容器
docker-compose exec backend bash

# 运行数据库迁移（如果有的话）
python recreate_db.py
```

## 🔐 SSL证书配置

### 使用Let's Encrypt
```bash
# 安装certbot
sudo apt install certbot python3-certbot-nginx

# 获取SSL证书
sudo certbot --nginx -d your-domain.com

# 自动续期
sudo crontab -e
# 添加: 0 12 * * * /usr/bin/certbot renew --quiet
```

### 更新nginx配置
编辑 `nginx.conf` 添加SSL配置：

```nginx
server {
    listen 443 ssl;
    server_name your-domain.com;
    
    ssl_certificate /etc/letsencrypt/live/your-domain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/your-domain.com/privkey.pem;
    
    # ... 其他配置
}

# HTTP重定向到HTTPS
server {
    listen 80;
    server_name your-domain.com;
    return 301 https://$server_name$request_uri;
}
```

## 📊 监控和日志

### 查看日志
```bash
# 查看所有服务日志
docker-compose logs

# 查看特定服务日志
docker-compose logs backend
docker-compose logs frontend
docker-compose logs postgres

# 实时查看日志
docker-compose logs -f backend
```

### 系统监控
```bash
# 查看容器资源使用
docker stats

# 查看容器状态
docker-compose ps
```

## 🔄 更新部署

### 更新前端
```bash
# 1. 本地重新构建
npm run build

# 2. 上传新的dist目录到服务器

# 3. 重启前端容器
docker-compose restart frontend
```

### 更新后端
```bash
# 1. 上传新的后端代码

# 2. 重新构建并重启
docker-compose up -d --build backend
```

### 完整更新
```bash
# 停止所有服务
docker-compose down

# 重新构建并启动
docker-compose up -d --build
```

## 🛠️ 故障排除

### 常见问题

1. **容器启动失败**
```bash
# 查看详细错误
docker-compose logs backend

# 检查端口占用
sudo netstat -tlnp | grep :8000
```

2. **数据库连接失败**
```bash
# 检查数据库容器状态
docker-compose ps postgres

# 测试数据库连接
docker-compose exec postgres psql -U postgres -d cupping_auoc -c "SELECT 1;"
```

3. **前端无法访问后端**
```bash
# 检查nginx配置
docker-compose exec frontend nginx -t

# 重新加载nginx配置
docker-compose exec frontend nginx -s reload
```

### 性能优化

1. **调整worker进程数**
编辑 `backend/gunicorn.conf.py`：
```python
workers = multiprocessing.cpu_count() * 2 + 1
```

2. **数据库优化**
编辑 `docker-compose.yml`：
```yaml
postgres:
  command: postgres -c shared_preload_libraries=pg_stat_statements -c max_connections=100
```

## 📞 技术支持

如果遇到部署问题，请检查：
1. Docker和Docker Compose版本
2. 系统资源（内存、磁盘空间）
3. 网络连接和防火墙设置
4. 日志文件中的错误信息

---
=======
# 🚀 Cupping AUOC 部署指南

## 📋 部署前准备

### 系统要求
- Docker 20.10+
- Docker Compose 2.0+
- 2GB+ 内存
- 10GB+ 磁盘空间

### 1. 安装Docker (Ubuntu/Debian)
```bash
# 更新包索引
sudo apt update

# 安装Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# 安装Docker Compose
sudo apt install docker-compose-plugin

# 将用户添加到docker组
sudo usermod -aG docker $USER
```

### 2. 安装Docker (CentOS/RHEL)
```bash
# 安装Docker
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo yum install docker-ce docker-ce-cli containerd.io

# 启动Docker
sudo systemctl start docker
sudo systemctl enable docker

# 安装Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

## 🎯 快速部署

### 1. 准备项目文件
```bash
# 1. 上传项目文件到服务器
# 2. 确保已生成前端构建文件 (dist目录)
# 3. 进入项目目录
cd /path/to/your/project
```

### 2. 配置环境变量
编辑 `docker-compose.yml` 中的环境变量：

```yaml
environment:
  SECRET_KEY: "your-super-secret-key-change-this-in-production"
  ALLOWED_ORIGINS: "http://your-domain.com,https://your-domain.com"
  POSTGRES_PASSWORD: "your-secure-database-password"
```

### 3. 一键部署
```bash
# 给部署脚本执行权限
chmod +x deploy.sh

# 执行部署
./deploy.sh
```

## 🔧 手动部署步骤

### 1. 构建前端
```bash
# 在本地或CI/CD中构建前端
npm install
npm run build

# 将dist目录上传到服务器
```

### 2. 启动服务
```bash
# 启动所有服务
docker-compose up -d

# 查看服务状态
docker-compose ps

# 查看日志
docker-compose logs -f
```

### 3. 验证部署
```bash
# 检查前端
curl http://localhost

# 检查后端API
curl http://localhost:8000/health

# 检查API文档
curl http://localhost:8000/docs
```

## 🗄️ 数据库管理

### 数据备份
```bash
# 备份数据库
docker-compose exec postgres pg_dump -U postgres cupping_auoc > backup_$(date +%Y%m%d_%H%M%S).sql
```

### 数据恢复
```bash
# 恢复数据库
docker-compose exec -T postgres psql -U postgres cupping_auoc < backup_file.sql
```

### 数据库迁移
```bash
# 进入后端容器
docker-compose exec backend bash

# 运行数据库迁移（如果有的话）
python recreate_db.py
```

## 🔐 SSL证书配置

### 使用Let's Encrypt
```bash
# 安装certbot
sudo apt install certbot python3-certbot-nginx

# 获取SSL证书
sudo certbot --nginx -d your-domain.com

# 自动续期
sudo crontab -e
# 添加: 0 12 * * * /usr/bin/certbot renew --quiet
```

### 更新nginx配置
编辑 `nginx.conf` 添加SSL配置：

```nginx
server {
    listen 443 ssl;
    server_name your-domain.com;
    
    ssl_certificate /etc/letsencrypt/live/your-domain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/your-domain.com/privkey.pem;
    
    # ... 其他配置
}

# HTTP重定向到HTTPS
server {
    listen 80;
    server_name your-domain.com;
    return 301 https://$server_name$request_uri;
}
```

## 📊 监控和日志

### 查看日志
```bash
# 查看所有服务日志
docker-compose logs

# 查看特定服务日志
docker-compose logs backend
docker-compose logs frontend
docker-compose logs postgres

# 实时查看日志
docker-compose logs -f backend
```

### 系统监控
```bash
# 查看容器资源使用
docker stats

# 查看容器状态
docker-compose ps
```

## 🔄 更新部署

### 更新前端
```bash
# 1. 本地重新构建
npm run build

# 2. 上传新的dist目录到服务器

# 3. 重启前端容器
docker-compose restart frontend
```

### 更新后端
```bash
# 1. 上传新的后端代码

# 2. 重新构建并重启
docker-compose up -d --build backend
```

### 完整更新
```bash
# 停止所有服务
docker-compose down

# 重新构建并启动
docker-compose up -d --build
```

## 🛠️ 故障排除

### 常见问题

1. **容器启动失败**
```bash
# 查看详细错误
docker-compose logs backend

# 检查端口占用
sudo netstat -tlnp | grep :8000
```

2. **数据库连接失败**
```bash
# 检查数据库容器状态
docker-compose ps postgres

# 测试数据库连接
docker-compose exec postgres psql -U postgres -d cupping_auoc -c "SELECT 1;"
```

3. **前端无法访问后端**
```bash
# 检查nginx配置
docker-compose exec frontend nginx -t

# 重新加载nginx配置
docker-compose exec frontend nginx -s reload
```

### 性能优化

1. **调整worker进程数**
编辑 `backend/gunicorn.conf.py`：
```python
workers = multiprocessing.cpu_count() * 2 + 1
```

2. **数据库优化**
编辑 `docker-compose.yml`：
```yaml
postgres:
  command: postgres -c shared_preload_libraries=pg_stat_statements -c max_connections=100
```

## 📞 技术支持

如果遇到部署问题，请检查：
1. Docker和Docker Compose版本
2. 系统资源（内存、磁盘空间）
3. 网络连接和防火墙设置
4. 日志文件中的错误信息

---
>>>>>>> main
**注意**: 生产环境请务必修改默认密码和密钥！ 