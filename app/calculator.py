class Calculator:
    """简单的计算器类，用于演示"""
    
    def add(self, a: float, b: float) -> float:
        """返回两个数的和"""
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        """返回两个数的差"""
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        """返回两个数的积"""
        return a * b
    
    def divide(self, a: float, b: float) -> float:
        """返回两个数的商"""
        if b == 0:
            raise ValueError("除数不能为零")
        return a / b