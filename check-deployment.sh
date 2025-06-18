#!/bin/bash

# Cupping AUOC 部署检查脚本
set -e

echo "🔍 检查部署环境..."

# 检查必要的文件
echo "📁 检查必要文件..."

required_files=(
    "docker-compose.yml"
    "nginx.conf"
    "deploy.sh"
    "backend/Dockerfile"
    "backend/requirements.txt"
    "backend/main.py"
    "backend/gunicorn.conf.py"
    "dist/index.html"
)

missing_files=()

for file in "${required_files[@]}"; do
    if [ ! -f "$file" ]; then
        missing_files+=("$file")
    else
        echo "✅ $file 存在"
    fi
done

if [ ${#missing_files[@]} -ne 0 ]; then
    echo "❌ 缺少以下必要文件:"
    for file in "${missing_files[@]}"; do
        echo "   - $file"
    done
    exit 1
fi

# 检查dist目录
echo ""
echo "📦 检查前端构建文件..."
if [ ! -d "dist" ]; then
    echo "❌ dist 目录不存在，请先运行 'npm run build'"
    exit 1
fi

dist_files=("index.html" "assets")
for file in "${dist_files[@]}"; do
    if [ ! -e "dist/$file" ]; then
        echo "❌ dist/$file 不存在"
        exit 1
    else
        echo "✅ dist/$file 存在"
    fi
done

# 检查Docker环境
echo ""
echo "🐳 检查Docker环境..."
if ! command -v docker &> /dev/null; then
    echo "❌ Docker 未安装"
    exit 1
else
    echo "✅ Docker 已安装: $(docker --version)"
fi

if ! docker compose version &> /dev/null; then
    echo "❌ Docker Compose 未安装"
    exit 1
else
    echo "✅ Docker Compose 已安装: $(docker compose version)"
fi

# 检查端口占用
echo ""
echo "🔌 检查端口占用..."
ports=(80 8000 5432)
for port in "${ports[@]}"; do
    if lsof -Pi :$port -sTCP:LISTEN -t >/dev/null 2>&1; then
        echo "⚠️  端口 $port 已被占用"
        echo "   占用进程: $(lsof -ti:$port | xargs ps -p | tail -n +2)"
    else
        echo "✅ 端口 $port 可用"
    fi
done

# 检查磁盘空间
echo ""
echo "💾 检查磁盘空间..."
available_space=$(df -h . | awk 'NR==2 {print $4}')
echo "✅ 可用空间: $available_space"

# 检查内存
echo ""
echo "🧠 检查内存..."
total_memory=$(free -h | awk 'NR==2 {print $2}')
available_memory=$(free -h | awk 'NR==2 {print $7}')
echo "✅ 总内存: $total_memory, 可用内存: $available_memory"

# 检查docker-compose配置
echo ""
echo "⚙️  验证Docker Compose配置..."
if docker compose config > /dev/null 2>&1; then
    echo "✅ Docker Compose 配置有效"
else
    echo "❌ Docker Compose 配置无效"
    docker compose config
    exit 1
fi

echo ""
echo "🎉 所有检查通过！可以执行部署了"
echo ""
echo "🚀 运行部署命令:"
echo "   chmod +x deploy.sh"
echo "   ./deploy.sh"
echo ""
echo "📊 部署后访问地址:"
echo "   前端: http://localhost"
echo "   后端API: http://localhost:8000"
echo "   API文档: http://localhost:8000/docs" 