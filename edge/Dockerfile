# edge/Dockerfile

FROM python:3.9-slim

WORKDIR /app

# 复制依赖文件并安装依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制整个边缘缓存服务代码
COPY . .

# 暴露端口（与 config.py 中的端口保持一致）
EXPOSE 80

# 启动服务
CMD ["python", "src/server.py"]
