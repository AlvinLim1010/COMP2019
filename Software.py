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

        for F in (HomePage, PredictionPage, PredictionPage2, HistoryPage, OutputPage):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(PredictionPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        self.title('POMEPAI')

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

        predictButton = tk.Button(self, text="PREDICTION (SINGLE)", fg="#DDAA85", bg="Black", width=30, height=2, bd=0, activebackground="Black",
                                  activeforeground="#DDAA85", font=('Raleway', 10, 'bold'),
                                  command=lambda: controller.show_frame(PredictionPage))
        predictButton.grid(column=0, row=0, padx=(0, 840), pady=(100, 70))

        predictButton2 = tk.Button(self, text="PREDICTION (EXCEL)", fg="#DDAA85", bg="Black", width=30, height=2, bd=0,
                                  activebackground="Black", activeforeground="#DDAA85",
                                  font=('Raleway', 10, 'bold'),
                                  command=lambda: controller.show_frame(PredictionPage2))
        predictButton2.grid(column=0, row=0, padx=(0, 840), pady=(300, 100))

        historyButton = tk.Button(self, text="HISTORY", fg="#DDAA85", bg="Black", width=30, height=2, bd=0,
                                  activebackground="#4F3D2F", activeforeground="BLACK",
                                  font=('Raleway', 10, 'bold'),
                                  command=lambda: controller.show_frame(HistoryPage))
        historyButton.grid(column=0, row=0, padx=(0, 840), pady=(460, 100))


class PredictionPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Background image
        bg = Image.open("Pictures/GUI2.png")
        resizebg = bg.resize((1100,700), Image.ANTIALIAS)

        self.newbg = ImageTk.PhotoImage(resizebg)
        rectangle = tk.Canvas(self, width=1100, height=700, borderwidth=0, highlightthickness=0)
        rectangle.create_image(0, 0, image=self.newbg, anchor=NW)
        rectangle.create_text(130, 155, text="POME Prediction AI", fill="#DDAA85", font=('Raleway', 17, 'bold'))
        rectangle.create_text(680, 100, text="Prediction For Single Point", fill="#DDAA85",font=('Raleway', 17, 'bold'))
        rectangle.create_text(675, 450, text="Select Biogas For Prediction", fill="#4F3D2F", font=('Raleway', 10, 'bold'))
        rectangle.grid(row=0, column=0)

        aboutButton = tk.Button(self, text="ABOUT", fg="#DDAA85", bg="Black", width=30, height=2, bd=0,font=('Raleway', 10, 'bold'), activebackground="Black",
                               activeforeground="#DDAA85", command=lambda: controller.show_frame(HomePage))
        aboutButton.grid(column=0, row=0, padx=(0, 840), pady=(0, 135))

        predictButton = tk.Button(self, text="PREDICTION (SINGLE)", fg="#DDAA85", bg="#4F3D2F", width=30, height=2, bd=0, font=('Raleway', 10, 'bold'),  activebackground="#4F3D2F",
                                  activeforeground="#DDAA85", command=lambda: controller.show_frame(PredictionPage))
        predictButton.grid(column=0, row=0, padx=(0, 840), pady=(100, 70))

        predictButton2 = tk.Button(self, text="PREDICTION (EXCEL)", fg="#DDAA85", bg="Black", width=30, height=2, bd=0,
                                   activebackground="Black", activeforeground="#DDAA85",
                                   font=('Raleway', 10, 'bold'),
                                   command=lambda: controller.show_frame(PredictionPage2))
        predictButton2.grid(column=0, row=0, padx=(0, 840), pady=(300, 100))

        historyButton = tk.Button(self, text="HISTORY", fg="#DDAA85", bg="Black", width=30, height=2, bd=0, font=('Raleway', 10, 'bold'), activebackground="Black",
                                  activeforeground="#DDAA85", command=lambda: controller.show_frame(HistoryPage))
        historyButton.grid(column=0, row=0, padx=(0, 840), pady=(460, 100))

        input1 = tk.StringVar()
        input2 = tk.StringVar()
        input3 = tk.StringVar()
        input4 = tk.StringVar()
        input5 = tk.StringVar()
        input6 = tk.StringVar()
        input7 = tk.StringVar()
        input8 = tk.StringVar()
        input9 = tk.StringVar()

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

        input1Entered = tk.Entry(self, width=30, command=clear(), textvariable=input1)
        input1Entered.grid(column=0, row=0, padx=(0,250), pady=(0, 250))

        input2Entered = tk.Entry(self, width=30, command=clear(), textvariable=input2)
        input2Entered.grid(column=0, row=0, padx=(0,250), pady=(0, 80))

        input3Entered = tk.Entry(self, width=30, command=clear(), textvariable=input3)
        input3Entered.grid(column=0, row=0, padx=(0,250), pady=(90, 0))

        input4Entered = tk.Entry(self, width=30, command=clear(), textvariable=input4)
        input4Entered.grid(column=0, row=0, padx=(260, 0), pady=(0, 250))

        input5Entered = tk.Entry(self, width=30, command=clear(), textvariable=input5)
        input5Entered.grid(column=0, row=0, padx=(260, 0), pady=(0, 80))

        input6Entered = tk.Entry(self, width=30, command=clear(), textvariable=input6)
        input6Entered.grid(column=0, row=0, padx=(260, 0), pady=(90, 0))

        input7Entered = tk.Entry(self, width=30, command=clear(), textvariable=input7)
        input7Entered.grid(column=0, row=0, padx=(780, 0), pady=(0, 250))

        input8Entered = tk.Entry(self, width=30, command=clear(), textvariable=input8)
        input8Entered.grid(column=0, row=0, padx=(780, 0), pady=(0, 80))

        input9Entered = tk.Entry(self, width=30, command=clear(), textvariable=input9)
        input9Entered.grid(column=0, row=0, padx=(780, 0), pady=(90, 0))

        CH4 = tk.Checkbutton(self, text='CH4', bg="#E4BC9E", activebackground="#E4BC9E").grid(column=0, row=0,padx=(150, 0),pady=(300, 0))
        CO2 = tk.Checkbutton(self, text='CO2', bg="#E4BC9E", activebackground="#E4BC9E").grid(column=0, row=0,padx=(250, 0),pady=(300, 0))
        H2S = tk.Checkbutton(self, text='H2S', bg="#E4BC9E", activebackground="#E4BC9E").grid(column=0, row=0,padx=(350, 0),pady=(300, 0))

        doPredictionButton = tk.Button(self, text="DO PREDICTION", fg="#4F3D2F", bg="white", width=23, height=2, bd=0,
                                       command=lambda: controller.show_frame(OutputPage))
        doPredictionButton.grid(column=0, row=0, padx=(340, 80), pady=(520, 20))

        clearButton = tk.Button(self, text="CLEAR ALL", fg="#4F3D2F", bg="white", width=13, height=1, bd=0,
                                command=lambda: clear())
        clearButton.grid(column=0, row=0, padx=(850, 80), pady=(520, 20))

class PredictionPage2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        listbox = Listbox(self, height=144, width=144, selectmode="multiple")
        listbox.pack

        def getExcel():

            file = askopenfile(filetypes=[('Excel Files', '*.xlsx')])
            inputExcelFile = load_workbook(filename=file.name)
            inputExcelFile2 = inputExcelFile.active

            features_row = inputExcelFile2[1]

            for item in features_row:
                box1.insert(END, item.value)

            file_label = tk.Label(self, text='File Uploaded Successfully!', foreground='green')
            file_label.grid(column=0, row=0, padx=(350, 80), pady=(580, 20))
            file_label.after(3000, lambda: file_label.destroy())

        # Background image
        bg = Image.open("Pictures/GUI3.png")
        resizebg = bg.resize((1100,700), Image.ANTIALIAS)

        # def data():
        #     global filename
        #     filename = askopenfilename(initialdir=r'C:\Users\surya\Desktop\CDAC Noida\ML\Files', title="Select file")
        #     e1.insert(0, filename)
        #     e1.config(text=filename)
        #
        #     global file
        #     file = pd.read_csv(filename)
        #     for i in file.columns:
        #         box1.insert(END, i)
        #
        #     for i in file.columns:
        #         if type(file[i][0]) == np.float64:
        #             file[i].fillna(file[i].mean(), inplace=True)
        #         elif type(file[i][0]) == np.int64:
        #             file[i].fillna(file[i].median(), inplace=True)
        #         elif type(file[i][0]) == type(""):
        #             imp = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
        #             s = imp.fit_transform(file[i].values.reshape(-1, 1))
        #             file[i] = s
        #
        #     colss = file.columns
        #     global X_Axis
        #     X_Axis = StringVar()
        #     X_Axis.set('X-axis')
        #     choose = ttk.Combobox(self, width=22, textvariable=X_Axis)
        #     choose['values'] = (tuple(colss))
        #     choose.place(x=400, y=20)
        #
        #     global Y_Axis
        #     Y_Axis = StringVar()
        #     Y_Axis.set('Y-axis')
        #     choose = ttk.Combobox(self, width=22, textvariable=Y_Axis)
        #
        #     choose['values'] = (tuple(colss))
        #     choose.place(x=400, y=40)
        #
        #     global graphtype
        #     graphtype = StringVar()
        #     graphtype.set('Graph')
        #     choose = ttk.Combobox(self, width=22, textvariable=graphtype)
        #     choose['values'] = ('scatter', 'line', 'bar', 'hist', 'corr', 'pie')
        #     choose.place(x=400, y=60)
        #
        # def getx():
        #     x_v = []
        #     s = box1.curselection()
        #     global feature_col
        #     for i in s:
        #         if i not in feature_col:
        #             feature_col.append((file.columns)[i])
        #             x_v = feature_col
        #     for i in x_v:
        #         box2.insert(END, i)
        #
        # def gety():
        #     y_v = []
        #     global target_col
        #     s = box1.curselection()
        #     for j in s:
        #         if j not in target_col:
        #             target_col.append((file.columns)[j])
        #             y_v = target_col
        #
        #     for i in y_v:
        #         box3.insert(END, i)

        self.newbg = ImageTk.PhotoImage(resizebg)
        rectangle = tk.Canvas(self, width=1100, height=700, borderwidth=0, highlightthickness=0)
        rectangle.create_image(0, 0, image=self.newbg, anchor=NW)
        rectangle.create_text(130, 155, text="POME Prediction AI", fill="#DDAA85", font=('Raleway', 17, 'bold'))
        rectangle.create_text(680, 100, text="Prediction For Excel File", fill="#DDAA85", font=('Raleway', 17, 'bold'))
        rectangle.create_text(835, 190, text="(ONLY .xlsx FILES)", fill="Black", font=('Raleway', 10))
        rectangle.grid(row=0, column=0)

        aboutButton = tk.Button(self, text="ABOUT", fg="#DDAA85", bg="Black", width=30, height=2, bd=0,
                                activebackground="Black", activeforeground="#DDAA85",
                                font=('Raleway', 10, 'bold'),
                                command=lambda: controller.show_frame(HomePage))
        aboutButton.grid(column=0, row=0, padx=(0, 840), pady=(0, 135))

        predictButton = tk.Button(self, text="PREDICTION (SINGLE)", fg="#DDAA85", bg="Black", width=30, height=2, bd=0,
                                  activebackground="Black", activeforeground="#DDAA85",
                                  font=('Raleway', 10, 'bold'),
                                  command=lambda: controller.show_frame(PredictionPage))
        predictButton.grid(column=0, row=0, padx=(0, 840), pady=(100, 70))

        predictButton2 = tk.Button(self, text="PREDICTION (EXCEL)",  fg="#DDAA85", bg="#4F3D2F", width=30, height=2, bd=0,
                                  activebackground="#4F3D2F", activeforeground="#DDAA85",
                                  font=('Raleway', 10, 'bold'),
                                  command=lambda: controller.show_frame(PredictionPage2))
        predictButton2.grid(column=0, row=0, padx=(0, 840), pady=(300, 100))

        historyButton = tk.Button(self, text="HISTORY", fg="#DDAA85", bg="Black", width=30, height=2, bd=0,
                                  activebackground="Black", activeforeground="#DDAA85",
                                  font=('Raleway', 10, 'bold'),
                                  command=lambda: controller.show_frame(HistoryPage))
        historyButton.grid(column=0, row=0, padx=(0, 840), pady=(460, 100))

        # listbox = Listbox(root, height=100, width=100)
        # listbox.pack(pady=20)

        listbox = Listbox(self, height=144, width=144, selectmode="multiple")
        listbox.pack

        e1 = Entry(self, text='')
        e1.grid(column=0, row=0, padx=(260,0), pady=(0, 270))  # test file path

        box1 = Listbox(self, height=15, width=25, selectmode='multiple')
        box1.grid(row=0, column=0, padx=(0, 50), pady=(15, 0))

        box2 = Listbox(self, height=15, width=25)
        box2.grid(row=0, column=0, padx=(263, 0), pady=(15, 0))

        Button(self, text='Select X', activeforeground="white", activebackground="black", bd=0).grid(column=0, row=0,
                                                                                                     padx=(157, 0),
                                                                                                     pady=(300, 0))

        box3 = Listbox(self, height=15, width=25)
        box3.grid(row=0, column=0, padx=(575, 0), pady=(15, 0))
        Button(self, text='Select Y', activeforeground="white", activebackground="black", bd=0).grid(column=0, row=0,
                                                                                                     padx=(370, 0),
                                                                                                     pady=(300, 0))
        # self.mainloop()

        doPredictionButton = tk.Button(self, text="DO PREDICTION", fg="#4F3D2F", bg="white", width=23, height=2, bd=0,
                                       command=lambda: controller.show_frame(OutputPage))
        doPredictionButton.grid(column=0, row=0, padx=(340, 80), pady=(520, 20))

        importButton = tk.Button(self, text="IMPORT FILE", command=getExcel, fg="#4F3D2F", bg="white", width=10, height=1,bd=0)
        importButton.grid(column=0, row=0, padx=(575,0),pady=(0,270))

class HistoryPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Background image
        bg = Image.open("Pictures/GUI4.png")
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

        predictButton = tk.Button(self, text="PREDICTION (SINGLE)",fg="#DDAA85", bg="Black", width=30, height=2, bd=0, activebackground="Black", activeforeground="#DDAA85",
                                  font=('Raleway', 10, 'bold'),
                                  command=lambda: controller.show_frame(PredictionPage))
        predictButton.grid(column=0, row=0, padx=(0, 840), pady=(100, 70))

        predictButton2 = tk.Button(self, text="PREDICTION (EXCEL)", fg="#DDAA85", bg="Black", width=30, height=2, bd=0,
                                  activebackground="Black", activeforeground="#DDAA85",
                                  font=('Raleway', 10, 'bold'),
                                  command=lambda: controller.show_frame(PredictionPage2))
        predictButton2.grid(column=0, row=0, padx=(0, 840), pady=(300, 100))

        historyButton = tk.Button(self, text="HISTORY", fg="#DDAA85", bg="#4F3D2F", width=30, height=2, bd=0,
                                  activebackground="#4F3D2F", activeforeground="#DDAA85",
                                  font=('Raleway', 10, 'bold'),
                                  command=lambda: controller.show_frame(HistoryPage))
        historyButton.grid(column=0, row=0, padx=(0, 840), pady=(460, 100))


class OutputPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Background image
        bg = Image.open("Pictures/GUI5.png")
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

        predictButton = tk.Button(self, text="PREDICTION (SINGLE)", fg="#DDAA85", bg="Black", width=30, height=2, bd=0,
                                font=('Raleway', 10, 'bold'), activebackground="#4F3D2F",
                                  activeforeground="#DDAA85", command=lambda: controller.show_frame(PredictionPage))
        predictButton.grid(column=0, row=0, padx=(0, 840), pady=(100, 70))

        predictButton2 = tk.Button(self, text="PREDICTION (EXCEL)", fg="#DDAA85", bg="Black", width=30, height=2, bd=0,
                                  activebackground="Black", activeforeground="#DDAA85",
                                  font=('Raleway', 10, 'bold'),
                                  command=lambda: controller.show_frame(PredictionPage2))
        predictButton2.grid(column=0, row=0, padx=(0, 840), pady=(300, 100))

        historyButton = tk.Button(self, text="HISTORY", fg="#DDAA85", bg="Black", width=30, height=2, bd=0,
                                  activebackground="#4F3D2F", activeforeground="BLACK",
                                  font=('Raleway', 10, 'bold'),
                                  command=lambda: controller.show_frame(HistoryPage))
        historyButton.grid(column=0, row=0, padx=(0, 840), pady=(460, 100))

        newDataButton = tk.Button(self, text="INPUT NEW DATA", fg="#4F3D2F", bg="white", width=17, height=1, bd=0)
        newDataButton.grid(column=0, row=0, padx=(10, 380), pady=(520, 20))

        downloadButton = tk.Button(self, text="DOWNLOAD OUTPUT", fg="#4F3D2F", bg="white", width=17, height=1, bd=0)
        downloadButton.grid(column=0, row=0, padx=(350, 80), pady=(520, 20))

app = tkinterApp()
app.mainloop()

