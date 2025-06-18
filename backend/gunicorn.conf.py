<<<<<<< HEAD
# Gunicorn配置文件
import multiprocessing
import os

# 绑定地址和端口
bind = f"0.0.0.0:{os.getenv('API_PORT', '8000')}"

# 工作进程数
workers = multiprocessing.cpu_count() * 2 + 1

# 工作进程类型
worker_class = "uvicorn.workers.UvicornWorker"

# 工作进程超时时间
timeout = 120
keepalive = 5

# 最大请求数
max_requests = 1000
max_requests_jitter = 100

# 日志配置 - 使用标准输出（适合容器化部署）
accesslog = "-"  # 输出到 stdout
errorlog = "-"   # 输出到 stderr
loglevel = "info"

# 预加载应用
preload_app = True

# 进程名称
proc_name = "cupping-auoc-api"

# 用户和组 - 使用容器中的app用户
user = "app"
=======
# Gunicorn配置文件
import multiprocessing
import os

# 绑定地址和端口
bind = f"0.0.0.0:{os.getenv('API_PORT', '8000')}"

# 工作进程数
workers = multiprocessing.cpu_count() * 2 + 1

# 工作进程类型
worker_class = "uvicorn.workers.UvicornWorker"

# 工作进程超时时间
timeout = 120
keepalive = 5

# 最大请求数
max_requests = 1000
max_requests_jitter = 100

# 日志配置 - 使用标准输出（适合容器化部署）
accesslog = "-"  # 输出到 stdout
errorlog = "-"   # 输出到 stderr
loglevel = "info"

# 预加载应用
preload_app = True

# 进程名称
proc_name = "cupping-auoc-api"

# 用户和组 - 使用容器中的app用户
user = "app"
>>>>>>> main
group = "app" 