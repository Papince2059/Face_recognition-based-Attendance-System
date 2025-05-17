
import os
import cv2
import numpy as np
from datetime import datetime
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Based Standard Attendance System")

        self.marked_students = set()  # Track students who have marked attendance

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 25, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1300, height=45)

        # Left image
        img_top = Image.open(r"Images\faceRecognize.jpeg").resize((650, 650))
        self.photoimage_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimage_top)
        f_lbl.place(x=0, y=45, width=650, height=650)

        # Right image
        img_bottom = Image.open(r"images\facial_recognition.jpg").resize((650, 650))
        self.photoimage_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl = Label(self.root, image=self.photoimage_bottom)
        f_lbl.place(x=650, y=45, width=650, height=650)

        # Face Recognition Button
        b1_1 = Button(self.root, text='Face Recognition', cursor="hand2", command=self.face_recognize, font=("times new roman", 15, "bold"), bg="darkgreen", fg="white")
        b1_1.place(x=230, y=570, width=180, height=40)

        # Save & Exit Button
        b2_1 = Button(self.root, text='Save & Exit', cursor="hand2", command=self.exit_to_main, font=("times new roman", 15, "bold"), bg="red", fg="white")
        b2_1.place(x=450, y=570, width=180, height=40)

    # Attendance Function
    def mark_attendance(self, i, r, n, d):
        now = datetime.now()
        dt = now.strftime("%d/%m/%Y")
        dtString = now.strftime("%H:%M:%S")

        # Check if the student already marked attendance
        if i in self.marked_students:
            messagebox.showinfo("Attendance", f"Attendance already marked for {n}. Camera shutting down.")
            self.shutdown_camera()
            return

        with open('attendance.csv', "r+", newline="\n") as f:
            myData = f.readlines()
            name_list = [line.split(",")[0] for line in myData]

            if i not in name_list:
                f.writelines(f"{i},{r},{n},{d},{dtString},{dt}, Present\n")
                messagebox.showinfo("Attendance", f"Attendance marked for {n}.")
            else:
                messagebox.showinfo("Attendance", f"Attendance already marked for {n} today.")
                self.shutdown_camera()  # Close camera if attendance is already marked

        # Add student to the marked list
        self.marked_students.add(i)

    # Face Recognition Function
    def face_recognize(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbours, color, text, clf):
            if img is None or img.size == 0:  # Check if the frame is empty
                return []

            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbours)

            coord = []
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)
                id, predict = clf.predict(gray_img[y:y+h, x:x+w])
                confidence = int((100 * (1 - predict / 300)))

                con = mysql.connector.connect(host="localhost", username="root", password="Papince$200000", database="face_recognizer")
                my_cursor = con.cursor()

                my_cursor.execute("SELECT Student_ID FROM students WHERE Student_ID=" + str(id))
                i = my_cursor.fetchone()
                if i:
                    i = i[0]
                else:
                    continue

                my_cursor.execute("SELECT `RollNo.` FROM students WHERE Student_ID=" + str(id))
                r = my_cursor.fetchone()[0]

                my_cursor.execute("SELECT Name FROM students WHERE Student_ID=" + str(id))
                n = my_cursor.fetchone()[0]

                my_cursor.execute("SELECT Department FROM students WHERE Student_ID=" + str(id))
                d = my_cursor.fetchone()[0]

                if confidence > 77:
                    cv2.putText(img, f"ID: {i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 2)
                    cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 2)
                    cv2.putText(img, f"Name: {n}", (x, y - 25), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 2)
                    cv2.putText(img, f"Dept: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 2)
                    self.mark_attendance(i, r, n, d)
                else:
                    cv2.putText(img, "Unknown", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 0, 0), 2)

                coord.append((x, y, w, h))
            return coord

        def recognize(img, clf, faceCascade):
            if img is None or img.size == 0:  # Check for empty frame
                return img
            draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()

        if not os.path.exists("classfier.xml"):
            messagebox.showerror("Error", "Model file 'classfier.xml' not found!")
            return

        clf.read("classfier.xml")
        self.video_cap = cv2.VideoCapture(0)

        if not self.video_cap.isOpened():
            messagebox.showerror("Error", "Camera not accessible. Please check your webcam.")
            return

        while True:
            ret, img = self.video_cap.read()
            if not ret or img is None:
                messagebox.showerror("Error", "Failed to capture image. Camera may not be accessible.")
                break
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Press 'Enter' to exit
                break

        self.shutdown_camera()

    # Function to shut down the camera
    def shutdown_camera(self):
        if hasattr(self, 'video_cap'):
            self.video_cap.release()
        cv2.destroyAllWindows()

    # Save & Exit function
    def exit_to_main(self):
        self.shutdown_camera()
        self.root.destroy()
        os.system("python main.py")

# Run the program
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()


# import os
# import cv2
# import numpy as np
# import pickle
# import torch
# from datetime import datetime
# from tkinter import *
# from tkinter import messagebox
# from deepface import DeepFace
# from ultralytics import YOLO  # YOLOv8 for face detection

# class FaceRecognition:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("Face Recognition Based Attendance System")

#         # Load YOLOv8 Model
#         model_path = r"C:\Users\Papince Gupta\OneDrive\Desktop\semester 6\AI\Project\yolov8n-face.pt"
#         if not os.path.exists(model_path):
#             messagebox.showerror("Error", "YOLO model file not found!")
#             return
        
#         self.model = YOLO(model_path)

#         # Load trained embeddings
#         self.embeddings = self.load_embeddings()

#         # Track students who have marked attendance
#         self.marked_students = set()

#         title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 25, "bold"), bg="white", fg="blue")
#         title_lbl.place(x=0, y=0, width=1300, height=45)

#         b1_1 = Button(self.root, text='Face Recognition', cursor="hand2", command=self.face_recognize, font=("times new roman", 15, "bold"), bg="darkgreen", fg="white")
#         b1_1.place(x=230, y=570, width=180, height=40)

#     def load_embeddings(self):
#         if os.path.exists("face_embeddings.pkl"):
#             with open("face_embeddings.pkl", "rb") as f:
#                 return pickle.load(f)
#         else:
#             messagebox.showerror("Error", "No trained embeddings found! Please train the model first.")
#             return {}

#     def mark_attendance(self, name):
#         now = datetime.now()
#         dt = now.strftime("%d/%m/%Y")
#         dtString = now.strftime("%H:%M:%S")

#         if name in self.marked_students:
#             messagebox.showinfo("Attendance", f"Attendance already marked for {name}.")
#             return

#         with open('attendance.csv', "a") as f:
#             f.write(f"{name},{dtString},{dt}, Present\n")

#         messagebox.showinfo("Attendance", f"Attendance marked for {name}.")
#         self.marked_students.add(name)

#     def recognize_face(self, face_img):
#         try:
#             if face_img is None or face_img.size == 0:
#                 return "Unknown"

#             result = DeepFace.represent(face_img, model_name="Facenet", enforce_detection=False)
#             if result:
#                 detected_embedding = np.array(result[0]['embedding'])
#                 best_match = None
#                 min_dist = float("inf")

#                 for person, stored_embedding in self.embeddings.items():
#                     dist = np.linalg.norm(detected_embedding - np.array(stored_embedding))
#                     if dist < min_dist:
#                         min_dist = dist
#                         best_match = person

#                 return best_match if min_dist < 0.6 else "Unknown"
#             return "Unknown"
#         except Exception as e:
#             print("Recognition Error:", e)
#             return "Unknown"

#     def face_recognize(self):
#         cap = cv2.VideoCapture(0)
#         if not cap.isOpened():
#             messagebox.showerror("Error", "Could not access the camera.")
#             return

#         while True:
#             ret, frame = cap.read()
#             if not ret:
#                 messagebox.showerror("Error", "Failed to capture image.")
#                 break

#             results = self.model.predict(frame)  # Ensure correct method usage
#             for result in results:
#                 if hasattr(result, 'boxes') and result.boxes is not None:
#                     for box in result.boxes.xyxy.cpu().numpy():
#                         x1, y1, x2, y2 = map(int, box[:4])

#                         # Ensure face crop is within image bounds
#                         h, w, _ = frame.shape
#                         x1, y1, x2, y2 = max(0, x1), max(0, y1), min(w, x2), min(h, y2)

#                         face_img = frame[y1:y2, x1:x2]
#                         if face_img is not None and face_img.shape[0] > 0 and face_img.shape[1] > 0:
#                             name = self.recognize_face(face_img)
#                             color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)
#                             cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
#                             cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
#                             if name != "Unknown":
#                                 self.mark_attendance(name)

#             cv2.imshow("Face Recognition", frame)
#             if cv2.waitKey(1) == 13:  # Press 'Enter' to exit
#                 break

#         cap.release()
#         cv2.destroyAllWindows()

#     def shutdown_camera(self):
#         cv2.destroyAllWindows()

# # Run the program
# if __name__ == "__main__":
#     root = Tk()
#     obj = FaceRecognition(root)
#     root.mainloop()
