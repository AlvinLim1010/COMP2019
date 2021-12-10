import tkinter as tk

window = tk.Tk()
window.overrideredirect(True)
window.title('Software')
window.geometry("1000x750")


def toLoginPage():
    window.destroy()
    import loginPage


def toHomePage():
    window.destroy()
    import homePage


def toHistoryPage():
    window.destroy()
    import historyPage


logOutLabel = tk.Button(window, text="LOG OUT", font=("Arial", 7), fg="white", bg="grey", width=10, height=2, command=toLoginPage)
logOutLabel.grid(column=0, row=0, padx=(900, 20), pady=(5, 700))

loginLabel = tk.Label(window, text="PREDICTION PAGE", fg="white", bg="grey", width=100, height=4)
loginLabel.grid(column=0, row=0, padx=(30, 30), pady=(20, 650))

tk.Grid.rowconfigure(window, 0, weight=1)
tk.Grid.columnconfigure(window, 0, weight=1)

rectangle = tk.Canvas(width=1000, height=750)
rectangle.create_rectangle(10, 70, 950, 20)
rectangle.create_rectangle(10, 565, 950, 95)
rectangle.create_rectangle(30, 505, 930, 115)
rectangle.grid(row=0, column=0, padx=(15, 15), pady=(80, 0))

homeButton = tk.Button(window, text="HOME", font=("Arial", 8), fg="white", bg="grey", width=23, height=2,
                       command=toHomePage)
homeButton.grid(column=0, row=0, padx=(10, 665), pady=(6, 506))

predictButton = tk.Button(window, text="PREDICT", font=("Arial", 8), fg="white", bg="grey", width=23, height=2)
predictButton.grid(column=0, row=0, padx=(110, 335), pady=(6, 506))

trainButton = tk.Button(window, text="TRAIN", font=("Arial", 8), fg="white", bg="grey", width=23, height=2)
trainButton.grid(column=0, row=0, padx=(335, 130), pady=(6, 506))

historyButton = tk.Button(window, text="HISTORY", font=("Arial", 8), fg="white", bg="grey", width=23, height=2,
                          command=toHistoryPage)
historyButton.grid(column=0, row=0, padx=(665, 30), pady=(6, 506))

window.mainloop()

