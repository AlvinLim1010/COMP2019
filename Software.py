import tkinter as tk
from tkinter import ttk
import mysql.connector
import tkinter.messagebox
from tkinter.filedialog import askopenfile
from openpyxl import load_workbook

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

        rectangle = tk.Canvas(self, width=760, height=760)
        rectangle.create_line(15, 120, 745, 120)
        rectangle.create_rectangle(220, 500, 540, 270)
        rectangle.create_line(15, 600, 745, 600)
        rectangle.grid(row=0, column=0)

        titleLabel = ttk.Label(self, text="LOGIN", font=TitleFont)
        titleLabel.grid(column=0, row=0, pady=(0, 665))

        usernameLabel = tk.Label(self, text="Enter username:", font=("Arial", 12))
        usernameLabel.grid(column=0, row=0, pady=(200, 350))

        username = tk.StringVar()
        usernameEntered = tk.Entry(self, width=30, textvariable=username)
        usernameEntered.grid(column=0, row=0, pady=(220, 320))

        passwordLabel = tk.Label(self, text="Enter password:", font=("Arial", 12))
        passwordLabel.grid(column=0, row=0, pady=(300, 280))

        password = tk.StringVar()
        passwordEntered = tk.Entry(self, width=30, textvariable=password, show="*")
        passwordEntered.grid(column=0, row=0, pady=(320, 240))

        logInButton = tk.Button(self, text="LOGIN", font=("Arial", 10), fg="white", bg="grey", width=15, height=1
                                , command=lambda: validateLogin(username.get(), password.get()))
        logInButton.grid(column=0, row=0, pady=(400, 230))

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
                tkinter.messagebox.showerror("Error Login", "Invalid credentials!")
            cursor.close()
            conn.close()


class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        rectangle = tk.Canvas(self, width=760, height=760)
        rectangle.create_rectangle(15, 135, 740, 85)
        rectangle.create_line(15, 191, 155, 191)
        rectangle.create_rectangle(15, 740, 740, 200)
        rectangle.grid(row=0, column=0)

        logOutButton = tk.Button(self, text="LOG OUT", fg="white", bg="grey", width=15, height=1
                                 , command=lambda: controller.show_frame(LoginPage))
        logOutButton.grid(column=0, row=0, padx=(630, 0), pady=(0, 720))

        titleLabel = ttk.Label(self, text="HOME PAGE", font=TitleFont)
        titleLabel.grid(column=0, row=0, pady=(0, 665))

        homeButton = ttk.Button(self, text="HOME", command=lambda: controller.show_frame(HomePage))
        homeButton.grid(column=0, row=0, padx=(10, 625), pady=(0, 540))

        predictButton = ttk.Button(self, text="PREDICT", command=lambda: controller.show_frame(PredictionPage))
        predictButton.grid(column=0, row=0, padx=(110, 335), pady=(0, 540))

        trainButton = ttk.Button(self, text="TRAIN", command=lambda: controller.show_frame(TrainingPage))
        trainButton.grid(column=0, row=0, padx=(335, 130), pady=(0, 540))

        historyButton = ttk.Button(self, text="HISTORY", command=lambda: controller.show_frame(HistoryPage))
        historyButton.grid(column=0, row=0, padx=(625, 30), pady=(0, 540))

        instructionLabel = tk.Label(self, text="INSTRUCTIONS", font=("Arial", 15))
        instructionLabel.grid(column=0, row=0, padx=(10, 600), pady=(0, 410))


class PredictionPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def getExcel():
            file = askopenfile(filetypes=[('Excel Files', '*.xlsx')])
            wb = load_workbook(filename=file.name)
            wb2 = wb.active

            file_label = tk.Label(self, text='File Uploaded Successfully!', foreground='green')
            file_label.grid(column=0, row=0, padx=(10, 600), pady=(680, 15))
            file_label.after(3000, lambda: file_label.destroy())

        rectangle = tk.Canvas(self, width=760, height=760)
        rectangle.create_rectangle(15, 135, 740, 85)
        rectangle.create_rectangle(15, 645, 740, 160)
        rectangle.create_rectangle(35, 585, 720, 175)
        rectangle.grid(row=0, column=0)

        logOutButton = tk.Button(self, text="LOG OUT", fg="white", bg="grey", width=15, height=1
                                 , command=lambda: controller.show_frame(LoginPage))
        logOutButton.grid(column=0, row=0, padx=(630, 0), pady=(0, 720))

        titleLabel = ttk.Label(self, text="PREDICTION PAGE", font=TitleFont)
        titleLabel.grid(column=0, row=0, pady=(0, 665))

        homeButton = ttk.Button(self, text="HOME", command=lambda: controller.show_frame(HomePage))
        homeButton.grid(column=0, row=0, padx=(10, 625), pady=(0, 540))

        predictButton = ttk.Button(self, text="PREDICT", command=lambda: controller.show_frame(PredictionPage))
        predictButton.grid(column=0, row=0, padx=(110, 335), pady=(0, 540))

        trainButton = ttk.Button(self, text="TRAIN", command=lambda: controller.show_frame(TrainingPage))
        trainButton.grid(column=0, row=0, padx=(335, 130), pady=(0, 540))

        historyButton = ttk.Button(self, text="HISTORY", command=lambda: controller.show_frame(HistoryPage))
        historyButton.grid(column=0, row=0, padx=(625, 30), pady=(0, 540))

        importButton = tk.Button(self, text="IMPORT FILE", command=getExcel, fg="white", bg="grey", width=15, height=2)
        importButton.grid(column=0, row=0, padx=(10, 630), pady=(620, 20))

        importText = tk.Label(self, text="(ONLY .xlsx FILES)", font=("Arial", 10))
        importText.grid(column=0, row=0, padx=(10, 630), pady=(680, 20))

        doPredictionButton = tk.Button(self, text="DO PREDICTION", fg="white", bg="grey", width=15, height=2,
                                       command=lambda : controller.show_frame(OutputPage))
        doPredictionButton.grid(column=0, row=0, padx=(200, 200), pady=(610, 20))


class TrainingPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        rectangle = tk.Canvas(self, width=760, height=760)
        rectangle.create_rectangle(15, 135, 740, 85)
        rectangle.create_rectangle(15, 645, 740, 160)
        rectangle.create_rectangle(35, 585, 720, 175)
        rectangle.grid(row=0, column=0)

        logOutButton = tk.Button(self, text="LOG OUT", fg="white", bg="grey", width=15, height=1
                                 , command=lambda: controller.show_frame(LoginPage))
        logOutButton.grid(column=0, row=0, padx=(630, 0), pady=(0, 720))

        titleLabel = ttk.Label(self, text="TRAINING PAGE", font=TitleFont)
        titleLabel.grid(column=0, row=0, pady=(0, 665))

        homeButton = ttk.Button(self, text="HOME", command=lambda: controller.show_frame(HomePage))
        homeButton.grid(column=0, row=0, padx=(10, 625), pady=(0, 540))

        predictButton = ttk.Button(self, text="PREDICT", command=lambda: controller.show_frame(PredictionPage))
        predictButton.grid(column=0, row=0, padx=(110, 335), pady=(0, 540))

        trainButton = ttk.Button(self, text="TRAIN", command=lambda: controller.show_frame(TrainingPage))
        trainButton.grid(column=0, row=0, padx=(335, 130), pady=(0, 540))

        historyButton = ttk.Button(self, text="HISTORY", command=lambda: controller.show_frame(HistoryPage))
        historyButton.grid(column=0, row=0, padx=(625, 30), pady=(0, 540))

        importButton = tk.Button(self, text="IMPORT FILE", fg="white", bg="grey", width=15, height=2)
        importButton.grid(column=0, row=0, padx=(10, 630), pady=(620, 20))

        importText = tk.Label(self, text="(ONLY .xlsx FILES)", font=("Arial", 10))
        importText.grid(column=0, row=0, padx=(10, 630), pady=(680, 20))

        doTrainingButton = tk.Button(self, text="DO TRAINING", fg="white", bg="grey", width=15, height=2)
        doTrainingButton.grid(column=0, row=0, padx=(200, 200), pady=(610, 20))


class HistoryPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        rectangle = tk.Canvas(self, width=760, height=760)
        rectangle.create_rectangle(15, 135, 740, 85)
        rectangle.create_rectangle(15, 720, 740, 160)
        rectangle.grid(row=0, column=0)

        logOutButton = tk.Button(self, text="LOG OUT", fg="white", bg="grey", width=15, height=1
                                 , command=lambda: controller.show_frame(LoginPage))
        logOutButton.grid(column=0, row=0, padx=(630, 0), pady=(0, 720))

        titleLabel = ttk.Label(self, text="HISTORY PAGE", font=TitleFont)
        titleLabel.grid(column=0, row=0, pady=(0, 665))

        homeButton = ttk.Button(self, text="HOME", command=lambda: controller.show_frame(HomePage))
        homeButton.grid(column=0, row=0, padx=(10, 625), pady=(0, 540))

        predictButton = ttk.Button(self, text="PREDICT", command=lambda: controller.show_frame(PredictionPage))
        predictButton.grid(column=0, row=0, padx=(110, 335), pady=(0, 540))

        trainButton = ttk.Button(self, text="TRAIN", command=lambda: controller.show_frame(TrainingPage))
        trainButton.grid(column=0, row=0, padx=(335, 130), pady=(0, 540))

        historyButton = ttk.Button(self, text="HISTORY", command=lambda: controller.show_frame(HistoryPage))
        historyButton.grid(column=0, row=0, padx=(625, 30), pady=(0, 540))


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
