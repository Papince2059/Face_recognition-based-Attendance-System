# from tkinter import *
# from tkinter import ttk
# from PIL import Image, ImageTk
# from tkinter import messagebox
# import mysql.connector
# import cv2
# import os
# import csv
# from tkinter import filedialog

# myData = []
# csv_file_path = ""

# class Attendance:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("Face Recognition Based Standard Attendance System")

#         self.var_attend_id = StringVar();
#         self.var_attendance = StringVar();
#         self.var_name = StringVar();
#         self.var_dep = StringVar();
#         self.var_roll = StringVar();
#         self.var_date = StringVar();
#         self.var_time = StringVar();


#         img = Image.open(r"images\coaching.jpg")
#         img = img.resize((450, 200))
#         self.photoimage = ImageTk.PhotoImage(img)
#         f_lbl = Label(self.root, image=self.photoimage)
#         f_lbl.place(x=0, y=0, width=470, height=200)

#         img2 = Image.open(r"images\classroom.jpg")
#         img2 = img2.resize((450, 200))
#         self.photoimage2 = ImageTk.PhotoImage(img2)
#         f_lbl = Label(self.root, image=self.photoimage2)
#         f_lbl.place(x=450, y=0, width=470, height=200)
        
#         img3 = Image.open(r"images\class.jpeg")
#         img3 = img3.resize((450, 200))
#         self.photoimage3 = ImageTk.PhotoImage(img3)
#         f_lbl = Label(self.root, image=self.photoimage3)
#         f_lbl.place(x=900, y=0, width=470, height=200)
        
#         # background
#         img4 = Image.open(r"images\Background.jpeg")
#         img4 = img4.resize((1350, 500))
#         self.photoimage4 = ImageTk.PhotoImage(img4)
#         bg_img = Label(self.root, image=self.photoimage4)
#         bg_img.place(x=0, y=200, width=1300, height=550)

#         title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 25, "bold"), bg="white", fg="darkgreen")
#         title_lbl.place(x=0, y=0, width=1300, height=45)

#         main_frame = Frame(bg_img, bd=2, bg="white")
#         main_frame.place(x=5, y=50, width=1268, height=450)

#         #left frame
#         left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text = "Student Attendance Details", font=("times new roman", 14, "bold"))
#         left_frame.place(x=5, y=3, width=630, height=435)

#         img_left = Image.open(r"images\student.jpeg")
#         img_left = img_left.resize((300, 100))
#         self.photoimage_left = ImageTk.PhotoImage(img_left)

#         f_lbl = Label(left_frame, image=self.photoimage_left)
#         f_lbl.place(x=5, y=0, width=300, height=100)

#         left_inside_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
#         left_inside_frame.place(x=5, y=105, width=615, height=300)

#         #label and entry

#         #attendance's ID
#         attendanceId_label = Label(left_inside_frame, text="Attendance ID:", font=("times new roman", 13), bg="white")
#         attendanceId_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

#         attendanceId_entry = ttk.Entry(left_inside_frame, width=15, textvariable=self.var_attend_id, font=("times new roman", 13))
#         attendanceId_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

#         roll_label = Label(left_inside_frame, text="Roll No:", font=("times new roman", 13), bg="white")
#         roll_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

#         roll_entry = ttk.Entry(left_inside_frame, width=15, textvariable=self.var_roll, font=("times new roman", 13))
#         roll_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

#         #student's name
#         Name_label = Label(left_inside_frame, text="Student Name:", font=("times new roman", 13), bg="white")
#         Name_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)

#         Name_entry = ttk.Entry(left_inside_frame, width=15, textvariable=self.var_name, font=("times new roman", 13))
#         Name_entry.grid(row=0, column=3, padx=5, pady=5, sticky=W)

#         dep_label = Label(left_inside_frame, text="Department:", font=("times new roman", 13), bg="white")
#         dep_label.grid(row=1, column=2, padx=5, pady=5, sticky=W)

#         dep_entry = ttk.Entry(left_inside_frame, width=15, textvariable=self.var_dep, font=("times new roman", 13))
#         dep_entry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

#         time_label = Label(left_inside_frame, text="Time:", font=("times new roman", 13), bg="white")
#         time_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)

#         time_entry = ttk.Entry(left_inside_frame, width=15, textvariable=self.var_time, font=("times new roman", 13))
#         time_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)
        
#         date_label = Label(left_inside_frame, text="Date:", font=("times new roman", 13), bg="white")
#         date_label.grid(row=2, column=2, padx=5, pady=5, sticky=W)

#         date_entry = ttk.Entry(left_inside_frame, width=15, textvariable=self.var_date, font=("times new roman", 13))
#         date_entry.grid(row=2, column=3, padx=5, pady=5, sticky=W)

#         attendance_label = Label(left_inside_frame, text="Attendance Status", font=("times new roman", 13), bg="white")
#         attendance_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)

#         self.atten_status = ttk.Combobox(left_inside_frame, textvariable=self.var_attendance, font=("times new roman", 13), width=15, state="readonly")
#         self.atten_status["values"]=("Status", "Present", "Absent")
#         self.atten_status.current(0)
#         self.atten_status.grid(row=3, column=1, pady=7, sticky=W)

#         #buttons frame
#         btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
#         btn_frame.place(x=0, y=162, width=615, height=30)

#         save_btn = Button(btn_frame, text="Import CSV", command=self.importCSV, bg="blue", width=12, font=("times new roman", 12), fg="white")
#         save_btn.grid(row=0, column=0)
        
#         export_btn = Button(btn_frame, text="Export CSV", command=self.exportCSV, bg="green", width=12, font=("times new roman", 12), fg="white")
#         export_btn.grid(row=0, column=1)

#         delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, bg="red", width=12, font=("times new roman", 12), fg="white")
#         delete_btn.grid(row=0, column=2)

#         reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, bg="orange", width=12, font=("times new roman", 12), fg="white")
#         reset_btn.grid(row=0, column=3)

#         reset_btn = Button(btn_frame, text="Save & Back", command=self.Save_back, bg="orange", width=12, font=("times new roman", 12), fg="white")
#         reset_btn.grid(row=0, column=4)


#         #right frame
#         right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text = "Student Details", font=("times new roman", 14, "bold"))
#         right_frame.place(x=640, y=3, width=620, height=435)

#         table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
#         table_frame.place(x=5, y=5, width=604, height=375)

#         scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
#         scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

#         self.AttendanceReportTable = ttk.Treeview(table_frame, column=('id', 'roll', 'name', 'dep', 'time', 'date', 'attendance'),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
#         scroll_x.pack(side=BOTTOM, fill=X) 
#         scroll_y.pack(side=RIGHT, fill=Y) 

#         scroll_x.config(command=self.AttendanceReportTable.xview)
#         scroll_y.config(command=self.AttendanceReportTable.yview)

#         self.AttendanceReportTable.heading("id", text="Attendance ID")
#         self.AttendanceReportTable.heading("roll", text="Roll")
#         self.AttendanceReportTable.heading("name", text="Name")
#         self.AttendanceReportTable.heading("dep", text="Department")
#         self.AttendanceReportTable.heading("time", text="Time")
#         self.AttendanceReportTable.heading("date", text="Date")
#         self.AttendanceReportTable.heading("attendance", text="Attendance")

#         self.AttendanceReportTable["show"] = "headings"
         
#         self.AttendanceReportTable.column("id",width=100)
#         self.AttendanceReportTable.column("roll",width=100)
#         self.AttendanceReportTable.column("name",width=100)
#         self.AttendanceReportTable.column("dep",width=100)
#         self.AttendanceReportTable.column("time",width=100)
#         self.AttendanceReportTable.column("date",width=100)
#         self.AttendanceReportTable.column("attendance",width=100)

#         self.AttendanceReportTable.pack(fill=BOTH, expand=1)

#         self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

#     #fetch data functions
#     def fetchData(self, rows):
#         self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
#         for i in rows:
#             self.AttendanceReportTable.insert("",END,values=i)

#     def importCSV(self):
#         global myData, csv_file_path
#         myData.clear()
#         csv_file_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
#         if csv_file_path:
#             with open(csv_file_path) as file:
#                 csvread = csv.reader(file, delimiter=",")
#                 for i in csvread:
#                     myData.append(i)
#                 self.fetchData(myData)

#     def exportCSV(self):
#         try:
#             global csv_file_path 

#             if len(myData) < 1:
#                 messagebox.showerror("No Data", "No data found to export", parent=self.root)
#                 return False
            
#             overwrite = messagebox.askyesno("Export CSV", "Do you want to overwrite the imported CSV file?")

#             if overwrite and csv_file_path:
#                 fln = csv_file_path
#             else:
#                 fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
#                 if not fln:
#                     return
                
#             with open(fln, mode="w", newline="") as myfile:
#                 exp_write = csv.writer(myfile, delimiter=",")
#                 for i in myData:
#                     exp_write.writerow(i)

#             messagebox.showinfo("Data exported", f"Your data was exported to {os.path.basename(fln)} successfully")

#         except Exception as es:
#             messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


#     def get_cursor(self, event=""):
#         cursor_row = self.AttendanceReportTable.focus()
#         content = self.AttendanceReportTable.item(cursor_row)
#         rows = content["values"]
#         self.var_attend_id.set(rows[0])
#         self.var_roll.set(rows[1])
#         self.var_name.set(rows[2])
#         self.var_dep.set(rows[3])
#         self.var_time.set(rows[4])
#         self.var_date.set(rows[5])
#         self.var_attendance.set(rows[6])

#     def reset_data(self):
#         self.var_attend_id.set("")
#         self.var_roll.set("")
#         self.var_name.set("")
#         self.var_dep.set("")
#         self.var_time.set("")
#         self.var_date.set("")
#         self.var_attendance.set("")
    
#     def Save_back(self):
#         try:
#             # Call your function to save attendance data to the database
#             self.save_attendance_to_db()

#             # Destroy the current window
#             self.root.destroy()

#             # Go back to main.py
#             os.system("python main.py")
#         except Exception as e:
#             messagebox.showerror("Error", f"Failed to save data: {str(e)}")

    
#     def delete_data(self):
#         try:
#             if self.var_attend_id.get() == "":
#                 messagebox.showerror("Error", "Please select a record to delete", parent=self.root)
#                 return

#             delete_id = self.var_attend_id.get()

#             global csv_file_path
#             if not csv_file_path:
#                 messagebox.showerror("Error", "No CSV file loaded.", parent=self.root)
#                 return

#             updated_data = []
#             with open(csv_file_path, mode="r") as file:
#                 csvreader = csv.reader(file, delimiter=",")
#                 for row in csvreader:
#                     if row[0] != delete_id:
#                         updated_data.append(row)

#             with open(csv_file_path, mode="w", newline="") as file:
#                 csvwriter = csv.writer(file, delimiter=",")
#                 csvwriter.writerows(updated_data)

#             messagebox.showinfo("Success", f"Attendance ID {delete_id} deleted successfully", parent=self.root)

#             self.fetchData(updated_data)
#             self.reset_data()

#         except Exception as es:
#             messagebox.showerror("Error", f"Error deleting record: {str(es)}", parent=self.root)
    

# if __name__ == "__main__": 
#     root = Tk()
#     obj = Attendance(root)
#     root.mainloop()

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

myData = []
csv_file_path = ""

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Based Standard Attendance System")

        self.var_attend_id = StringVar();
        self.var_attendance = StringVar();
        self.var_name = StringVar();
        self.var_dep = StringVar();
        self.var_roll = StringVar();
        self.var_date = StringVar();
        self.var_time = StringVar();


        img = Image.open(r"images\coaching.jpg")
        img = img.resize((450, 200))
        self.photoimage = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimage)
        f_lbl.place(x=0, y=0, width=470, height=200)

        img2 = Image.open(r"images\classroom.jpg")
        img2 = img2.resize((450, 200))
        self.photoimage2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimage2)
        f_lbl.place(x=450, y=0, width=470, height=200)
        
        img3 = Image.open(r"images\class.jpeg")
        img3 = img3.resize((450, 200))
        self.photoimage3 = ImageTk.PhotoImage(img3)
        f_lbl = Label(self.root, image=self.photoimage3)
        f_lbl.place(x=900, y=0, width=470, height=200)
        
        # background
        img4 = Image.open(r"images\Background.jpeg")
        img4 = img4.resize((1350, 500))
        self.photoimage4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root, image=self.photoimage4)
        bg_img.place(x=0, y=200, width=1300, height=550)

        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 25, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1300, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=5, y=50, width=1268, height=450)

        #left frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text = "Student Attendance Details", font=("times new roman", 14, "bold"))
        left_frame.place(x=5, y=3, width=630, height=435)

        img_left = Image.open(r"images\student.jpeg")
        img_left = img_left.resize((300, 100))
        self.photoimage_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame, image=self.photoimage_left)
        f_lbl.place(x=5, y=0, width=300, height=100)

        left_inside_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=5, y=105, width=615, height=300)

        #label and entry

        #attendance's ID
        attendanceId_label = Label(left_inside_frame, text="Attendance ID:", font=("times new roman", 13), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        attendanceId_entry = ttk.Entry(left_inside_frame, width=15, textvariable=self.var_attend_id, font=("times new roman", 13))
        attendanceId_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        roll_label = Label(left_inside_frame, text="Roll No:", font=("times new roman", 13), bg="white")
        roll_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        roll_entry = ttk.Entry(left_inside_frame, width=15, textvariable=self.var_roll, font=("times new roman", 13))
        roll_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        #student's name
        Name_label = Label(left_inside_frame, text="Student Name:", font=("times new roman", 13), bg="white")
        Name_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        Name_entry = ttk.Entry(left_inside_frame, width=15, textvariable=self.var_name, font=("times new roman", 13))
        Name_entry.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        dep_label = Label(left_inside_frame, text="Department:", font=("times new roman", 13), bg="white")
        dep_label.grid(row=1, column=2, padx=5, pady=5, sticky=W)

        dep_entry = ttk.Entry(left_inside_frame, width=15, textvariable=self.var_dep, font=("times new roman", 13))
        dep_entry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        time_label = Label(left_inside_frame, text="Time:", font=("times new roman", 13), bg="white")
        time_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)

        time_entry = ttk.Entry(left_inside_frame, width=15, textvariable=self.var_time, font=("times new roman", 13))
        time_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)
        
        date_label = Label(left_inside_frame, text="Date:", font=("times new roman", 13), bg="white")
        date_label.grid(row=2, column=2, padx=5, pady=5, sticky=W)

        date_entry = ttk.Entry(left_inside_frame, width=15, textvariable=self.var_date, font=("times new roman", 13))
        date_entry.grid(row=2, column=3, padx=5, pady=5, sticky=W)

        attendance_label = Label(left_inside_frame, text="Attendance Status", font=("times new roman", 13), bg="white")
        attendance_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)

        self.atten_status = ttk.Combobox(left_inside_frame, textvariable=self.var_attendance, font=("times new roman", 13), width=15, state="readonly")
        self.atten_status["values"]=("Status", "Present", "Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3, column=1, pady=7, sticky=W)

        #buttons frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=162, width=615, height=30)

        import_btn = Button(btn_frame, text="Import CSV", command=self.importCSV, bg="blue", width=10, font=("times new roman", 12), fg="white")
        import_btn.grid(row=0, column=0)
        
        export_btn = Button(btn_frame, text="Export CSV", command=self.exportCSV, bg="green", width=10, font=("times new roman", 12), fg="white")
        export_btn.grid(row=0, column=1)

        update_btn = Button(btn_frame, text="Update", command=self.update_attendance, bg="purple", width=10, font=("times new roman", 12), fg="white")
        update_btn.grid(row=0, column=2)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, bg="red", width=10, font=("times new roman", 12), fg="white")
        delete_btn.grid(row=0, column=3)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, bg="orange", width=10, font=("times new roman", 12), fg="white")
        reset_btn.grid(row=0, column=4)

        save_back_btn = Button(btn_frame, text="Save & Back", command=self.Save_back, bg="orange", width=10, font=("times new roman", 12), fg="white")
        save_back_btn.grid(row=0, column=5)

        #right frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text = "Student Details", font=("times new roman", 14, "bold"))
        right_frame.place(x=640, y=3, width=620, height=435)

        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=5, width=604, height=375)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, column=('id', 'roll', 'name', 'dep', 'time', 'date', 'attendance'),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X) 
        scroll_y.pack(side=RIGHT, fill=Y) 

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("dep", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")

        self.AttendanceReportTable["show"] = "headings"
         
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("dep",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

    #fetch data functions
    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    def importCSV(self):
        global myData, csv_file_path
        myData.clear()
        csv_file_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        if csv_file_path:
            with open(csv_file_path) as file:
                csvread = csv.reader(file, delimiter=",")
                for i in csvread:
                    myData.append(i)
                self.fetchData(myData)

    def exportCSV(self):
        try:
            global csv_file_path 

            if len(myData) < 1:
                messagebox.showerror("No Data", "No data found to export", parent=self.root)
                return False
            
            overwrite = messagebox.askyesno("Export CSV", "Do you want to overwrite the imported CSV file?")

            if overwrite and csv_file_path:
                fln = csv_file_path
            else:
                fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
                if not fln:
                    return
                
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in myData:
                    exp_write.writerow(i)

            messagebox.showinfo("Data exported", f"Your data was exported to {os.path.basename(fln)} successfully")

        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content["values"]
        if rows:
            self.var_attend_id.set(rows[0])
            self.var_roll.set(rows[1])
            self.var_name.set(rows[2])
            self.var_dep.set(rows[3])
            self.var_time.set(rows[4])
            self.var_date.set(rows[5])
            self.var_attendance.set(rows[6])

    def reset_data(self):
        self.var_attend_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendance.set("Status")
    
    def update_attendance(self):
        global myData, csv_file_path
        
        # Check if there's a selected row
        if self.var_attend_id.get() == "":
            messagebox.showerror("Error", "Please select an attendance record to update", parent=self.root)
            return
        
        # Get the updated values
        updated_id = self.var_attend_id.get()
        updated_roll = self.var_roll.get()
        updated_name = self.var_name.get()
        updated_dep = self.var_dep.get()
        updated_time = self.var_time.get()
        updated_date = self.var_date.get()
        updated_attendance = self.var_attendance.get()
        
        # Validate input
        if updated_attendance == "Status":
            messagebox.showerror("Error", "Please select attendance status (Present/Absent)", parent=self.root)
            return
        
        # Update the data in memory
        for i, row in enumerate(myData):
            if row[0] == updated_id:
                myData[i] = [updated_id, updated_roll, updated_name, updated_dep, updated_time, updated_date, updated_attendance]
                break
        
        # Update the treeview
        self.fetchData(myData)
        
        # Update the CSV file if it exists
        if csv_file_path:
            with open(csv_file_path, mode="w", newline="") as file:
                csvwriter = csv.writer(file, delimiter=",")
                csvwriter.writerows(myData)
            
            messagebox.showinfo("Success", "Attendance updated successfully", parent=self.root)

    def delete_data(self):
        try:
            if self.var_attend_id.get() == "":
                messagebox.showerror("Error", "Please select a record to delete", parent=self.root)
                return

            delete_id = self.var_attend_id.get()

            global myData, csv_file_path
            if not csv_file_path:
                messagebox.showerror("Error", "No CSV file loaded.", parent=self.root)
                return

            updated_data = []
            for row in myData:
                if row[0] != delete_id:
                    updated_data.append(row)
            
            myData = updated_data  # Update the global myData

            if csv_file_path:
                with open(csv_file_path, mode="w", newline="") as file:
                    csvwriter = csv.writer(file, delimiter=",")
                    csvwriter.writerows(myData)

            messagebox.showinfo("Success", f"Attendance ID {delete_id} deleted successfully", parent=self.root)

            self.fetchData(myData)
            self.reset_data()

        except Exception as es:
            messagebox.showerror("Error", f"Error deleting record: {str(es)}", parent=self.root)
    
    def save_attendance_to_db(self):
        try:
            # Check if there's any data to save
            if len(myData) < 1:
                messagebox.showerror("No Data", "No attendance data to save", parent=self.root)
                return False
            
            # Connect to MySQL database
            conn = mysql.connector.connect(
                host="localhost",
                user="root",  # Replace with your MySQL username
                password="Papince$200000",  # Replace with your MySQL password
                database="face_recognizer"  # Replace with your database name
            )
            cursor = conn.cursor()
            
            # Create attendance table if it doesn't exist
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS attendance (
                    attendance_id VARCHAR(50) PRIMARY KEY,
                    roll VARCHAR(50),
                    name VARCHAR(100),
                    department VARCHAR(100),
                    course VARCHAR(100),
                    year VARCHAR(50),
                    semester VARCHAR(50),
                    section VARCHAR(50),
                    time VARCHAR(50),
                    date VARCHAR(50),
                    attendance VARCHAR(20)
                )
            """)
            
            # Clear existing data for the current date if specified
            if any(row[5] for row in myData):  # Check if any row has date
                # Get unique dates from the data
                dates = set(row[5] for row in myData if row[5])
                for date in dates:
                    cursor.execute("DELETE FROM attendance WHERE date=%s", (date,))
            
            # For each attendance record, get additional student details from student table
            for row in myData:
                # Check if row has all required fields
                if len(row) < 7:
                    continue
                
                # Get student details from student table
                try:
                    cursor.execute("SELECT course, year, semester, section FROM student WHERE roll=%s", (row[1],))
                    student_details = cursor.fetchone()
                    
                    if student_details:
                        course, year, semester, section = student_details
                    else:
                        # If student not found, use default values
                        course, year, semester, section = "N/A", "N/A", "N/A", "N/A"
                except:
                    # If there's an error or student table doesn't exist yet
                    course, year, semester, section = "N/A", "N/A", "N/A", "N/A"
                
                # Insert or update attendance with additional student details
                cursor.execute("""
                    INSERT INTO attendance (
                        attendance_id, roll, name, department, course, year, 
                        semester, section, time, date, attendance
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE
                        roll=%s, name=%s, department=%s, course=%s, year=%s,
                        semester=%s, section=%s, time=%s, date=%s, attendance=%s
                """, (
                    row[0], row[1], row[2], row[3], course, year, semester, section, row[4], row[5], row[6],
                    row[1], row[2], row[3], course, year, semester, section, row[4], row[5], row[6]
                ))
            
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Attendance data saved successfully to database", parent=self.root)
            return True
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save attendance data: {str(e)}", parent=self.root)
            return False
    
    def Save_back(self):
        try:
            # Call function to save attendance data to the database
            if self.save_attendance_to_db():
                # Destroy the current window
                self.root.destroy()
                
                # Go back to main.py
                os.system("python main.py")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save data: {str(e)}")

if __name__ == "__main__": 
    root = Tk()
    obj = Attendance(root)
    root.mainloop()