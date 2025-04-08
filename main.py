import tkinter as tk
from tkinter import ttk, messagebox as mess
import tkinter.simpledialog as tsd
import cv2, os, csv, numpy as np
from PIL import Image
import pandas as pd
import datetime
import time

############################################# FUNCTIONS ################################################

def assure_path_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

##################################################################################

def tick():
    clock.config(text=time.strftime('%H:%M:%S'))
    clock.after(200, tick)

###################################################################################

def contact():
    mess._show(title='Contact us', message="Please contact us on : 'harshith0929@gmail.com'")

###################################################################################

def check_haarcascadefile():
    if not os.path.isfile("haarcascade_frontalface_default.xml"):
        mess._show(title='Some file missing', message='Please contact us for help')
        window.destroy()

###################################################################################

def save_pass():
    assure_path_exists("TrainingImageLabel/")
    path = os.path.join("TrainingImageLabel", "psd.txt")
    if os.path.isfile(path):
        with open(path, "r") as tf:
            key = tf.read()
    else:
        master.destroy()
        new_pas = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
        if new_pas:
            with open(path, "w") as tf:
                tf.write(new_pas)
            mess._show(title='Password Registered', message='New password was registered successfully!!')
        else:
            mess._show(title='No Password Entered', message='Password not set!! Please try again')
        return

    op, newp, nnewp = old.get(), new.get(), nnew.get()
    if op == key:
        if newp == nnewp:
            with open(path, "w") as tf:
                tf.write(newp)
            mess._show(title='Password Changed', message='Password changed successfully!!')
        else:
            mess._show(title='Error', message='Confirm new password again!!!')
    else:
        mess._show(title='Wrong Password', message='Please enter correct old password.')
    master.destroy()

###################################################################################

def change_pass():
    global master
    master = tk.Tk()
    master.geometry("400x160")
    master.resizable(False, False)
    master.title("Change Password")
    master.configure(background="white")

    global old, new, nnew
    tk.Label(master, text='Enter Old Password', bg='white', font=('comic', 12, 'bold')).place(x=10, y=10)
    old = tk.Entry(master, width=25, fg="black", relief='solid', font=('comic', 12, 'bold'), show='*')
    old.place(x=180, y=10)

    tk.Label(master, text='Enter New Password', bg='white', font=('comic', 12, 'bold')).place(x=10, y=45)
    new = tk.Entry(master, width=25, fg="black", relief='solid', font=('comic', 12, 'bold'), show='*')
    new.place(x=180, y=45)

    tk.Label(master, text='Confirm New Password', bg='white', font=('comic', 12, 'bold')).place(x=10, y=80)
    nnew = tk.Entry(master, width=25, fg="black", relief='solid', font=('comic', 12, 'bold'), show='*')
    nnew.place(x=180, y=80)

    tk.Button(master, text="Cancel", command=master.destroy, fg="black", bg="red", height=1, width=25,
              activebackground="white", font=('comic', 10, 'bold')).place(x=200, y=120)
    tk.Button(master, text="Save", command=save_pass, fg="black", bg="#00fcca", height=1, width=25,
              activebackground="white", font=('comic', 10, 'bold')).place(x=10, y=120)
    master.mainloop()

###################################################################################

def psw():
    assure_path_exists("TrainingImageLabel/")
    path = os.path.join("TrainingImageLabel", "psd.txt")
    if os.path.isfile(path):
        with open(path, "r") as tf:
            key = tf.read()
    else:
        new_pas = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
        if new_pas:
            with open(path, "w") as tf:
                tf.write(new_pas)
            mess._show(title='Password Registered', message='New password was registered successfully!!')
        else:
            mess._show(title='No Password Entered', message='Password not set!! Please try again')
        return

    password = tsd.askstring('Password', 'Enter Password', show='*')
    if password == key:
        TrainImages()
    elif password:
        mess._show(title='Wrong Password', message='You have entered wrong password')

######################################################################################

def clear():
    txt.delete(0, 'end')
    message1.configure(text="1)Take Images  >>>  2)Save Profile")

def clear2():
    txt2.delete(0, 'end')
    message1.configure(text="1)Take Images  >>>  2)Save Profile")

#######################################################################################

def TakeImages():
    check_haarcascadefile()
    assure_path_exists("StudentDetails/")
    assure_path_exists("TrainingImage/")
    serial = 1

    path = "StudentDetails/StudentDetails.csv"
    if os.path.isfile(path):
        with open(path, 'r') as csvFile:
            serial = len(list(csv.reader(csvFile))) // 2
    else:
        with open(path, 'a+') as csvFile:
            csv.writer(csvFile).writerow(['SERIAL NO.', '', 'ID', '', 'NAME'])

    Id, name = txt.get(), txt2.get()
    if name.replace(" ", "").isalpha():
        cam = cv2.VideoCapture(0)
        detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        sampleNum = 0

        while True:
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                sampleNum += 1
                cv2.imwrite(f"TrainingImage/{name}.{serial}.{Id}.{sampleNum}.jpg", gray[y:y + h, x:x + w])
                cv2.imshow('Taking Images', img)
            if cv2.waitKey(100) & 0xFF == ord('q') or sampleNum >= 100:
                break

        cam.release()
        cv2.destroyAllWindows()

        with open(path, 'a+') as csvFile:
            csv.writer(csvFile).writerow([serial, '', Id, '', name])
        message1.configure(text=f"Images Taken for ID : {Id}")
    else:
        message.configure(text="Enter Correct name")

########################################################################################

def TrainImages():
    check_haarcascadefile()
    assure_path_exists("TrainingImageLabel/")
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    faces, Ids = getImagesAndLabels("TrainingImage")

    if faces:
        recognizer.train(faces, np.array(Ids))
        recognizer.save("TrainingImageLabel/Trainner.yml")
        message1.configure(text="Profile Saved Successfully")
        message.configure(text=f'Total Registrations till now  : {Ids[0]}')
    else:
        mess._show(title='No Registrations', message='Please Register someone first!!!')

############################################################################################

def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces, Ids = [], []

    for imagePath in imagePaths:
        pilImage = Image.open(imagePath).convert('L')
        imageNp = np.array(pilImage, 'uint8')
        Id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces.append(imageNp)
        Ids.append(Id)

    return faces, Ids

###########################################################################################

def TrackImages():
    check_haarcascadefile()
    assure_path_exists("Attendance/")
    assure_path_exists("StudentDetails/")
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    path = "TrainingImageLabel/Trainner.yml"

    if os.path.isfile(path):
        recognizer.read(path)
    else:
        mess._show(title='Data Missing', message='Please click on Save Profile to reset data!!')
        return

    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX

    path = "StudentDetails/StudentDetails.csv"
    if os.path.isfile(path):
        df = pd.read_csv(path)
    else:
        mess._show(title='Details Missing', message='Students details are missing, please check!')
        cam.release()
        cv2.destroyAllWindows()
        window.destroy()

    attendance_list = []

    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)

        for (x, y, w, h) in faces:
            serial, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if conf < 50:
                name = df.loc[df['SERIAL NO.'] == serial]['NAME'].values
                Id = df.loc[df['SERIAL NO.'] == serial]['ID'].values
                tt = str(Id[0]) + "-" + name[0]
                attendance_list.append([Id[0], name[0]])
            else:
                tt = 'Unknown'
            cv2.putText(im, tt, (x + h, y), font, 1, (255, 255, 255), 2)
            cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow('Taking Attendance', im)

        if cv2.waitKey(1) == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

    if attendance_list:
        col_names = ['ID', '', 'Name', '', 'Date', '', 'Time']
        path = "Attendance/Attendance_" + str(datetime.date.today()) + ".csv"

        with open(path, 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(col_names)

        for entry in attendance_list:
            with open(path, 'a+') as csvFile:
                writer = csv.writer(csvFile)
                now = time.strftime("%H:%M:%S")
                writer.writerow([entry[0], '', entry[1], '', datetime.date.today(), '', now])

        message1.configure(text="Attendance Taken")

############################################################################################

######################################## GUI ###########################################

window = tk.Tk()
window.title("Face Recognizer")

window.geometry('1280x720')
window.configure(background='white')

frame1 = tk.Frame(window, bg="white")
frame1.place(relx=0.03, rely=0.17, relwidth=0.45, relheight=0.80)

frame2 = tk.Frame(window, bg="white")
frame2.place(relx=0.52, rely=0.17, relwidth=0.45, relheight=0.80)

clock = tk.Label(window, fg="black", bg="white", width=20, height=1, font=('comic', 12, 'bold'))
clock.place(x=860, y=10)
tick()

head1 = tk.Label(window, text="Face-Recognition-Based-Attendance-System", fg="black", bg="white", font=('comic', 30, 'bold'))
head1.place(x=180, y=0)

message1 = tk.Label(window, text="1)Take Images  >>>  2)Save Profile", bg="white", fg="black", width=50, height=1, activebackground="yellow", font=('comic', 15, 'bold'))
message1.place(x=250, y=50)

txt = tk.Entry(frame1, width=20, fg="black", relief='solid', font=('comic', 15, 'bold'))
txt.place(x=220, y=200)

txt2 = tk.Entry(frame1, width=20, fg="black", relief='solid', font=('comic', 15, 'bold'))
txt2.place(x=220, y=300)

clearButton = tk.Button(frame1, text="Clear", command=clear, fg="black", bg="#fcca00", width=20, height=2, activebackground="white", font=('comic', 15, 'bold'))
clearButton.place(x=220, y=400)

clearButton2 = tk.Button(frame1, text="Clear", command=clear2, fg="black", bg="#fcca00", width=20, height=2, activebackground="white", font=('comic', 15, 'bold'))
clearButton2.place(x=220, y=500)

takeImage = tk.Button(frame1, text="Take Images", command=TakeImages, fg="black", bg="#00fcca", width=20, height=3, activebackground="white", font=('comic', 15, 'bold'))
takeImage.place(x=220, y=600)

trainImage = tk.Button(frame2, text="Save Profile", command=psw, fg="black", bg="#00fcca", width=20, height=3, activebackground="white", font=('comic', 15, 'bold'))
trainImage.place(x=220, y=600)

trackImg = tk.Button(frame2, text="Take Attendance", command=TrackImages, fg="black", bg="#fcca00", width=20, height=3, activebackground="white", font=('comic', 15, 'bold'))
trackImg.place(x=220, y=400)

quitWindow = tk.Button(window, text="Quit", command=window.destroy, fg="white", bg="red", width=20, height=3, activebackground="Red", font=('comic', 15, 'bold'))
quitWindow.place(x=1050, y=620)

window.mainloop()
