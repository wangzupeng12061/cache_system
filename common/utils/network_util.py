# common/utils/network_util.py

import requests

def fetch_url(url, params=None, timeout=5):
    """
    通过 HTTP GET 请求获取指定 URL 的 JSON 数据。
    :param url: 请求的 URL 地址。
    :param params: 可选的查询参数，字典形式。
    :param timeout: 请求超时时间，默认 5 秒。
    :return: 如果请求成功返回 JSON 数据，否则返回 None。
    """
    try:
        response = requests.get(url, params=params, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"请求 {url} 时出错: {e}")
        return None

# 测试代码
if __name__ == "__main__":
    test_url = "https://jsonplaceholder.typicode.com/todos/1"
    result = fetch_url(test_url)
    print(result)
