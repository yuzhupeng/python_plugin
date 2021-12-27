import os
import logging
import re
from logging.handlers import TimedRotatingFileHandler


def setup_log(log_name):
    # 创建logger对象。传入logger名字
    log_dir = os.path.dirname(os.path.abspath(__file__)) + os.sep + 'logs' 
    logger = logging.getLogger(log_name)
    log_path = log_dir
    # 设置日志记录等级
    logger.setLevel(logging.INFO)
    # interval 滚动周期，
    # when="MIDNIGHT", interval=1 表示每天0点为更新点，每天生成一个文件
    # backupCount  表示日志保存个数
    file_handler = TimedRotatingFileHandler(
        filename=log_path, when="MIDNIGHT", interval=1, backupCount=30
    )
    # filename="mylog" suffix设置，会生成文件名为mylog.2020-02-25.log
    file_handler.suffix = "%Y-%m-%d.log"
    # extMatch是编译好正则表达式，用于匹配日志文件名后缀
    # 需要注意的是suffix和extMatch一定要匹配的上，如果不匹配，过期日志不会被删除。
    file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}.log$")
    # 定义日志输出格式
    file_handler.setFormatter(
        logging.Formatter(
            "[%(asctime)s] [%(process)d] [%(levelname)s] - %(module)s.%(funcName)s (%(filename)s:%(lineno)d) - %(message)s"
        )
    )
    logger.addHandler(file_handler)
    return logger


if __name__ == "__main__":
    logger = setup_log("mylog")
    logger.info("this is info message")
    logger.warning("this is a warning message")
    try:
        int("xjk")
    except ValueError as e:
        logger.error(e)
# 如果其他py文件想使用此配置日志，只需 logging.getLogger(日志的名字)  即可

