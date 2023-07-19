import logging.handlers
from config import BASE_PATH
import os

class GetLogger(object):
    # 定义类属性
    logger = None

    # 定义获取logger日志器的类方法
    @classmethod
    def get_logger(cls):
        # 判断类属性logger是否为空,如果为空,则执行一下操作
        if cls.logger is None:
            # 获取 日志器
            cls.logger = logging.getLogger()

            # 设置 日志器 级别
            cls.logger.setLevel(logging.INFO)

            # 获取处理器 控制台
            sh = logging.StreamHandler()

            log_path = os.path.join(BASE_PATH, "log",  "err_log.log")  # BASE_PATH：项目根目录路径
            # 获取处理器 文件-以时间分隔
            th = logging.handlers.TimedRotatingFileHandler(filename=log_path,
                                                           when="midnight",
                                                           interval=1,
                                                           backupCount=30,
                                                           encoding="utf-8")

            # 设置格式器
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s %(funcName)s:%(lineno)d] - %(message)s"
            fm = logging.Formatter(fmt)

            # 将格式器添加到 处理器 控制台
            sh.setFormatter(fm)
            # 将格式器添加到 处理器 文件
            th.setFormatter(fm)

            # 给 处理器-文件 设置 日志级别
            # th.setLevel(logging.ERROR)

            # 将处理器添加到 日志器
            cls.logger.addHandler(sh)
            cls.logger.addHandler(th)

        return cls.logger

if __name__ == '__main__':
    log = GetLogger.get_logger()
    log.info("测试信息级别日志")
    log.error("error 级别日志")
