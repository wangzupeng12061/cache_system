# edge/src/cache_manager.py

class CacheManager:
    def __init__(self, max_capacity=10):
        # 内部使用字典保存缓存数据，使用列表记录最近使用顺序（LRU策略）
        self.cache = {}
        self.order = []  # 列表中第一个元素为最久未使用的键
        self.max_capacity = max_capacity

    def has_key(self, key):
        """检查缓存中是否存在指定 key。"""
        return key in self.cache

    def get(self, key):
        """获取缓存数据，并更新该 key 的使用顺序。"""
        if key in self.cache:
            # 更新使用顺序：移除后追加到末尾（表示最近使用）
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        return None

    def put(self, key, value):
        """向缓存中写入数据，如果超过容量则淘汰最久未使用的数据。"""
        if key in self.cache:
            # 更新已有数据
            self.cache[key] = value
            self.order.remove(key)
            self.order.append(key)
        else:
            if len(self.cache) >= self.max_capacity:
                # 淘汰最早使用的 key
                lru_key = self.order.pop(0)
                del self.cache[lru_key]
            self.cache[key] = value
            self.order.append(key)
