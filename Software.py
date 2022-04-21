# GUI
import tkinter as tk
from tkinter import ttk, filedialog
from tkinter import *
import xlsxwriter
from PIL import Image, ImageTk
from datetime import datetime

# Sklearn
from sklearn.linear_model import LinearRegression  # for building LR model
from sklearn.multioutput import MultiOutputRegressor  # To make the output be independent to each other

# Data Manipulation
import pandas as pd  # for data manipulation
import numpy as np  # for data manipulation


class Software(tk.Tk):

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

        for F in (HomePage, PredictionPage, PredictionPage2):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

        # Get the data from excel to train the AI model
        global dataset
        dataset = pd.read_excel("Excel Data File/FinalData.xlsx")

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        self.title('POMEPAI')


class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Background image
        bg = Image.open("Pictures/GUI1.png")
        resizebg = bg.resize((1100, 700), Image.ANTIALIAS)

        self.newbg = ImageTk.PhotoImage(resizebg)
        rectangle = tk.Canvas(self, width=1100, height=700, borderwidth=0, highlightthickness=0)
        rectangle.create_image(0, 0, image=self.newbg, anchor=NW)
        rectangle.create_text(130, 155, text="POME Prediction AI", fill="#DDAA85", font=('Raleway', 17, 'bold'))
        rectangle.grid(row=0, column=0)

        aboutButton = tk.Button(self, text="ABOUT", fg="#DDAA85", bg="#4F3D2F", width=30, height=2, bd=0,
                                activebackground="#4F3D2F",
                                activeforeground="#DDAA85", font=('Raleway', 10, 'bold'),
                                command=lambda: controller.show_frame(HomePage))
        aboutButton.grid(column=0, row=0, padx=(0, 840), pady=(0, 135))

        predictButton = tk.Button(self, text="PREDICTION (SINGLE)", fg="#DDAA85", bg="Black", width=30, height=2, bd=0,
                                  activebackground="Black",
                                  activeforeground="#DDAA85", font=('Raleway', 10, 'bold'),
                                  command=lambda: controller.show_frame(PredictionPage))
        predictButton.grid(column=0, row=0, padx=(0, 840), pady=(100, 70))

        predictButton2 = tk.Button(self, text="PREDICTION (EXCEL)", fg="#DDAA85", bg="Black", width=30, height=2, bd=0,
                                   activebackground="Black", activeforeground="#DDAA85",
                                   font=('Raleway', 10, 'bold'),
                                   command=lambda: controller.show_frame(PredictionPage2))
        predictButton2.grid(column=0, row=0, padx=(0, 840), pady=(300, 100))


class PredictionPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Background image
        bg = Image.open("Pictures/GUI2.png")
        resizebg = bg.resize((1100, 700), Image.ANTIALIAS)

        self.newbg = ImageTk.PhotoImage(resizebg)
        rectangle = tk.Canvas(self, width=1100, height=700, borderwidth=0, highlightthickness=0)
        rectangle.create_image(0, 0, image=self.newbg, anchor=NW)
        rectangle.create_text(130, 155, text="POME Prediction AI", fill="#DDAA85", font=('Raleway', 17, 'bold'))
        rectangle.create_text(680, 100, text="Prediction For Single Point", fill="#DDAA85",
                              font=('Raleway', 17, 'bold'))
        rectangle.create_text(675, 450, text="Select Biogas For Prediction", fill="#4F3D2F",
                              font=('Raleway', 10, 'bold'))
        rectangle.grid(row=0, column=0)

        aboutButton = tk.Button(self, text="ABOUT", fg="#DDAA85", bg="Black", width=30, height=2, bd=0,
                                font=('Raleway', 10, 'bold'), activebackground="Black",
                                activeforeground="#DDAA85", command=lambda: controller.show_frame(HomePage))
        aboutButton.grid(column=0, row=0, padx=(0, 840), pady=(0, 135))

        predictButton = tk.Button(self, text="PREDICTION (SINGLE)", fg="#DDAA85", bg="#4F3D2F", width=30, height=2,
                                  bd=0, font=('Raleway', 10, 'bold'), activebackground="#4F3D2F",
                                  activeforeground="#DDAA85", command=lambda: controller.show_frame(PredictionPage))
        predictButton.grid(column=0, row=0, padx=(0, 840), pady=(100, 70))

        predictButton2 = tk.Button(self, text="PREDICTION (EXCEL)", fg="#DDAA85", bg="Black", width=30, height=2, bd=0,
                                   activebackground="Black", activeforeground="#DDAA85",
                                   font=('Raleway', 10, 'bold'),
                                   command=lambda: controller.show_frame(PredictionPage2))
        predictButton2.grid(column=0, row=0, padx=(0, 840), pady=(300, 100))

        input1 = tk.StringVar()
        input2 = tk.StringVar()
        input3 = tk.StringVar()
        input4 = tk.StringVar()
        input5 = tk.StringVar()

        # pH
        input1Entered = tk.Entry(self, width=30, textvariable=input1)
        input1Entered.grid(column=0, row=0, padx=(0, 265), pady=(0, 165))

        # COD1
        input2Entered = tk.Entry(self, width=30, textvariable=input2)
        input2Entered.grid(column=0, row=0, padx=(245, 0), pady=(0, 165))

        # BOD1
        input3Entered = tk.Entry(self, width=30, textvariable=input3)
        input3Entered.grid(column=0, row=0, padx=(765, 0), pady=(0, 165))

        # COD2
        input4Entered = tk.Entry(self, width=30, textvariable=input4)
        input4Entered.grid(column=0, row=0, padx=(30, 0), pady=(70, 0))

        # BOD2
        input5Entered = tk.Entry(self, width=30, textvariable=input5)
        input5Entered.grid(column=0, row=0, padx=(509, 0), pady=(70, 0))

        CH4Check = tk.IntVar()
        CO2Check = tk.IntVar()
        tk.Checkbutton(self, text='CH4', variable=CH4Check, bg="#E4BC9E",
                       activebackground="#E4BC9E").grid(column=0, row=0, padx=(150, 0), pady=(300, 0))
        tk.Checkbutton(self, text='CO2', variable=CO2Check, bg="#E4BC9E",
                       activebackground="#E4BC9E").grid(column=0, row=0, padx=(350, 0), pady=(300, 0))

        def validateCheckBox():
            if CO2Check.get() == 0 and CH4Check.get() == 0:
                error_Label = tk.Label(self, text='Invalid input', foreground='red')
                error_Label.grid(column=0, row=0, padx=(350, 90), pady=(580, 20))
                error_Label.after(3000, lambda: error_Label.destroy())
            else:
                predictSingleOutput(input1.get(),
                                    input2.get(), input4.get(), input3.get(),
                                    input5.get(),
                                    CH4Check.get(), CO2Check.get())

        def nonInteger():
            if (input1.get() == '' and input2.get() == '' and
                input3.get() == '' and input4.get() == '' and input5.get() == '') or (
                    input1.get().isalpha() or input2.get().isalpha() or
                    input3.get().isalpha() or input4.get().isalpha() or input5.get().isalpha()):
                error_Label = tk.Label(self, text='Invalid input', foreground='red')
                error_Label.grid(column=0, row=0, padx=(350, 90), pady=(580, 20))
                error_Label.after(3000, lambda: error_Label.destroy())

            else:
                validateCheckBox()

        doPredictionButton = tk.Button(self, text="DO PREDICTION", fg="#4F3D2F", bg="white", width=23, height=2, bd=0,
                                       command=lambda: nonInteger())
        doPredictionButton.grid(column=0, row=0, padx=(340, 80), pady=(520, 20))

        clearButton = tk.Button(self, text="CLEAR ALL", fg="#4F3D2F", bg="white", width=13, height=1, bd=0,
                                command=lambda: clear())
        clearButton.grid(column=0, row=0, padx=(850, 80), pady=(520, 20))

        def clear():
            input1.set("")
            input2.set("")
            input3.set("")
            input4.set("")
            input5.set("")
            CH4Check.set(0)
            CO2Check.set(0)

        def predictSingleOutput(ph_input, cod_input1, cod_input2, bod1_input,
                                bod2_input, ch4_input, co2_input):
            try:
                xInput = [[]]
                x = []
                y = []
                xInput = np.asarray(xInput)
                x = np.array(x)
                y = np.array(y)

                if ph_input != '':
                    xInput = np.concatenate((xInput, [[float(ph_input)]]), 1)
                    x = np.concatenate((x, ['pH Reactor']))
                if cod_input1 != '':
                    xInput = np.concatenate((xInput, [[float(cod_input1)]]), 1)
                    x = np.concatenate((x, ['COD F/mg/L']))
                if cod_input2 != '':
                    xInput = np.concatenate((xInput, [[float(cod_input2)]]), 1)
                    x = np.concatenate((x, ['COD Eff/mg/L']))
                if bod1_input != '':
                    xInput = np.concatenate((xInput, [[float(bod1_input)]]), 1)
                    x = np.concatenate((x, ['BOD F/mg/L']))
                if bod2_input != '':
                    xInput = np.concatenate((xInput, [[float(bod2_input)]]), 1)
                    x = np.concatenate((x, ['BOD Eff/mg/L']))

                if ch4_input == 1:
                    y = np.concatenate((y, ['CH4']))
                if co2_input == 1:
                    y = np.concatenate((y, ['CO2']))

                # Getting dataset to fit to Model
                xData = dataset[x].values
                yData = dataset[y].values

                # AI Model
                lr = LinearRegression()
                multiOutputLR = MultiOutputRegressor(lr)
                multiOutputLR = multiOutputLR.fit(xData, yData)

                y_pred = multiOutputLR.predict(xInput)
                xInput = np.around(xInput, 3)
                y_pred = np.around(y_pred, 3)

                dataHeadings = []
                dataXAndY = [[]]
                dataHeadings = np.array(dataHeadings)
                dataXAndY = np.array(dataXAndY)

                dataHeadings = np.concatenate((dataHeadings, y))
                dataHeadings = np.concatenate((dataHeadings, x))
                dataHeadingOnScreen = dataHeadings.tolist()
                dataXAndY = np.concatenate((dataXAndY, y_pred), 1)
                dataXAndY = np.concatenate((dataXAndY, xInput), 1)
                dataOnScreen = dataXAndY.tolist()
                dataHeadings = np.vstack((dataHeadings, dataXAndY))

                clear()

                def outputScreenSinglePrediction(headingsToDisplayOnScreen, dataToDisplayInFile, dataToDisplayOnScreen):
                    outputDisplaying = Tk()
                    outputDisplaying.title("OutputScreen")
                    outputDisplaying.resizable(0, 0)

                    def downloadExcelOutput():
                        dateAndTime = datetime.now()
                        dateAndTime = dateAndTime.strftime("%d-%m-%Y_%H.%M.%S")

                        filename = "OutputFiles/Output_" + dateAndTime + ".xlsx"
                        workbook = xlsxwriter.Workbook(filename)
                        worksheet = workbook.add_worksheet("Output")

                        col = 0

                        for row, dataInFile in enumerate(dataToDisplayInFile):
                            worksheet.write_row(row, col, dataInFile)

                        worksheet.set_column(0, (len(dataToDisplayInFile[0]) - 1), 12)

                        workbook.close()

                    tree_frame = Frame(outputDisplaying)
                    tree_frame.pack()

                    tree_scroll = Scrollbar(tree_frame)
                    tree_scroll.pack(side=RIGHT, fill=Y)

                    outputTree = ttk.Treeview(tree_frame, show='headings', height=8, yscrollcommand=tree_scroll.set,
                                              selectmode="none")
                    outputTree.pack()

                    tree_scroll.config(command=outputTree.yview)

                    outputTree['columns'] = headingsToDisplayOnScreen
                    outputTree.column("#0", width=0, stretch=False)
                    length = int(800 / len(headingsToDisplayOnScreen))

                    for i in headingsToDisplayOnScreen:
                        outputTree.column(i, anchor=CENTER, width=length, stretch=False)
                        outputTree.heading(i, text=i, anchor=CENTER)

                    count = 0
                    for data in dataToDisplayOnScreen:
                        outputTree.insert(parent='', index='end', iid=count, text="", values=data)
                        count += 1

                    ttk.Button(outputDisplaying, text='Download Output', command=lambda: downloadExcelOutput()).pack()

                    outputDisplaying.mainloop()

                outputScreenSinglePrediction(dataHeadingOnScreen, dataHeadings, dataOnScreen)

            except:
                error_Label = tk.Label(self, text='Input contain Alphabet', foreground='red')
                error_Label.grid(column=0, row=0, padx=(350, 90), pady=(580, 20))
                error_Label.after(3000, lambda: error_Label.destroy())


class PredictionPage2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def getExcel():
            filename = filedialog.askopenfilename(title="Open A File", filetypes=[('Excel Files', '*.xlsx')])
            filenameEntry.insert(0, filename)
            filenameEntry.config(text=filename)

            global df
            df = pd.read_excel(filename)

            box1.delete(0, END)

            for item in df.columns:
                box1.insert(END, item)

            file_label = tk.Label(self, text='File Uploaded Successfully!', foreground='green')
            file_label.grid(column=0, row=0, padx=(350, 90), pady=(580, 20))
            file_label.after(3000, lambda: file_label.destroy())

        # Background image
        bg = Image.open("Pictures/GUI3.png")
        resizebg = bg.resize((1100, 700), Image.ANTIALIAS)

        self.newbg = ImageTk.PhotoImage(resizebg)
        rectangle = tk.Canvas(self, width=1100, height=700, borderwidth=0, highlightthickness=0)
        rectangle.create_image(0, 0, image=self.newbg, anchor=NW)
        rectangle.create_text(130, 155, text="POME Prediction AI", fill="#DDAA85", font=('Raleway', 17, 'bold'))
        rectangle.create_text(680, 100, text="Prediction For Excel File", fill="#DDAA85", font=('Raleway', 17, 'bold'))
        rectangle.create_text(835, 165, text="(ONLY .xlsx FILES)", fill="Black", font=('Raleway', 10))
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

        predictButton2 = tk.Button(self, text="PREDICTION (EXCEL)", fg="#DDAA85", bg="#4F3D2F", width=30, height=2,
                                   bd=0,
                                   activebackground="#4F3D2F", activeforeground="#DDAA85",
                                   font=('Raleway', 10, 'bold'),
                                   command=lambda: controller.show_frame(PredictionPage2))
        predictButton2.grid(column=0, row=0, padx=(0, 840), pady=(300, 100))

        def clear():
            filenameEntry.delete(0, 'end')
            box1.delete(0, END)
            box2.delete(0, END)
            box3.delete(0, END)

        def clearX():
            box2.delete(0, END)

        def clearY():
            box3.delete(0, END)

        def getX():
            global x_v
            x_v = []
            s = box1.curselection()
            box2.delete(0, END)
            for i in s:
                data = box1.get(i)
                x_v.append(data)

            for data in x_v:
                box2.insert(END, data)

            box1.select_clear(0, END)

        def getY():
            global y_v
            y_v = []
            s = box1.curselection()
            box3.delete(0, END)
            for i in s:
                data = box1.get(i)
                y_v.append(data)

            for data in y_v:
                box3.insert(END, data)

            box1.select_clear(0, END)

        def setX():
            global x_v
            x_v = []

        def setY():
            global y_v
            y_v = []

        def validateListBox():
            try:
                if not x_v and not y_v:
                    error_Label = tk.Label(self, text='Invalid input', foreground='red')
                    error_Label.grid(column=0, row=0, padx=(350, 90), pady=(580, 20))
                    error_Label.after(3000, lambda: error_Label.destroy())
                else:
                    predictFileOutput()
            except:
                error_Label = tk.Label(self, text='Invalid input', foreground='red')
                error_Label.grid(column=0, row=0, padx=(350, 90), pady=(580, 20))
                error_Label.after(3000, lambda: error_Label.destroy())

        def predictFileOutput():
            try:

                # Getting dataset to fit to Model
                xData = dataset[x_v].values
                yData = dataset[y_v].values

                # Getting dataset to do prediction
                xInput = df[x_v].values

                # AI Model
                lr = LinearRegression()
                multiOutputLR = MultiOutputRegressor(lr)
                multiOutputLR = multiOutputLR.fit(xData, yData)

                y_pred = multiOutputLR.predict(xInput)
                xInput = np.around(xInput, 3)
                y_pred = np.around(y_pred, 3)

                fullData = np.concatenate((y_pred, xInput), axis=1)
                heading = np.concatenate((y_v, x_v))
                dataFiles = np.vstack((heading, fullData))
                headingScreen = heading.tolist()
                fullData = fullData.tolist()

                def outputScreenExcelPrediction(headingsToDisplayOnScreen, dataToDisplayInFile, dataToDisplayOnScreen):
                    setX()
                    setY()
                    clearX()
                    clearY()
                    outputDisplaying = Tk()
                    outputDisplaying.title("OutputScreen")
                    outputDisplaying.resizable(0, 0)

                    def downloadExcelOutput():
                        dateAndTime = datetime.now()
                        dateAndTime = dateAndTime.strftime("%d-%m-%Y_%H.%M.%S")

                        filename = "OutputFiles/Output_" + dateAndTime + ".xlsx"
                        workbook = xlsxwriter.Workbook(filename)
                        worksheet = workbook.add_worksheet("Output")

                        col = 0

                        for row, dataInFile in enumerate(dataToDisplayInFile):
                            worksheet.write_row(row, col, dataInFile)

                        worksheet.set_column(0, (len(dataToDisplayInFile[0]) - 1), 12)

                        workbook.close()

                    tree_frame = Frame(outputDisplaying)
                    tree_frame.pack()

                    tree_scroll = Scrollbar(tree_frame)
                    tree_scroll.pack(side=RIGHT, fill=Y)

                    outputTree = ttk.Treeview(tree_frame, show='headings', height=8, yscrollcommand=tree_scroll.set,
                                              selectmode="none")
                    outputTree.pack()

                    tree_scroll.config(command=outputTree.yview)

                    outputTree['columns'] = headingsToDisplayOnScreen
                    outputTree.column("#0", width=0, stretch=False)
                    length = int(800 / len(headingsToDisplayOnScreen))

                    for i in headingsToDisplayOnScreen:
                        outputTree.column(i, anchor=CENTER, width=length, stretch=False)
                        outputTree.heading(i, text=i, anchor=CENTER)

                    count = 0
                    for data in dataToDisplayOnScreen:
                        outputTree.insert(parent='', index='end', iid=count, text="", values=data)
                        count += 1

                    ttk.Button(outputDisplaying, text='Download Output', command=lambda: downloadExcelOutput()).pack()

                    outputDisplaying.mainloop()

                outputScreenExcelPrediction(headingScreen, dataFiles, fullData)

            except:
                error_Label = tk.Label(self, text='Input Feature is not available', foreground='red')
                error_Label.grid(column=0, row=0, padx=(350, 90), pady=(580, 20))
                error_Label.after(3000, lambda: error_Label.destroy())

        Button(self, text='Select X', activeforeground="white", activebackground="black", bd=0,
               command=lambda: getX()).grid(column=0, row=0, padx=(190, 0), pady=(300, 0))
        Button(self, text='Select Y', activeforeground="white", activebackground="black", bd=0,
               command=lambda: getY()).grid(column=0, row=0, padx=(500, 0), pady=(300, 0))
        Button(self, text='Remove X', activeforeground="white", activebackground="black", bd=0,
               command=lambda: clearX()).grid(column=0, row=0, padx=(320, 0), pady=(300, 0))
        Button(self, text='Remove Y', activeforeground="white", activebackground="black", bd=0,
               command=lambda: clearY()).grid(column=0, row=0, padx=(630, 0), pady=(300, 0))

        filenameEntry = Entry(self, text='', width=55)
        filenameEntry.grid(column=0, row=0, padx=(200, 70), pady=(0, 320))

        box1 = Listbox(self, height=15, width=25, selectmode='multiple', activestyle='none')
        box1.grid(row=0, column=0, padx=(0, 50), pady=(15, 0))

        box2 = Listbox(self, height=15, width=25)
        box2.grid(row=0, column=0, padx=(263, 0), pady=(15, 0))

        box3 = Listbox(self, height=15, width=25)
        box3.grid(row=0, column=0, padx=(575, 0), pady=(15, 0))

        doPredictionButton = tk.Button(self, text="DO PREDICTION", fg="#4F3D2F", bg="white", width=23, height=2, bd=0,
                                       command=lambda: validateListBox())
        doPredictionButton.grid(column=0, row=0, padx=(340, 80), pady=(520, 20))

        clearButton = tk.Button(self, text="CLEAR ALL", fg="#4F3D2F", bg="white", width=13, height=1, bd=0,
                                command=lambda: clear())
        clearButton.grid(column=0, row=0, padx=(850, 80), pady=(520, 20))

        importButton = tk.Button(self, text="IMPORT FILE", command=getExcel, fg="#4F3D2F", bg="white", width=10,
                                 height=1, bd=0)
        importButton.grid(column=0, row=0, padx=(575, 0), pady=(0, 320))


app = Software()
app.mainloop()
