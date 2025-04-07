# common/utils/logging_util.py

import logging
import os

def setup_logger(name=__name__, log_level=logging.INFO, log_file=None):
    """
    初始化并返回一个 Logger 实例。
    :param name: Logger 名称。
    :param log_level: 日志级别。
    :param log_file: 如果提供，将日志同时写入该文件。
    :return: 配置好的 Logger 对象。
    """
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    # 控制台处理器
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # 如果提供日志文件，则添加文件处理器
    if log_file:
        fh = logging.FileHandler(log_file)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    
    return logger

# 测试代码
if __name__ == "__main__":
    logger = setup_logger("TestLogger", logging.DEBUG, "test.log")
    logger.debug("这是一条调试信息")
    logger.info("这是一条普通信息")
