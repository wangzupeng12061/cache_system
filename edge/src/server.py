# edge/src/server.py

from flask import Flask, request, jsonify
from config import HOST, PORT, CACHE_CAPACITY
from cache_manager import CacheManager

app = Flask(__name__)

# 初始化缓存管理器
cache_manager = CacheManager(max_capacity=CACHE_CAPACITY)

@app.route('/data', methods=['GET'])
def get_data():
    """
    处理 /data 接口的 GET 请求：
    - 根据请求参数中的 key 检查缓存是否命中。
    - 如果命中，直接返回缓存数据；否则，模拟生成数据，写入缓存后返回。
    """
    # 获取请求参数 key，默认为 "default"
    key = request.args.get('key', 'default')
    
    if cache_manager.has_key(key):
        data = cache_manager.get(key)
        source = 'cache'
    else:
        # 模拟从数据中心获取数据或动态生成数据
        data = f"Data for key: {key}"
        cache_manager.put(key, data)
        source = 'generated'
    
    response = {
        'source': source,
        'data': data
    }
    return jsonify(response)

if __name__ == '__main__':
    # 启动 Flask 服务器，监听指定的 HOST 和 PORT
    app.run(host=HOST, port=PORT)
