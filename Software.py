import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
import mysql.connector
from tkinter.filedialog import askopenfile
from openpyxl import load_workbook
from PIL import Image, ImageTk

TitleFont = ("Arial", 35)


class tkinterApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        self.resizable(0, 0)
        windowWidth = self.winfo_screenwidth()
        windowHeight = self.winfo_screenheight()
        appWidth = 760
        appHeight = 760

        x = int((windowWidth / 2) - (appWidth / 2))
        y = int((windowHeight / 2) - (appHeight / 2))

        self.geometry("{}x{}+{}+{}".format(appWidth, appHeight, x, y))

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (LoginPage, HomePage, PredictionPage, TrainingPage, HistoryPage, OutputPage):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        self.title('Software')


class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Background image
        bg = Image.open("Pictures/login.png")
        resizebg = bg.resize((760, 760), Image.ANTIALIAS)
        self.newbg = ImageTk.PhotoImage(resizebg)

        rectangle = tk.Canvas(self, width=760, height=760)
        rectangle.create_rectangle(220, 500, 540, 270)
        rectangle.create_image(0, 0, image=self.newbg, anchor=NW)
        rectangle.create_text(385, 230, text="LOGIN", fill="#00557E", font=('Raleway', 30, 'bold'))
        rectangle.create_text(325, 295, text="Username", fill="black", font=('Raleway', 11))
        rectangle.create_text(325, 365, text="Password", fill="black", font=('Raleway', 11))
        rectangle.grid(row=0, column=0)

        username = tk.StringVar()
        usernameEntered = tk.Entry(self, width=30, textvariable=username)
        usernameEntered.grid(column=0, row=0, padx=(0, 0), pady=(220, 350))

        password = tk.StringVar()
        passwordEntered = tk.Entry(self, width=30, textvariable=password, show="*")
        passwordEntered.grid(column=0, row=0, pady=(320, 310))

        # Define functions
        def on_enter(e):
            button.config(background='#00557E', foreground="white")

        def on_leave(e):
            button.config(background='SystemButtonFace', foreground='black')

        # Create a Button
        button = tk.Button(self, text="Login", font=('Raleway', 11), width=10, height=0, bd=0,
                           command=lambda: validateLogin(username.get(), password.get()))
        button.grid(column=0, row=0, pady=(400, 230))

        # Bind the Enter and Leave Events to the Button
        button.bind('<Enter>', on_enter)
        button.bind('<Leave>', on_leave)

        def validateLogin(user_username, user_password):
            conn = mysql.connector.connect(host="localhost", port="3306", user="root", password="", database="project")
            cursor = conn.cursor()
            cursor.execute("SElECT * FROM admin WHERE username =%s AND pass = %s", [user_username, user_password])
            record = cursor.fetchall()
            usernameEntered.delete(0, 'end')
            passwordEntered.delete(0, 'end')
            if record:
                controller.show_frame(HomePage)
            else:
                messagebox.showinfo("Invalid login!", "Invalid credentials")
            cursor.close()
            conn.close()


class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Background image
        bg = Image.open("Pictures/template.png")
        resizebg = bg.resize((760, 760), Image.ANTIALIAS)

        self.newbg = ImageTk.PhotoImage(resizebg)
        rectangle = tk.Canvas(self, width=760, height=930)
        rectangle.create_image(0, 0, image=self.newbg, anchor=NW)
        rectangle.create_text(425, 22, text="H O M E", fill="White", font=('Raleway', 20, 'bold'))
        rectangle.grid(row=0, column=0)

        logOutButton = tk.Button(self, text="LOG OUT", fg="black", bg="white", width=10, height=1, bd=0
                                 , command=lambda: controller.show_frame(LoginPage))
        logOutButton.grid(column=0, row=0, padx=(630, 0), pady=(0, 885))

        homeButton = tk.Button(self, text="HOME", width=10, height=1, bd=0,
                               command=lambda: controller.show_frame(HomePage))
        homeButton.grid(column=0, row=0, padx=(0, 625), pady=(0, 440))

        predictButton = tk.Button(self, text="PREDICT", width=10, height=1, bd=0,
                                  command=lambda: controller.show_frame(PredictionPage))
        predictButton.grid(column=0, row=0, padx=(0, 625), pady=(100, 390))

        trainButton = tk.Button(self, text="TRAIN", width=10, height=1, bd=0,
                                command=lambda: controller.show_frame(TrainingPage))
        trainButton.grid(column=0, row=0, padx=(0, 625), pady=(200, 340))

        historyButton = tk.Button(self, text="HISTORY", width=10, height=1, bd=0,
                                  command=lambda: controller.show_frame(HistoryPage))
        historyButton.grid(column=0, row=0, padx=(0, 625), pady=(300, 290))


class PredictionPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def getExcel():
            file = askopenfile(filetypes=[('Excel Files', '*.xlsx')])
            inputExcelFile = load_workbook(filename=file.name)
            inputExcelFile2 = inputExcelFile.active

            file_label = tk.Label(self, text='File Uploaded Successfully!', foreground='green')
            file_label.grid(column=0, row=0, padx=(10, 600), pady=(680, 15))
            file_label.after(3000, lambda: file_label.destroy())

        # Background image
        bg = Image.open("Pictures/template.png")
        resizebg = bg.resize((760, 760), Image.ANTIALIAS)

        self.newbg = ImageTk.PhotoImage(resizebg)
        rectangle = tk.Canvas(self, width=760, height=930)
        rectangle.create_image(0, 0, image=self.newbg, anchor=NW)
        rectangle.create_text(425, 22, text="P R E D I C T I O N", fill="White", font=('Raleway', 20, 'bold'))
        rectangle.create_text(195, 745, text="(ONLY .xlsx FILES)", fill="White", font=('Raleway', 10))
        rectangle.grid(row=0, column=0)

        logOutButton = tk.Button(self, text="LOG OUT", fg="black", bg="white", width=10, height=1, bd=0,
                                 command=lambda: controller.show_frame(LoginPage))
        logOutButton.grid(column=0, row=0, padx=(630, 0), pady=(0, 885))

        homeButton = tk.Button(self, text="HOME", width=10, height=1, bd=0,
                               command=lambda: controller.show_frame(HomePage))
        homeButton.grid(column=0, row=0, padx=(0, 625), pady=(0, 440))

        predictButton = tk.Button(self, text="PREDICT", width=10, height=1, bd=0,
                                  command=lambda: controller.show_frame(PredictionPage))
        predictButton.grid(column=0, row=0, padx=(0, 625), pady=(100, 390))

        trainButton = tk.Button(self, text="TRAIN", width=10, height=1, bd=0,
                                command=lambda: controller.show_frame(TrainingPage))
        trainButton.grid(column=0, row=0, padx=(0, 625), pady=(200, 340))

        historyButton = tk.Button(self, text="HISTORY", width=10, height=1, bd=0,
                                  command=lambda: controller.show_frame(HistoryPage))
        historyButton.grid(column=0, row=0, padx=(0, 625), pady=(300, 290))

        importButton = tk.Button(self, text="IMPORT FILE", command=getExcel, fg="black", bg="white", width=10, height=1)
        importButton.grid(column=0, row=0, padx=(10, 380), pady=(520, 20))

        doPredictionButton = tk.Button(self, text="DO PREDICTION", fg="black", bg="white", width=13, height=1,
                                       command=lambda: controller.show_frame(OutputPage))
        doPredictionButton.grid(column=0, row=0, padx=(200, 100), pady=(520, 20))


class TrainingPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Background image
        bg = Image.open("Pictures/template.png")
        resizebg = bg.resize((760, 760), Image.ANTIALIAS)

        self.newbg = ImageTk.PhotoImage(resizebg)
        rectangle = tk.Canvas(self, width=760, height=930)
        rectangle.create_image(0, 0, image=self.newbg, anchor=NW)
        rectangle.create_text(425, 22, text="T R A I N I N G", fill="White", font=('Raleway', 20, 'bold'))
        rectangle.create_text(195, 745, text="(ONLY .xlsx FILES)", fill="White", font=('Raleway', 10))
        rectangle.grid(row=0, column=0)

        logOutButton = tk.Button(self, text="LOG OUT", fg="black", bg="white", width=10, height=1, bd=0,
                                 command=lambda: controller.show_frame(LoginPage))
        logOutButton.grid(column=0, row=0, padx=(630, 0), pady=(0, 885))

        homeButton = tk.Button(self, text="HOME", width=10, height=1, bd=0,
                               command=lambda: controller.show_frame(HomePage))
        homeButton.grid(column=0, row=0, padx=(0, 625), pady=(0, 440))

        predictButton = tk.Button(self, text="PREDICT", width=10, height=1, bd=0,
                                  command=lambda: controller.show_frame(PredictionPage))
        predictButton.grid(column=0, row=0, padx=(0, 625), pady=(100, 390))

        trainButton = tk.Button(self, text="TRAIN", width=10, height=1, bd=0,
                                command=lambda: controller.show_frame(TrainingPage))
        trainButton.grid(column=0, row=0, padx=(0, 625), pady=(200, 340))

        historyButton = tk.Button(self, text="HISTORY", width=10, height=1, bd=0,
                                  command=lambda: controller.show_frame(HistoryPage))
        historyButton.grid(column=0, row=0, padx=(0, 625), pady=(300, 290))

        importButton = tk.Button(self, text="IMPORT FILE", fg="black", bg="white", width=10, height=1)
        importButton.grid(column=0, row=0, padx=(10, 380), pady=(520, 20))

        doPredictionButton = tk.Button(self, text="DO TRAINING", fg="black", bg="white", width=13, height=1,
                                       command=lambda: controller.show_frame(OutputPage))
        doPredictionButton.grid(column=0, row=0, padx=(200, 100), pady=(520, 20))


class HistoryPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Background image
        bg = Image.open("Pictures/template.png")
        resizebg = bg.resize((760, 760), Image.ANTIALIAS)

        self.newbg = ImageTk.PhotoImage(resizebg)
        rectangle = tk.Canvas(self, width=760, height=930)
        rectangle.create_image(0, 0, image=self.newbg, anchor=NW)
        rectangle.create_text(425, 22, text="H I S T O R Y", fill="White", font=('Raleway', 20, 'bold'))
        rectangle.grid(row=0, column=0)

        logOutButton = tk.Button(self, text="LOG OUT", fg="black", bg="white", width=10, height=1, bd=0
                                 , command=lambda: controller.show_frame(LoginPage))
        logOutButton.grid(column=0, row=0, padx=(630, 0), pady=(0, 885))

        homeButton = tk.Button(self, text="HOME", width=10, height=1, bd=0,
                               command=lambda: controller.show_frame(HomePage))
        homeButton.grid(column=0, row=0, padx=(0, 625), pady=(0, 440))

        predictButton = tk.Button(self, text="PREDICT", width=10, height=1, bd=0,
                                  command=lambda: controller.show_frame(PredictionPage))
        predictButton.grid(column=0, row=0, padx=(0, 625), pady=(100, 390))

        trainButton = tk.Button(self, text="TRAIN", width=10, height=1, bd=0,
                                command=lambda: controller.show_frame(TrainingPage))
        trainButton.grid(column=0, row=0, padx=(0, 625), pady=(200, 340))

        historyButton = tk.Button(self, text="HISTORY", width=10, height=1, bd=0,
                                  command=lambda: controller.show_frame(HistoryPage))
        historyButton.grid(column=0, row=0, padx=(0, 625), pady=(300, 290))


class OutputPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        rectangle = tk.Canvas(self, width=760, height=760)
        rectangle.create_rectangle(15, 135, 740, 85)
        rectangle.create_rectangle(15, 630, 740, 160)
        rectangle.grid(row=0, column=0)

        logOutButton = tk.Button(self, text="LOG OUT", fg="white", bg="grey", width=15, height=1
                                 , command=lambda: controller.show_frame(LoginPage))
        logOutButton.grid(column=0, row=0, padx=(630, 0), pady=(0, 720))

        titleLabel = ttk.Label(self, text="OUTPUT PAGE", font=TitleFont)
        titleLabel.grid(column=0, row=0, pady=(0, 665))

        homeButton = ttk.Button(self, text="HOME", command=lambda: controller.show_frame(HomePage))
        homeButton.grid(column=0, row=0, padx=(10, 625), pady=(0, 540))

        predictButton = ttk.Button(self, text="PREDICT", command=lambda: controller.show_frame(PredictionPage))
        predictButton.grid(column=0, row=0, padx=(110, 335), pady=(0, 540))

        trainButton = ttk.Button(self, text="TRAIN", command=lambda: controller.show_frame(TrainingPage))
        trainButton.grid(column=0, row=0, padx=(335, 130), pady=(0, 540))

        historyButton = ttk.Button(self, text="HISTORY", command=lambda: controller.show_frame(HistoryPage))
        historyButton.grid(column=0, row=0, padx=(625, 30), pady=(0, 540))

        newDataButton = tk.Button(self, text="INPUT NEW DATA", fg="white", bg="grey", width=17, height=1)
        newDataButton.grid(column=0, row=0, padx=(0, 600), pady=(560, 0))

        downloadButton = tk.Button(self, text="DOWNLOAD OUTPUT", fg="white", bg="grey", width=17, height=1)
        downloadButton.grid(column=0, row=0, padx=(150, 450), pady=(560, 0))


app = tkinterApp()
app.mainloop()
