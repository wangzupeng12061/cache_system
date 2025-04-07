# data_center/src/data_manager.py

class DataManager:
    def __init__(self):
        # 模拟持久化数据存储，这里使用一个字典进行存储
        self.data_store = {
            "default": "这是数据中心默认的数据",
            "key1": "数据中心：key1 的数据",
            "key2": "数据中心：key2 的数据"
        }
    
    def get_data(self, key):
        """
        根据 key 获取数据，如果没有则返回一个默认提示信息
        """
        return self.data_store.get(key, f"数据中心中未找到 key: {key} 对应的数据")
    
    def update_data(self, key, value):
        """
        更新或添加数据到数据中心
        """
        self.data_store[key] = value
        return True
