import tkinter as tk
from tkinter import messagebox
from controllers.auth_controller import AuthController

class LoginUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Đăng nhập")
        self.root.geometry("300x200")
        
        self.auth = AuthController()
        
        tk.Label(root, text="Tên đăng nhập:").pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()
        
        tk.Label(root, text="Mật khẩu:").pack()
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()
        
        self.login_button = tk.Button(root, text="Đăng nhập", command=self.login)
        self.login_button.pack()
        
        self.register_button = tk.Button(root, text="Đăng ký", command=self.register)
        self.register_button.pack()
    
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        result = self.auth.login(username, password)
        messagebox.showinfo("Thông báo", result)
    
    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        result = self.auth.register(username, password)
        messagebox.showinfo("Thông báo", result)

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginUI(root)
    root.mainloop()
