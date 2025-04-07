# 使用官方 Python 3.9 slim 镜像作为基础镜像
FROM python:3.9-slim

# 设置工作目录为 /app
WORKDIR /app

# 将 requirements.txt 复制到容器中
COPY requirements.txt /app

# 安装所需依赖
RUN pip install --no-cache-dir -r requirements.txt

# 将客户端的所有代码复制到容器中
COPY . /app

# 容器启动后默认执行的命令
CMD ["python", "src/main.py"]
