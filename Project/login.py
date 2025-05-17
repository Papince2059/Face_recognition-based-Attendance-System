# from tkinter import *
# from tkinter import ttk
# from PIL import Image, ImageTk
# from tkinter import messagebox
# import mysql.connector
# import cv2
# import os
# from main import Face_recognition_System

# # def open_main():
# #     os.system("python main.py")  # This runs main.py as a separate process
# class Login:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("Face Recognition Based Standard Attendance System")

#         # Variables to store username and password
#         self.username = StringVar()
#         self.password = StringVar()

#         # Background Image
#         self.bg = ImageTk.PhotoImage(file="images/back.jpg")
#         self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

#         # Login Frame
#         Frame_login = Frame(self.root, bg="white")
#         Frame_login.place(x=265, y=100, height=500, width=755)

#         # Title & Subtitle
#         title = Label(Frame_login, text="Login Here", font=("Impact", 35, "bold"), fg="#d77337", bg="white").place(x=250, y=50)
#         desc = Label(Frame_login, text="Attendance System", font=("Goudy old style", 15, "bold"), fg="#d25d17", bg="white").place(x=250, y=150)

#         # Username
#         lbl_username = Label(Frame_login, text="Username", font=("Goudy old style", 15, "bold"), fg="gray", bg="white").place(x=250, y=220)
#         self.txt_username = Entry(Frame_login, font=("times new roman", 15), bg="lightgray", textvariable=self.username)
#         self.txt_username.place(x=250, y=250, width=250)

#         # Password
#         lbl_password = Label(Frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="gray", bg="white").place(x=250, y=300)
#         self.txt_password = Entry(Frame_login, font=("times new roman", 15), bg="lightgray", show="*", textvariable=self.password)
#         self.txt_password.place(x=250, y=330, width=250)

#         # Login Button
#         login_btn = Button(Frame_login, text="Login", cursor="hand2", command=self.login, fg="white", bg="#d77337", font=("times new roman", 20)).place(x=250, y=380)

#     def login(self):
#             # Perform login functionality here
#         email = self.username.get()
#         password = self.password.get()

#         try:
#             con = mysql.connector.connect(host="localhost", username="root", password="Papince$200000", database="face_recognizer")
#             my_cursor = con.cursor()
#             my_cursor.execute("SELECT * FROM admin WHERE email = %s AND password = %s", (email, password))
#             row = my_cursor.fetchone()
#             if row is not None:
#                 messagebox.showinfo("Login", f"Welcome, {email}!")
#                 # Open the main window after successful login
#                 self.open_main_window()
#             else:
#                 messagebox.showerror("Login Failed", "Invalid username or password")

#         except Exception as e:
#             messagebox.showerror("Error", f"Error: {str(e)}")

#     def open_main_window(self):
#         # Close the current login window
#         self.new_window = Toplevel(self.root)
#         self.app = Face_Recognition_Attendance_System(self.new_window)

# if __name__ == "__main__": 
#     root = Tk()
#     obj = Login(root)
#     root.mainloop()

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import os

def open_main():
    os.system("python main.py")  # Runs main.py as a separate process

class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Based Standard Attendance System")

        # Variables to store username and password
        self.username = StringVar()
        self.password = StringVar()

        # Background Image
        self.bg = ImageTk.PhotoImage(file="images/back.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # Login Frame
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=265, y=100, height=500, width=755)

        # Title & Subtitle
        title = Label(Frame_login, text="Login Here", font=("Impact", 35, "bold"), fg="#d77337", bg="white").place(x=250, y=50)
        desc = Label(Frame_login, text="Attendance System", font=("Goudy old style", 15, "bold"), fg="#d25d17", bg="white").place(x=250, y=150)

        # Username
        lbl_username = Label(Frame_login, text="Username", font=("Goudy old style", 15, "bold"), fg="gray", bg="white").place(x=250, y=220)
        self.txt_username = Entry(Frame_login, font=("times new roman", 15), bg="lightgray", textvariable=self.username)
        self.txt_username.place(x=250, y=250, width=250)

        # Password
        lbl_password = Label(Frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="gray", bg="white").place(x=250, y=300)
        self.txt_password = Entry(Frame_login, font=("times new roman", 15), bg="lightgray", show="*", textvariable=self.password)
        self.txt_password.place(x=250, y=330, width=250)

        # # Login Button
        # login_btn = Button(Frame_login, text="Login", cursor="hand2", command=self.login, fg="white", bg="#d77337", font=("times new roman", 20)).place(x=250, y=380)

        # # Register Button
        # register_btn = Button(Frame_login, text="Register", cursor="hand2", command=self.register, fg="white", bg="blue", font=("times new roman", 15)).place(x=250, y=430)
        # Login and Register Buttons
        login_btn = Button(Frame_login, text="Login", cursor="hand2", command=self.login, 
                        fg="white", bg="#d77337", font=("times new roman", 20))
        login_btn.place(x=180, y=380, width=150, height=40)  # Adjusted position

        register_btn = Button(Frame_login, text="Register", cursor="hand2", command=self.register, 
                            fg="white", bg="blue", font=("times new roman", 15))
        register_btn.place(x=350, y=380, width=150, height=40)  # Placed beside Login

    def login(self):
        email = self.username.get()
        password = self.password.get()

        try:
            con = mysql.connector.connect(host="localhost", username="root", password="Papince$200000", database="face_recognizer")
            my_cursor = con.cursor()
            my_cursor.execute("SELECT * FROM admin WHERE email = %s AND password = %s", (email, password))
            row = my_cursor.fetchone()
            con.close()
            if row is not None:
                messagebox.showinfo("Login", f"Welcome, {email}!")
                self.open_main_window()
            else:
                messagebox.showerror("Login Failed", "Invalid username or password")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")

    def register(self):
        self.reg_window = Toplevel(self.root)
        self.reg_window.title("Register")
        self.reg_window.geometry("400x350")

        Label(self.reg_window, text="Register", font=("Impact", 25, "bold"), fg="green").pack(pady=10)

        # Registration Fields
        Label(self.reg_window, text="Username:", font=("times new roman", 15)).pack(pady=5)
        self.reg_username = Entry(self.reg_window, font=("times new roman", 15))
        self.reg_username.pack(pady=5)

        Label(self.reg_window, text="Password:", font=("times new roman", 15)).pack(pady=5)
        self.reg_password = Entry(self.reg_window, font=("times new roman", 15), show="*")
        self.reg_password.pack(pady=5)

        # Register Button
        Button(self.reg_window, text="Register", font=("times new roman", 15), bg="blue", fg="white", command=self.save_user).pack(pady=20)

    def save_user(self):
        new_user = self.reg_username.get()
        new_pass = self.reg_password.get()

        if new_user == "" or new_pass == "":
            messagebox.showerror("Error", "All fields are required", parent=self.reg_window)
            return

        try:
            con = mysql.connector.connect(host="localhost", username="root", password="Papince$200000", database="face_recognizer")
            my_cursor = con.cursor()
            my_cursor.execute("INSERT INTO admin (email, password) VALUES (%s, %s)", (new_user, new_pass))
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Registration Successful!", parent=self.reg_window)
            self.reg_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}", parent=self.reg_window)

    def open_main_window(self):
        self.root.destroy()  # Close the login window
        open_main()  # Open the main application

if __name__ == "__main__": 
    root = Tk()
    obj = Login(root)
    root.mainloop()
