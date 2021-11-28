import tkinter as tk
from tkinter import ttk

window = tk.Tk()

loginLabel = tk.Label(
    window,
    text="LOGIN",
    fg="white",
    bg="grey",
    width=100,
    height=4,
).grid(column=0, row=0, pady=20, padx=150)

tk.Grid.rowconfigure(window, 0, weight=1)
tk.Grid.columnconfigure(window, 0, weight=1)

topLine = tk.Canvas(width=1000)
topLine.create_line(20, 5, 980, 5)
topLine.grid(row=1, column=0)

rectangle = tk.Canvas(width=1000)
rectangle.create_rectangle(50, 250, 350, 50)
rectangle.grid(row=1, column=0, padx=(300,0), pady=(100,0))

label = ttk.Label(window, text="Enter username")
label.grid(column=0, row=1, pady=(0, 0))

username = tk.StringVar()
nameEntered = ttk.Entry(window, width=30, textvariable=username)
nameEntered.grid(column=0, row=1, pady=(60, 0))

label = ttk.Label(window, text="Enter password")
label.grid(column=0, row=1, pady=(150, 0))

password = tk.StringVar()
nameEntered = ttk.Entry(window, width=30, textvariable=password, show="*")
nameEntered.grid(column=0, row=1, pady=(200, 0))

botLine = tk.Canvas(width=1000)
botLine.create_line(20, 5, 980, 5)
botLine.grid(row=3, column=0)


def main():
    window.title('Software')
    window.geometry("1000x750+300+300")
    window.mainloop()


if __name__ == '__main__':
    main()
