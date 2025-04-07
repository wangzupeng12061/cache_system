import requests
import sys
import json
from client.src.config import EDGE_SERVER_URL

def fetch_data(endpoint="/data"):
    """
    向边缘缓存服务器发送 GET 请求获取数据。
    :param endpoint: 访问的接口路径，默认访问 /data 接口
    :return: 返回响应的 JSON 数据
    """
    url = f"{EDGE_SERVER_URL}{endpoint}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # 如果响应状态码不是 200，将抛出异常
        return response.json()       # 假设服务端返回 JSON 格式数据
    except requests.RequestException as e:
        print(f"请求边缘缓存服务时出错: {e}")
        sys.exit(1)

def main():
    print("客户端开始发送请求到边缘缓存服务...")
    data = fetch_data()  # 根据实际情况调整 endpoint
    print("接收到的数据:")
    # 美化输出 JSON 数据
    print(json.dumps(data, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    main()
