import os
import logging
from dotenv import load_dotenv
from .config import Config
from .calculator import Calculator

# 设置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    """主应用程序入口"""
    # 加载环境变量
    load_dotenv()
    
    # 初始化配置
    config = Config()
    
    # 初始化计算器
    calc = Calculator()
    
    logger.info("应用程序启动")
    logger.info(f"环境: {config.environment}")
    logger.info(f"调试模式: {config.debug_mode}")
    
    # 演示功能
    result = calc.add(10, 5)
    logger.info(f"10 + 5 = {result}")
    
    result = calc.multiply(4, 7)
    logger.info(f"4 * 7 = {result}")
    
    logger.info("应用程序执行完成")

if __name__ == "__main__":
    main()