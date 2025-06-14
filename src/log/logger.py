from loguru import logger
import os

#current file name + "logs"
log_dir = os.path.join(os.path.dirname(__file__), "logs")
os.makedirs(log_dir, exist_ok=True)

logger.add(
    os.path.join(log_dir, "app_{time}.log"),
    rotation="500 KB",        # 单个文件大小上限
    retention="7 days",       # 保留时间
    encoding="utf-8",         # 编码
    enqueue=True,             # 多线程安全
    backtrace=True,           # 更详细错误栈
    diagnose=True             # 更详细变量信息
)

__all__ = ["logger"]