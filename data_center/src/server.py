# data_center/src/server.py

from flask import Flask, request, jsonify
from data_manager import DataManager

app = Flask(__name__)
data_manager = DataManager()

@app.route('/data', methods=['GET'])
def get_data():
    """
    GET 请求：根据请求参数中的 key 返回数据中心对应的数据
    如果未提供 key，则默认返回 "default" 对应的数据
    """
    key = request.args.get('key', 'default')
    data = data_manager.get_data(key)
    response = {
        "source": "data_center",
        "data": data
    }
    return jsonify(response)

@app.route('/data', methods=['POST'])
def update_data():
    """
    POST 请求：接收 JSON 格式的请求体，更新数据中心中的数据
    请求体中需包含 key 和 value
    """
    if not request.is_json:
        return jsonify({"error": "请求体必须为 JSON 格式"}), 400
    
    req_data = request.get_json()
    key = req_data.get("key")
    value = req_data.get("value")
    if not key or not value:
        return jsonify({"error": "请求缺少 key 或 value"}), 400
    
    data_manager.update_data(key, value)
    return jsonify({"message": "数据更新成功", "key": key, "value": value}), 200

if __name__ == '__main__':
    # 监听所有网络接口，端口设置为 80（可根据需要修改）
    app.run(host="0.0.0.0", port=80)
