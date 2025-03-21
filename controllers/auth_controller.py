# controllers/auth_controller.py
from database.db_manager import DatabaseManager

class AuthController:
    def __init__(self):
        self.db = DatabaseManager()
    
    # Đăng ký tài khoản mới
    def register(self, username, password):
        if self.db.get_user(username):
            return "Tên đăng nhập đã tồn tại!"
        self.db.add_user(username, password)
        return "Đăng ký thành công!"
    
    # Đăng nhập tài khoản
    def login(self, username, password):
        user = self.db.get_user(username)
        if user and user[2] == password:  # user[2] là cột password trong database
            return "Đăng nhập thành công!"
        return "Sai tên đăng nhập hoặc mật khẩu!"