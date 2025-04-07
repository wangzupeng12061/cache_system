# common/models/caching_model.py

class CachingModel:
    """
    一个简单的缓存预测模型示例，用于计算内容的流行度分数。
    """
    def __init__(self):
        # 初始化模型参数（如果需要）
        pass

    def predict(self, features):
        """
        根据输入特征预测内容流行度分数。
        :param features: 输入特征，支持列表或字典（假设特征值为数值）。
        :return: 预测的流行度分数。
        """
        if isinstance(features, dict):
            # 简单求和作为预测结果
            return sum(features.values())
        elif isinstance(features, list):
            return sum(features)
        else:
            return 0

# 测试代码
if __name__ == "__main__":
    model = CachingModel()
    sample_features = {"views": 120, "likes": 35, "shares": 10}
    score = model.predict(sample_features)
    print("预测流行度分数:", score)
