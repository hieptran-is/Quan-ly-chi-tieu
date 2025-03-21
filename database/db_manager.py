import sqlite3

class DatabaseManager:
    def __init__(self, db_name="expense_manager.db"):
        self.db_name = db_name
    
    def connect(self):
        return sqlite3.connect(self.db_name)
    
    # Thêm người dùng mới
    def add_user(self, username, password):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
    
    # Lấy thông tin người dùng
    def get_user(self, username):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()
        return user
    
    # Thêm danh mục thu/chi
    def add_category(self, name):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO categories (name) VALUES (?)", (name,))
        conn.commit()
        conn.close()
    
    # Lấy danh sách danh mục
    def get_categories(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM categories")
        categories = cursor.fetchall()
        conn.close()
        return categories
    
    # Thêm giao dịch thu/chi
    def add_transaction(self, user_id, category_id, amount, date):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO transactions (user_id, category_id, amount, date)
            VALUES (?, ?, ?, ?)""",
            (user_id, category_id, amount, date))
        conn.commit()
        conn.close()
    
    # Lấy danh sách giao dịch
    def get_transactions(self, user_id):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM transactions WHERE user_id = ?", (user_id,))
        transactions = cursor.fetchall()
        conn.close()
        return transactions