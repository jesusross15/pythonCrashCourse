class User:
    """---"""

    def __init__(self, first, last):
        """---"""
        self.first = first
        self.last = last
    
    def describe_user(self):
        """---"""
        print(f"{self.first} is wonderful person to be around.")
    
    def greet_user(self):
        """---"""
        print(f"Hello, {self.first} {self.last}. How are you doing today?")
        
    
