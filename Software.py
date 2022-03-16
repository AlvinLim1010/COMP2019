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
        appWidth = 1100
        appHeight = 700

        x = int((windowWidth / 2) - (appWidth / 2))
        y = int((windowHeight / 2) - (appHeight / 2))

        self.geometry("{}x{}+{}+{}".format(appWidth, appHeight, x, y))

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (HomePage, PredictionPage, HistoryPage, OutputPage):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(PredictionPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        self.title('Software')

# class LoginPage(tk.Frame):
#
#     def init(self, parent, controller):
#         tk.Frame.init(self, parent)
#
#         # Background image
#         bg = Image.open("Pictures/login.png")
#         resizebg = bg.resize((760, 760), Image.ANTIALIAS)
#         self.newbg = ImageTk.PhotoImage(resizebg)
#
#         rectangle = tk.Canvas(self, width=760, height=760)
#         rectangle.create_rectangle(220, 500, 540, 270)
#         rectangle.create_image(0, 0, image=self.newbg, anchor=NW)
#         rectangle.create_text(385, 230, text="LOGIN", fill="#00557E", font=('Raleway', 30, 'bold'))
#         rectangle.create_text(325, 295, text="Username", fill="black", font=('Raleway', 11))
#         rectangle.create_text(325, 365, text="Password", fill="black", font=('Raleway', 11))
#         rectangle.grid(row=0, column=0)
#
#         username = tk.StringVar()
#         usernameEntered = tk.Entry(self, width=30, textvariable=username)
#         usernameEntered.grid(column=0, row=0, padx=(0, 0), pady=(220, 350))
#
#         password = tk.StringVar()
#         passwordEntered = tk.Entry(self, width=30, textvariable=password, show="*")
#         passwordEntered.grid(column=0, row=0, pady=(320, 310))
#
#         # Define functions
#         def on_enter(e):
#             button.config(background='#00557E', foreground="white")
#
#         def on_leave(e):
#             button.config(background='SystemButtonFace', foreground='black')
#
#         # Create a Button
#         # button = tk.Button(self, text="Login", font=('Raleway', 11), width=10, height=0, bd=0,
#         #                    command=lambda: validateLogin(username.get(), password.get()))
#         # button.grid(column=0, row=0, pady=(400, 230))
#
#         # Bind the Enter and Leave Events to the Button
#         button.bind('<Enter>', on_enter)
#         button.bind('<Leave>', on_leave)

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Background image
        bg = Image.open("Pictures/GUI1.png")
        resizebg = bg.resize((1100,700), Image.ANTIALIAS)

        self.newbg = ImageTk.PhotoImage(resizebg)
        rectangle = tk.Canvas(self, width=1100, height=700, borderwidth=0, highlightthickness=0)
        rectangle.create_image(0, 0, image=self.newbg, anchor=NW)
        rectangle.create_text(130, 155, text="POME Prediction AI", fill="#DDAA85", font=('Raleway', 17, 'bold'))
        rectangle.grid(row=0, column=0)

        aboutButton = tk.Button(self, text="ABOUT", fg="#DDAA85", bg="#4F3D2F", width=30, height=2, bd=0, activebackground="#4F3D2F",
                                activeforeground="#DDAA85", font=('Raleway', 10, 'bold'),
                                command=lambda: controller.show_frame(HomePage))
        aboutButton.grid(column=0, row=0, padx=(0, 840), pady=(0, 135))

        predictButton = tk.Button(self, text="PREDICT", fg="#DDAA85", bg="Black", width=30, height=2, bd=0, activebackground="Black",
                                  activeforeground="#DDAA85", font=('Raleway', 10, 'bold'),
                                  command=lambda: controller.show_frame(PredictionPage))
        predictButton.grid(column=0, row=0, padx=(0, 840), pady=(100, 70))

        historyButton = tk.Button(self, text="HISTORY", fg="#DDAA85", bg="Black", width=30, height=2, bd=0, activebackground="Black",
                                  activeforeground="#DDAA85", font=('Raleway', 10, 'bold'),
                                  command=lambda: controller.show_frame(HistoryPage))
        historyButton.grid(column=0, row=0, padx=(0, 840), pady=(300, 100))


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
        bg = Image.open("Pictures/GUI2.png")
        resizebg = bg.resize((1100,700), Image.ANTIALIAS)

        self.newbg = ImageTk.PhotoImage(resizebg)
        rectangle = tk.Canvas(self, width=1100, height=700, borderwidth=0, highlightthickness=0)
        rectangle.create_image(0, 0, image=self.newbg, anchor=NW)
        rectangle.create_text(130, 155, text="POME Prediction AI", fill="#DDAA85", font=('Raleway', 17, 'bold'))
        rectangle.create_text(370, 630, text="(ONLY .xlsx FILES)", fill="Black", font=('Raleway', 10))
        rectangle.grid(row=0, column=0)

        aboutButton = tk.Button(self, text="ABOUT", fg="#DDAA85", bg="Black", width=30, height=2, bd=0,font=('Raleway', 10, 'bold'), activebackground="Black",
                               activeforeground="#DDAA85", command=lambda: controller.show_frame(HomePage))
        aboutButton.grid(column=0, row=0, padx=(0, 840), pady=(0, 135))

        predictButton = tk.Button(self, text="PREDICT", fg="#DDAA85", bg="#4F3D2F", width=30, height=2, bd=0, font=('Raleway', 10, 'bold'),  activebackground="#4F3D2F",
                                  activeforeground="#DDAA85", command=lambda: controller.show_frame(PredictionPage))
        predictButton.grid(column=0, row=0, padx=(0, 840), pady=(100, 70))

        historyButton = tk.Button(self, text="HISTORY", fg="#DDAA85", bg="Black", width=30, height=2, bd=0, font=('Raleway', 10, 'bold'), activebackground="Black",
                                  activeforeground="#DDAA85", command=lambda: controller.show_frame(HistoryPage))
        historyButton.grid(column=0, row=0, padx=(0, 840), pady=(300, 100))

        input1 = tk.StringVar()
        input2 = tk.StringVar()
        input3 = tk.StringVar()
        input4 = tk.StringVar()
        input5 = tk.StringVar()
        input6 = tk.StringVar()
        input7 = tk.StringVar()
        input8 = tk.StringVar()
        input9 = tk.StringVar()
        input10 = tk.StringVar()
        input11 = tk.StringVar()
        input12 = tk.StringVar()
        input13 = tk.StringVar()
        input14 = tk.StringVar()
        input15 = tk.StringVar()
        input16 = tk.StringVar()

        def clear():
            input1.set("")
            input2.set("")
            input3.set("")
            input4.set("")
            input5.set("")
            input6.set("")
            input7.set("")
            input8.set("")
            input9.set("")
            input10.set("")
            input11.set("")
            input12.set("")
            input13.set("")
            input14.set("")
            input15.set("")
            input16.set("")

        input1 = tk.StringVar()
        input1Entered = tk.Entry(self, width=40, command=clear(), textvariable=input1)
        input1Entered.grid(column=0, row=0, padx=(0, 100), pady=(0, 400))

        input2Entered = tk.Entry(self, width=40, command=clear(), textvariable=input2)
        input2Entered.grid(column=0, row=0, padx=(0, 100), pady=(0, 300))

        input3 = tk.StringVar()
        input3Entered = tk.Entry(self, width=40, command=clear(), textvariable=input3)
        input3Entered.grid(column=0, row=0, padx=(0, 100), pady=(0, 200))

        input4 = tk.StringVar()
        input4Entered = tk.Entry(self, width=40, command=clear(), textvariable=input4)
        input4Entered.grid(column=0, row=0, padx=(0, 100), pady=(0, 100))

        input5 = tk.StringVar()
        input5Entered = tk.Entry(self, width=40, command=clear(), textvariable=input5)
        input5Entered.grid(column=0, row=0, padx=(0, 100), pady=(0, 0))

        input6 = tk.StringVar()
        input6Entered = tk.Entry(self, width=40, command=clear(), textvariable=input6)
        input6Entered.grid(column=0, row=0, padx=(0, 100), pady=(100, 0))

        input7 = tk.StringVar()
        input7Entered = tk.Entry(self, width=40, command=clear(), textvariable=input7)
        input7Entered.grid(column=0, row=0, padx=(0, 100), pady=(200, 0))

        input8 = tk.StringVar()
        input8Entered = tk.Entry(self, width=40, command=clear(), textvariable=input8)
        input8Entered.grid(column=0, row=0, padx=(0, 100), pady=(300, 0))

        input9 = tk.StringVar()
        input9Entered = tk.Entry(self, width=40, command=clear(), textvariable=input9)
        input9Entered.grid(column=0, row=0, padx=(700, 0), pady=(0, 400))

        input10 = tk.StringVar()
        input10Entered = tk.Entry(self, width=40,  command=clear(), textvariable=input10)
        input10Entered.grid(column=0, row=0, padx=(700, 0), pady=(0, 300))

        input11 = tk.StringVar()
        input11Entered = tk.Entry(self, width=40,  command=clear(), textvariable=input11)
        input11Entered.grid(column=0, row=0, padx=(700, 0), pady=(0, 200))

        input12 = tk.StringVar()
        input12Entered = tk.Entry(self, width=40,  command=clear(), textvariable=input12)
        input12Entered.grid(column=0, row=0, padx=(700, 0), pady=(0, 100))

        input13 = tk.StringVar()
        input13Entered = tk.Entry(self, width=40,  command=clear(), textvariable=input13)
        input13Entered.grid(column=0, row=0, padx=(700, 0), pady=(0, 0))

        input14 = tk.StringVar()
        input14Entered = tk.Entry(self, width=40,  command=clear(), textvariable=input14)
        input14Entered.grid(column=0, row=0, padx=(700, 0), pady=(100, 0))

        input15 = tk.StringVar()
        input15Entered = tk.Entry(self, width=40,  command=clear(), textvariable=input15)
        input15Entered.grid(column=0, row=0, padx=(700, 0), pady=(200, 0))

        input16 = tk.StringVar()
        input16Entered = tk.Entry(self, width=40, command=clear(), textvariable=input16)
        input16Entered.grid(column=0, row=0, padx=(700, 0), pady=(300, 0))

        importButton = tk.Button(self, text="IMPORT FILE", command=getExcel, fg="#4F3D2F", bg="white", width=10, height=1,bd=0)
        importButton.grid(column=0, row=0, padx=(10, 380), pady=(520, 20))

        doPredictionButton = tk.Button(self, text="DO PREDICTION", fg="#4F3D2F", bg="white", width=13, height=1, bd=0,
                                       command=lambda: controller.show_frame(OutputPage))
        doPredictionButton.grid(column=0, row=0, padx=(350, 80), pady=(520, 20))

        ClearButton = tk.Button(self, text="CLEAR ALL", fg="#4F3D2F", bg="white", width=13, height=1, bd=0,
                                command=lambda: clear())
        ClearButton.grid(column=0, row=0, padx=(850, 80), pady=(520, 20))


class HistoryPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Background image
        bg = Image.open("Pictures/GUI3.png")
        resizebg = bg.resize((1100, 700), Image.ANTIALIAS)

        self.newbg = ImageTk.PhotoImage(resizebg)
        rectangle = tk.Canvas(self, width=1100, height=700, borderwidth=0, highlightthickness=0)
        rectangle.create_image(0, 0, image=self.newbg, anchor=NW)
        rectangle.create_text(130, 155, text="POME Prediction AI", fill="#DDAA85", font=('Raleway', 17, 'bold'))
        rectangle.grid(row=0, column=0)

        aboutButton = tk.Button(self, text="ABOUT", fg="#DDAA85", bg="Black", width=30, height=2, bd=0,  activebackground="Black", activeforeground="#DDAA85",
                                font=('Raleway', 10, 'bold'),
                                command=lambda: controller.show_frame(HomePage))
        aboutButton.grid(column=0, row=0, padx=(0, 840), pady=(0, 135))

        predictButton = tk.Button(self, text="PREDICT",fg="#DDAA85", bg="Black", width=30, height=2, bd=0, activebackground="Black", activeforeground="#DDAA85",
                                  font=('Raleway', 10, 'bold'),
                                  command=lambda: controller.show_frame(PredictionPage))
        predictButton.grid(column=0, row=0, padx=(0, 840), pady=(100, 70))

        historyButton = tk.Button(self, text="HISTORY",fg="#DDAA85", bg="#4F3D2F", width=30, height=2, bd=0, activebackground="#4F3D2F", activeforeground="#DDAA85",
                                  font=('Raleway', 10, 'bold'),
                                  command=lambda: controller.show_frame(HistoryPage))
        historyButton.grid(column=0, row=0, padx=(0, 840), pady=(300, 100))


class OutputPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Background image
        bg = Image.open("Pictures/GUI2.png")
        resizebg = bg.resize((1100, 700), Image.ANTIALIAS)

        self.newbg = ImageTk.PhotoImage(resizebg)
        rectangle = tk.Canvas(self, width=1100, height=700, borderwidth=0, highlightthickness=0)
        rectangle.create_image(0, 0, image=self.newbg, anchor=NW)
        rectangle.create_text(195, 745, text="(ONLY .xlsx FILES)", fill="White", font=('Raleway', 10))
        rectangle.create_text(130, 155, text="POME Prediction AI", fill="#DDAA85", font=('Raleway', 17, 'bold'))
        rectangle.grid(row=0, column=0)

        aboutButton = tk.Button(self, text="ABOUT", fg="#DDAA85", bg="Black", width=30, height=2, bd=0,
                                font=('Raleway', 10, 'bold'), activebackground="Black",
                                activeforeground="#DDAA85", command=lambda: controller.show_frame(HomePage))
        aboutButton.grid(column=0, row=0, padx=(0, 840), pady=(0, 135))

        predictButton = tk.Button(self, text="PREDICT", fg="#DDAA85", bg="#4F3D2F", width=30, height=2, bd=0,
                                  font=('Raleway', 10, 'bold'), activebackground="#4F3D2F",
                                  activeforeground="#DDAA85", command=lambda: controller.show_frame(PredictionPage))
        predictButton.grid(column=0, row=0, padx=(0, 840), pady=(100, 70))

        historyButton = tk.Button(self, text="HISTORY", fg="#DDAA85", bg="Black", width=30, height=2, bd=0,
                                  font=('Raleway', 10, 'bold'), activebackground="Black",
                                  activeforeground="#DDAA85", command=lambda: controller.show_frame(HistoryPage))
        historyButton.grid(column=0, row=0, padx=(0, 840), pady=(300, 100))

        newDataButton = tk.Button(self, text="INPUT NEW DATA", fg="#4F3D2F", bg="white", width=17, height=1, bd=0)
        newDataButton.grid(column=0, row=0, padx=(10, 380), pady=(520, 20))

        downloadButton = tk.Button(self, text="DOWNLOAD OUTPUT", fg="#4F3D2F", bg="white", width=17, height=1, bd=0)
        downloadButton.grid(column=0, row=0, padx=(350, 80), pady=(520, 20))


app = tkinterApp()
app.mainloop()

