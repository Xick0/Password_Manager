from datetime import datetime

class Password:
    def __init__(self):
        self.id = self.generate_id()
        self.username = None
        self.password = None

    def generate_id(self) -> int:
        return int(datetime.now().timestamp() * 10)
    
    def set_username(self, new_username: str) -> None:
        self.username = new_username

    def toString(self) -> str:
        return f"Username='{self.username}', Id='{str(self.id)}'"