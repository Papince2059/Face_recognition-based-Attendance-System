from tkinter import*
from tkinter import ttk  # stylishtoolkit
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from tkinter import messagebox



class Face_recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  # width x height
        self.root.title("Face Recognition System")
        
        
        # Load and place the first image (ap.jpg)
        img1 = Image.open(r"images\ap.jpg")
        img1 = img1.resize((500, 130))
        self.photoimage1 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.root, image=self.photoimage1)
        f_lbl1.place(x=0, y=0, width=389, height=130)

        # Load and place the second image (facial.jpg)
        img2 = Image.open(r"images\facial.jpg")
        img2 = img2.resize((500, 130))
        self.photoimage2 = ImageTk.PhotoImage(img2)
        f_lbl2 = Label(self.root, image=self.photoimage2)
        f_lbl2.place(x=389, y=0, width=500, height=130)

        # Load and place the third image (system.jpeg)
        img3 = Image.open(r"images\system.jpeg")
        img3 = img3.resize((500, 130))  # Ensure this is 500 wide
        self.photoimage3 = ImageTk.PhotoImage(img3)
        f_lbl3 = Label(self.root, image=self.photoimage3)
        f_lbl3.place(x=389 + 500, y=0, width=500, height=130)  # Adjusted to 500 width

        # Load and place the fourth image (extra.jpeg)
        img4 = Image.open(r"images\extra.jpeg")
        img4 = img4.resize((500, 130))  # Ensure this is 500 wide
        self.photoimage4 = ImageTk.PhotoImage(img4)
        f_lbl4 = Label(self.root, image=self.photoimage4)
        f_lbl4.place(x=389 + 500 + 500, y=0, width=500, height=130)  # Corrected position


        img4 = Image.open( r"images\back.jpg")
        img4 = img4.resize((1530, 710))
        self.photoimage4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root, image=self.photoimage4)
        bg_img.place(x=0, y=130, width=1530, height=768)


        title_lbl = Label(bg_img, text="FACE RECOGNITION BASED STANDARD ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 25, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1550, height=45)

        #student
        img5 = Image.open(r"images\student.jpeg")
        img5 = img5.resize((220, 220))
        self.photoimage5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimage5,command=self.student_details, cursor="hand2")
        b1.place(x=85, y=70, width=220, height=220)

        b1_1 = Button(bg_img, text='Student Details', command=self.student_details, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=85, y=250, width=220, height=40)

        # Face detector
        img6 = Image.open(r"images\access.jpg")
        img6 = img6.resize((220, 220))
        self.photoimage6 = ImageTk.PhotoImage(img6)
        b1 = Button(bg_img, image=self.photoimage6, cursor="hand2", command=self.face_data)
        b1.place(x=370, y=70, width=220, height=220)

        b1_1 = Button(bg_img, text='Face detector', cursor="hand2", command=self.face_data, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=370, y=250, width=220, height=40)

        # Attendance
        img7 = Image.open(r"images\night.jpg")
        img7 = img7.resize((220, 220))
        self.photoimage7 = ImageTk.PhotoImage(img7)
        b1 = Button(bg_img, image=self.photoimage7, cursor="hand2", command=self.attendance_data)
        b1.place(x=650, y=70, width=220, height=220)

        b1_1 = Button(bg_img, text='Attendance', cursor="hand2", command=self.attendance_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=650, y=250, width=220, height=40)

        #Helpdesk
        img8 = Image.open(r"images\helpdesk.jpeg")
        img8 = img8.resize((220, 220))
        self.photoimage8 = ImageTk.PhotoImage(img8)
        b1 = Button(bg_img, image=self.photoimage8, cursor="hand2")
        b1.place(x=930, y=70, width=220, height=220)

        b1_1 = Button(bg_img, text='Helpdesk', cursor="hand2",command=self.show_helpdesk, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=930, y=250, width=220, height=40)

        #Photos data
        img9 = Image.open(r"images\photos.jpeg")
        img9 = img9.resize((220, 220))
        self.photoimage9 = ImageTk.PhotoImage(img9)
        b1 = Button(bg_img, image=self.photoimage9, cursor="hand2", command=self.open_img)
        b1.place(x=85, y=330, width=220, height=220)

        b1_1 = Button(bg_img, text='Photos data', cursor="hand2", command=self.open_img, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=85, y=510, width=220, height=40)

        #Train data        
        img10 = Image.open(r"images\training.jpeg")
        img10 = img10.resize((220, 220))
        self.photoimage10 = ImageTk.PhotoImage(img10)
        b1 = Button(bg_img, image=self.photoimage10, cursor="hand2", command=self.train_data)
        b1.place(x=370, y=330, width=220, height=220)

        b1_1 = Button(bg_img, text='Train data', cursor="hand2", command=self.train_data, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=370, y=510, width=220, height=40)

        # Exit Image Button
        img_exit = Image.open(r"images\Exit.jpeg")
        img_exit = img_exit.resize((220, 220))  # Reduced size to match Train data button
        self.photoimage_exit = ImageTk.PhotoImage(img_exit)
        b_exit = Button(bg_img, image=self.photoimage_exit, cursor="hand2", command=self.exit_app)
        b_exit.place(x=655, y=330, width=220, height=180)  # Moved slightly to the right

        # Exit Text Button (Directly below Exit image)
        b_exit_txt = Button(bg_img, text='Exit', cursor="hand2", command=self.exit_app, font=("times new roman", 15, "bold"), bg="Blue", fg="white")
        b_exit_txt.place(x=655, y=510, width=220, height=40)  # Adjusted width & position




    def open_img(self):
        os.startfile("data")  #Image are in this folder

    # # Function buttons
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
    
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)
    
    def exit_app(self):
        self.root.destroy()  # Closes the application safely

  # Opens a new Exit window
    def show_helpdesk(self):
        messagebox.showinfo("Helpdesk", "📧 Email: papincegupta2059@gmail.com\n📞 Phone: +91 7011019759")




if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition_System(root)
    root.mainloop()   # mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event till the window is not closed.