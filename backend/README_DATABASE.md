<<<<<<< HEAD
# 📊 数据库配置说明

## 🎯 为什么使用不同的数据库？

### **开发环境 - SQLite**
我们在开发阶段使用SQLite的原因：

#### ✅ **优势**
- **零配置**：无需安装和配置数据库服务器
- **快速开始**：克隆项目即可运行，降低开发门槛
- **轻量级**：适合个人开发和小团队
- **便于调试**：数据库文件可以直接查看和操作
- **快速迭代**：模式变更和数据重置非常简单

#### ⚠️ **限制**
- 不支持真正的并发写入
- 缺乏高级数据库功能
- 不适合生产环境的大量数据

### **生产环境 - PostgreSQL**
生产环境推荐使用PostgreSQL：

#### ✅ **优势**
- **企业级性能**：优秀的查询优化器和并发处理
- **ACID兼容性**：完整的事务支持
- **丰富的数据类型**：JSON、数组、地理数据等
- **扩展性**：支持读写分离、分区表等
- **安全性**：完善的用户权限管理

## 🔧 配置切换

### **开发环境配置**
```bash
# .env 文件
ENVIRONMENT=development
# SQLite会自动使用，无需其他配置
```

### **生产环境配置**
```bash
# .env 文件
ENVIRONMENT=production
DB_USER=postgres
DB_PASSWORD=your_secure_password
DB_HOST=your_database_host
DB_PORT=5432
DB_NAME=cupping_auoc
```

## 🚀 部署建议

### **开发流程**
1. 本地开发使用SQLite
2. 功能完成后测试PostgreSQL兼容性
3. 使用Docker Compose进行本地PostgreSQL测试

### **生产部署**
1. 使用托管的PostgreSQL服务（如AWS RDS、Google Cloud SQL）
2. 配置数据库连接池
3. 设置数据库备份策略
4. 启用慢查询监控

## 📝 数据库迁移

当从SQLite迁移到PostgreSQL时：

```bash
# 1. 设置生产环境变量
export ENVIRONMENT=production

# 2. 创建数据库表
python -c "from database import engine, Base; Base.metadata.create_all(bind=engine)"

# 3. 如果有数据需要迁移，可以使用SQL导出/导入
```

## 🔍 最佳实践

1. **开发阶段**：使用SQLite快速迭代
2. **测试阶段**：在类生产环境中测试PostgreSQL
3. **生产阶段**：使用PostgreSQL + 连接池 + 监控
4. **数据备份**：定期备份生产数据库
=======
# 📊 数据库配置说明

## 🎯 为什么使用不同的数据库？

### **开发环境 - SQLite**
我们在开发阶段使用SQLite的原因：

#### ✅ **优势**
- **零配置**：无需安装和配置数据库服务器
- **快速开始**：克隆项目即可运行，降低开发门槛
- **轻量级**：适合个人开发和小团队
- **便于调试**：数据库文件可以直接查看和操作
- **快速迭代**：模式变更和数据重置非常简单

#### ⚠️ **限制**
- 不支持真正的并发写入
- 缺乏高级数据库功能
- 不适合生产环境的大量数据

### **生产环境 - PostgreSQL**
生产环境推荐使用PostgreSQL：

#### ✅ **优势**
- **企业级性能**：优秀的查询优化器和并发处理
- **ACID兼容性**：完整的事务支持
- **丰富的数据类型**：JSON、数组、地理数据等
- **扩展性**：支持读写分离、分区表等
- **安全性**：完善的用户权限管理

## 🔧 配置切换

### **开发环境配置**
```bash
# .env 文件
ENVIRONMENT=development
# SQLite会自动使用，无需其他配置
```

### **生产环境配置**
```bash
# .env 文件
ENVIRONMENT=production
DB_USER=postgres
DB_PASSWORD=your_secure_password
DB_HOST=your_database_host
DB_PORT=5432
DB_NAME=cupping_auoc
```

## 🚀 部署建议

### **开发流程**
1. 本地开发使用SQLite
2. 功能完成后测试PostgreSQL兼容性
3. 使用Docker Compose进行本地PostgreSQL测试

### **生产部署**
1. 使用托管的PostgreSQL服务（如AWS RDS、Google Cloud SQL）
2. 配置数据库连接池
3. 设置数据库备份策略
4. 启用慢查询监控

## 📝 数据库迁移

当从SQLite迁移到PostgreSQL时：

```bash
# 1. 设置生产环境变量
export ENVIRONMENT=production

# 2. 创建数据库表
python -c "from database import engine, Base; Base.metadata.create_all(bind=engine)"

# 3. 如果有数据需要迁移，可以使用SQL导出/导入
```

## 🔍 最佳实践

1. **开发阶段**：使用SQLite快速迭代
2. **测试阶段**：在类生产环境中测试PostgreSQL
3. **生产阶段**：使用PostgreSQL + 连接池 + 监控
4. **数据备份**：定期备份生产数据库
>>>>>>> main
5. **性能监控**：监控查询性能和连接池状态 