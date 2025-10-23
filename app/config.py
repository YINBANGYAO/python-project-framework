import os
from typing import Optional

class Config:
    """配置类，用于管理应用程序设置"""
    
    def __init__(self):
        self.environment = os.getenv("ENVIRONMENT", "development")
        self.debug_mode = os.getenv("DEBUG", "False").lower() == "true"
        self.database_url = os.getenv("DATABASE_URL")
        self.api_key = os.getenv("API_KEY")
        self.secret_key = os.getenv("SECRET_KEY")
    
    def validate(self) -> bool:
        """验证必要的配置是否存在"""
        required_vars = ["SECRET_KEY"]
        missing_vars = [var for var in required_vars if not getattr(self, var, None)]
        
        if missing_vars:
            raise ValueError(f"缺少必要的环境变量: {', '.join(missing_vars)}")
        
        return True
    
    def __str__(self) -> str:
        return f"Config(environment={self.environment}, debug={self.debug_mode})"