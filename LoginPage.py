from tkinter import *

window = Tk()

loginLabel = Label(
    window,
    text="LOGIN",
    fg="white",
    bg="grey",
    width=100,
    height=4,
).grid(column=0, row=0, pady=20, padx=150)

topLine = Canvas(width=1000)
topLine.create_line(20, 5, 980, 5)
topLine.grid(row=1, column=0)

botLine = Canvas(width=1000)
botLine.create_line(20, 5, 980, 5)
botLine.grid(row=3, column=0)


def main():
    window.title('Software')
    window.geometry("1000x750+300+300")
    window.mainloop()


if __name__ == '__main__':
    main()
