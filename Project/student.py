from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Based Standard Attendance System")

        #variables
        self.var_dep = StringVar();
        self.var_course = StringVar();
        self.var_year = StringVar();
        self.var_semester = StringVar();
        self.var_std_id = StringVar();
        self.var_std_name = StringVar();
        self.var_section = StringVar();
        self.var_roll = StringVar();
        self.var_gender = StringVar();
        self.var_dob = StringVar();
        self.var_email = StringVar();
        self.var_phone = StringVar();
        self.var_address = StringVar();
        self.var_teacher = StringVar();

        img = Image.open(r"Images\student1.jpeg")
        img = img.resize((500, 150))
        self.photoimage = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimage)
        f_lbl.place(x=0, y=0, width=445, height=120)

        img2 = Image.open(r"Images\student2.jpeg")
        img2 = img2.resize((500, 150))
        self.photoimage2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimage2)
        f_lbl.place(x=440, y=0, width=450, height=120)

        img3 = Image.open(r"Images\student3.jpeg")
        img3 = img3.resize((500, 150))
        self.photoimage3 = ImageTk.PhotoImage(img3)
        f_lbl = Label(self.root, image=self.photoimage3)
        f_lbl.place(x=885, y=0, width=440, height=120)

        #background
        img4 = Image.open(r"Images\back.jpg")
        img4 = img4.resize((1500, 800))
        self.photoimage4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root, image=self.photoimage4)
        bg_img.place(x=0, y=130, width=1300, height=700)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 25, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1300, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=3, y=52, width=1267, height=505)

        #left frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text = "Student Details", font=("times new roman", 14, "bold"))
        left_frame.place(x=5, y=3, width=640, height=487)

        img_left = Image.open(r"C:\Users\Papince Gupta\OneDrive\Desktop\semester 6\AI\Project\Images\student.jpeg")
        img_left = img_left.resize((615, 100))
        self.photoimage_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame, image=self.photoimage_left)
        f_lbl.place(x=5, y=0, width=615, height=100)

        #current courses
        course_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text = "Current Courses", font=("times new roman", 14, "bold"))
        course_frame.place(x=5, y=100, width=620, height=100)

        #department
        dep_label = Label(course_frame, text="Department", font=("times new roman", 13, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(course_frame, textvariable = self.var_dep, font=("times new roman", 13), width=15, state="readonly")
        dep_combo["values"]=("Select Department", "CSE", "IT", "Civil", "Mechanical", "ECE", "EEE")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=7, sticky=W)

        #course
        course_label = Label(course_frame, text="Courses", font=("times new roman", 13, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(course_frame, textvariable = self.var_course, font=("times new roman", 13), width=15, state="readonly")
        course_combo["values"]=("Select Course", "DSA", "DE", "ISCP", "ISES", "ECE", "EEE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=7, sticky=W)

        #Year
        year_label = Label(course_frame, text="Year", font=("times new roman", 13, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(course_frame, textvariable = self.var_year, font=("times new roman", 13), width=15, state="readonly")
        year_combo["values"]=("Select Year", "1st", "2nd", "3rd", "4th")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=7, sticky=W)

        #semester
        semester_label = Label(course_frame, text="Semester", font=("times new roman", 13, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W), 

        semester_combo = ttk.Combobox(course_frame, textvariable = self.var_semester, font=("times new roman", 13), width=15, state="readonly")
        semester_combo["values"]=("Select Semester", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=7, sticky=W)

        #Class Student Information
        class_student_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text = "Class Student Information", font=("times new roman", 14, "bold"))
        class_student_frame.place(x=5, y=206, width=620, height=249)

        #student's ID
        studentId_label = Label(class_student_frame, text="Student ID", font=("times new roman", 13), bg="white")
        studentId_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        studentId_entry = ttk.Entry(class_student_frame, textvariable = self.var_std_id, width=15, font=("times new roman", 13))
        studentId_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        #student's name
        studentName_label = Label(class_student_frame, text="Student Name", font=("times new roman", 13), bg="white")
        studentName_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        studentName_entry = ttk.Entry(class_student_frame, textvariable = self.var_std_name, width=15, font=("times new roman", 13))
        studentName_entry.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        #section
        section_label = Label(class_student_frame, text="Section", font=("times new roman", 13), bg="white")
        section_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        section_combo = ttk.Combobox(class_student_frame, textvariable = self.var_section, font=("times new roman", 13), width=13, state="readonly")
        section_combo["values"]=("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
        section_combo.current(0)
        section_combo.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        #roll no.
        roll_no_label = Label(class_student_frame, text="Roll No.", font=("times new roman", 13), bg="white")
        roll_no_label.grid(row=1, column=2, padx=5, pady=5, sticky=W)

        roll_no_entry = ttk.Entry(class_student_frame, textvariable = self.var_roll, width=15, font=("times new roman", 13))
        roll_no_entry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        #gender
        gender_label = Label(class_student_frame, text="Gender", font=("times new roman", 13), bg="white")
        gender_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_student_frame, textvariable = self.var_gender, font=("times new roman", 13), width=13, state="readonly")
        gender_combo["values"]=("Select Gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        #address
        address_label = Label(class_student_frame, text="Address", font=("times new roman", 13), bg="white")
        address_label.grid(row=2, column=2, padx=5, pady=5, sticky=W)

        address_entry = ttk.Entry(class_student_frame, textvariable = self.var_address, width=15, font=("times new roman", 13))
        address_entry.grid(row=2, column=3, padx=5, pady=5, sticky=W)

        #phone number
        phone_label = Label(class_student_frame, text="Phone No.", font=("times new roman", 13), bg="white")
        phone_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_student_frame, textvariable = self.var_phone, width=15, font=("times new roman", 13))
        phone_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        #DOB
        dob_label = Label(class_student_frame, text="DOB", font=("times new roman", 13), bg="white")
        dob_label.grid(row=3, column=2, padx=5, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_student_frame, textvariable = self.var_dob, width=15, font=("times new roman", 13))
        dob_entry.grid(row=3, column=3, padx=5, pady=5, sticky=W)


        #radio buttons
        self.var_radio1 = StringVar()
        radio1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="Take a photo sample", value="Yes")
        radio1.grid(row=4, column=0)

        radio2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="No photo sample", value="No")
        radio2.grid(row=4, column=1)

        #buttons frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=162, width=615, height=30)

        save_btn = Button(btn_frame, text="Save", command=self.add_data, bg="blue", width=17, font=("times new roman", 12), fg="white")
        save_btn.grid(row=0, column=0)
        
        update_btn = Button(btn_frame, text="Update", command=self.update_data, bg="green", width=16, font=("times new roman", 12), fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, bg="red", width=16, font=("times new roman", 12), fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, bg="orange", width=17, font=("times new roman", 12), fg="white")
        reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=192, width=615, height=30)

        take_photo_btn = Button(btn_frame1, command=self.generate_dataset, text="Take photo sample", bg="brown", width=33, font=("times new roman", 12), fg="white")
        take_photo_btn.grid(row=0, column=0)

        update_photo_btn = Button(btn_frame1, command=self.update_dataset, text="Update photo sample", bg="purple", width=33, font=("times new roman", 12), fg="white")
        update_photo_btn.grid(row=0, column=1)

        #right frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text = "Student Details", font=("times new roman", 14, "bold"))
        right_frame.place(x=650, y=3, width=600, height=487)

        img_right = Image.open(r"images\student1.jpeg")
        img_right = img_right.resize((600, 100))
        self.photoimage_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(right_frame, image=self.photoimage_right)
        f_lbl.place(x=3, y=0, width=600, height=100)

        #search system
        search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE, text = "Search system", font=("times new roman", 15, "bold"))
        search_frame.place(x=3, y=105, width=590, height=75)

        search_label = Label(search_frame, text="Search By:", font=("times new roman", 13, "bold"), bg="white", fg="red")
        search_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 13), width=12, state="readonly")
        search_combo["values"]=("Select", "Roll No", "Phone No.", "Name")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=5, sticky=W)

        search_entry = ttk.Entry(search_frame, width=12, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=4, pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search", bg="red", width=11, font=("times new roman", 12), fg="white")
        search_btn.grid(row=0, column=3, padx=3)

        show_all_btn = Button(search_frame, text="Show All", bg="orange", width=11, font=("times new roman", 12), fg="white")
        show_all_btn.grid(row=0, column=4, padx=3)

        #table
        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=3, y=185, width=590, height=275)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(
            table_frame, columns=('id', 'cour', 'year', 'sem', 'dep', 'name', 'section', 'roll', 'gender', 'address', 'phone', 'dob', 'photo'),
              xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X) 
        scroll_y.pack(side=RIGHT, fill=Y) 
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("id", text="Student_ID")
        self.student_table.heading("cour", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("section", text="Section")
        self.student_table.heading("roll", text="RollNo.")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("photo", text="Photo")
        self.student_table["show"] = "headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("cour",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("section",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        # self.student_table.bind("<ButtonRelease>", self.get_cursor)
        # self.fetch_data()

    #add data to database
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
             messagebox.showerror("Error","All fields are required", parent=self.root)
        else:
            try:
                con = mysql.connector.connect(host="localhost", username="root", password="Papince$200000", database="face_recognizer")
                my_cursor = con.cursor()
                my_cursor.execute("insert into students values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                (
                                    self.var_std_id.get(),
                                    self.var_course.get(),
                                    self.var_year.get(),
                                    self.var_semester.get(),
                                    self.var_dep.get(),
                                    self.var_std_name.get(),
                                    self.var_section.get(),
                                    self.var_roll.get(),
                                    self.var_gender.get(),
                                    self.var_address.get(),
                                    self.var_phone.get(),
                                    self.var_dob.get(),
                                    self.var_radio1.get()
                                ) )
                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo("Success", "Student details have been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    #fetch data from database
    def fetch_data(self):
        con = mysql.connector.connect(host="localhost", username="root", password="Papince$200000", database="face_recognizer")
        my_cursor = con.cursor()
        my_cursor.execute("SELECT * FROM students")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            con.commit()
        con.close()
    
    #get cursor
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        if data:
            self.var_std_id.set(data[0]),
            self.var_course.set(data[1]),
            self.var_year.set(data[2]),
            self.var_semester.set(data[3]),
            self.var_dep.set(data[4]),
            self.var_std_name.set(data[5]),
            self.var_section.set(data[6]),
            self.var_roll.set(data[7]),
            self.var_gender.set(data[8]),
            self.var_address.set(data[9]),
            self.var_phone.set(data[10]),
            self.var_dob.set(data[11]),
            self.var_radio1.set(data[12])

    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this student details", parent = self.root)
                if Update > 0:
                    con = mysql.connector.connect(host="localhost", username="root", password="Papince$200000", database="face_recognizer")
                    my_cursor = con.cursor()
                    original_student_id = self.var_std_id.get()
                    my_cursor.execute("update students set Student_ID=%s, Course=%s, Year=%s, Semester=%s,  Department=%s, Name=%s, Section=%s, `RollNo.`=%s, Gender=%s, Address=%s, Phone=%s, DOB=%s, Photo=%s where Student_ID=%s",
                                    (   
                                        self.var_std_id.get(),
                                        self.var_course.get(),
                                        self.var_year.get(),
                                        self.var_semester.get(),
                                        self.var_dep.get(),
                                        self.var_std_name.get(),
                                        self.var_section.get(),
                                        self.var_roll.get(),
                                        self.var_gender.get(),
                                        self.var_address.get(),
                                        self.var_phone.get(),
                                        self.var_dob.get(),
                                        self.var_radio1.get(),
                                        original_student_id
                                    ))
                    messagebox.showinfo("Success", "Student details successfully updated", parent = self.root)
                    con.commit()
                    self.fetch_data()
                    con.close()
                else:
                    if not Update:
                        return
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)
                
    # delete funtion
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student delete page", "Do you want to delete this student?", parent=self.root)
                if delete > 0:
                    con = mysql.connector.connect(host="localhost", username="root", password="Papince$200000", database="face_recognizer")
                    my_cursor = con.cursor()
                    s = "delete from students where Student_ID=%s"
                    val = (self.var_std_id. get(), )
                    my_cursor.execute(s, val)                
                else:
                    if not delete:
                        return
                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo("Delete", "Successfully deleted student details", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)
    
    #reset function
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_section.set("Select Section"),
        self.var_roll.set(""),
        self.var_gender.set("Select Gender"),
        self.var_address.set(""),
        self.var_phone.set(""),
        self.var_dob.set(""),
        self.var_radio1.set("")
    
    # Take photo
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                # Connect to the database
                con = mysql.connector.connect(host="localhost", username="root", password="Papince$200000", database="face_recognizer")
                my_cursor = con.cursor()

                # Fetch existing data from the students table
                my_cursor.execute("select * from students where Student_ID=%s", (self.var_std_id.get(),))
                student = my_cursor.fetchone()

                if student:

                    # Face detection and saving the photos
                    face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                    # Function to detect and crop faces
                    def face_cropped(img):
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                        if len(faces) == 0:
                            return None
                        for (x, y, w, h) in faces:
                            face_crop = img[y:y+h, x:x+w]
                            return face_crop

                    # Ensure Student_ID is retrieved correctly
                    student_id = self.var_std_id.get()
                    if not student_id:
                        messagebox.showerror("Error", "Student ID is missing or invalid.", parent=self.root)
                        return

                    # Access the webcam
                    cap = cv2.VideoCapture(0)
                    img_id = 0

                    while True:
                        ret, myFrame = cap.read()
                        if face_cropped(myFrame) is not None:
                            img_id += 1
                            face = cv2.resize(face_cropped(myFrame), (450, 450))
                            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                            # Ensure the student_id is properly inserted in the file name
                            file_name_path = f"data/user.{student_id}.{img_id}.jpg"
                            cv2.imwrite(file_name_path, face)

                            # Display the captured image with the image ID on it
                            cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 255), 2)
                            cv2.imshow("Cropped Face", face)

                        if cv2.waitKey(1) == 13 or img_id == 100:  # Press 'Enter' to exit or capture 100 images
                            break

                    cap.release()
                    cv2.destroyAllWindows()

                    messagebox.showinfo("Result", "Generating data sets completed!")
                else:
                    messagebox.showerror("Error", "Student ID not found in the database", parent=self.root)
                    
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


    #update photo
    def update_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                # Connect to the database
                con = mysql.connector.connect(host="localhost", username="root", password="Papince$200000", database="face_recognizer")
                my_cursor = con.cursor()

                # Check if the student exists in the database
                my_cursor.execute("select * from students where Student_ID=%s", (self.var_std_id.get(),))
                student = my_cursor.fetchone()

                if student:
                    # Update student photo dataset
                    face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                    # Function to detect and crop the face
                    def face_cropped(img):
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                        for (x, y, w, h) in faces:
                            face_crop = img[y:y+h, x:x+w]
                            return face_crop

                    # Start webcam
                    cap = cv2.VideoCapture(0)
                    img_id = 0
                    while True:
                        ret, myFrame = cap.read()
                        if face_cropped(myFrame) is not None:
                            img_id += 1
                            face = cv2.resize(face_cropped(myFrame), (450, 450))
                            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                            # Save the updated face image with the same student ID
                            file_name_path = f"data/user.{self.var_std_id.get()}.{img_id}.jpg"
                            cv2.imwrite(file_name_path, face)
                            cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 255), 2)
                            cv2.imshow("Updated Cropped Face", face)

                        if cv2.waitKey(1) == 13 or img_id == 100:
                            break

                    cap.release()
                    cv2.destroyAllWindows()

                    messagebox.showinfo("Result", "Updating photo samples completed!")
                else:
                    messagebox.showerror("Error", "Student not found in the database.", parent=self.root)

                con.commit()
                con.close()

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

if __name__ == "__main__": 
    root = Tk()
    obj = Student(root)
    root.mainloop()