<<<<<<< HEAD
#!/usr/bin/env python3
"""
数据库重新创建脚本
删除旧的数据库文件并创建新的数据库表结构
"""

import os
import sys
from database import engine, Base
import models

def recreate_database():
    """重新创建数据库"""
    db_file = "cupping_auoc.db"
    
    # 删除现有的数据库文件
    if os.path.exists(db_file):
        try:
            os.remove(db_file)
            print(f"✅ 已删除旧的数据库文件: {db_file}")
        except OSError as e:
            print(f"❌ 无法删除数据库文件: {e}")
            print("请确保没有程序正在使用数据库文件，然后重试")
            return False
    
    # 创建新的数据库表
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ 数据库表已重新创建")
        print("📋 创建的表:")
        for table_name in Base.metadata.tables.keys():
            print(f"   - {table_name}")
        
        # 显示用户表的字段信息
        print("👤 用户表字段:")
        for column in Base.metadata.tables['users'].columns:
            print(f"   - {column.name}: {column.type}")
        
        return True
    except Exception as e:
        print(f"❌ 创建数据库表时出错: {e}")
        return False

if __name__ == "__main__":
    print("🗄️  开始重新创建数据库...")
    if recreate_database():
        print("🎉 数据库重新创建成功!")
        print("💡 现在可以重新启动应用程序")
    else:
        print("💥 数据库重新创建失败")
=======
#!/usr/bin/env python3
"""
数据库重新创建脚本
删除旧的数据库文件并创建新的数据库表结构
"""

import os
import sys
from database import engine, Base
import models

def recreate_database():
    """重新创建数据库"""
    db_file = "cupping_auoc.db"
    
    # 删除现有的数据库文件
    if os.path.exists(db_file):
        try:
            os.remove(db_file)
            print(f"✅ 已删除旧的数据库文件: {db_file}")
        except OSError as e:
            print(f"❌ 无法删除数据库文件: {e}")
            print("请确保没有程序正在使用数据库文件，然后重试")
            return False
    
    # 创建新的数据库表
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ 数据库表已重新创建")
        print("📋 创建的表:")
        for table_name in Base.metadata.tables.keys():
            print(f"   - {table_name}")
        
        # 显示用户表的字段信息
        print("👤 用户表字段:")
        for column in Base.metadata.tables['users'].columns:
            print(f"   - {column.name}: {column.type}")
        
        return True
    except Exception as e:
        print(f"❌ 创建数据库表时出错: {e}")
        return False

if __name__ == "__main__":
    print("🗄️  开始重新创建数据库...")
    if recreate_database():
        print("🎉 数据库重新创建成功!")
        print("💡 现在可以重新启动应用程序")
    else:
        print("💥 数据库重新创建失败")
>>>>>>> main
        sys.exit(1) 