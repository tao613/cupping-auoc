#!/bin/bash

# Cupping AUOC 部署脚本
set -e

echo "🚀 开始部署 Cupping AUOC..."

# 检查Docker是否安装
if ! command -v docker &> /dev/null; then
    echo "❌ Docker 未安装，请先安装 Docker"
    exit 1
fi

if ! docker compose version &> /dev/null; then
    echo "❌ Docker Compose 未安装，请先安装 Docker Compose"
    exit 1
fi

# 创建必要的目录
echo "📁 创建必要的目录..."
mkdir -p backend/logs
mkdir -p data/postgres

# 检查前端构建文件
if [ ! -d "dist" ]; then
    echo "❌ 前端构建文件不存在，请先运行 'npm run build'"
    exit 1
fi

# 停止现有容器
echo "🛑 停止现有容器..."
docker compose down

# 构建并启动容器
echo "🔨 构建并启动容器..."
docker compose up -d --build

# 等待数据库启动
echo "⏳ 等待数据库启动..."
sleep 10

# 检查服务状态
echo "🔍 检查服务状态..."
docker compose ps

# 显示日志
echo "📋 显示服务日志..."
docker compose logs --tail=20

echo ""
echo "✅ 部署完成！"
echo "🌐 前端访问地址: http://localhost"
echo "🔗 后端API地址: http://localhost:8000"
echo "📊 API文档地址: http://localhost:8000/docs"
echo ""
echo "📝 查看日志命令:"
echo "   docker compose logs -f backend"
echo "   docker compose logs -f frontend"
echo "   docker compose logs -f postgres"
echo ""
echo "🛑 停止服务命令:"
echo "   docker compose down" 