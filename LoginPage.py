from tkinter import *
import Lines as Lines

window = Tk()

loginLabel = Label(
    window,
    text="LOGIN",
    fg="white",
    bg="grey",
    width=100,
    height=4,
)

loginLabel.grid(column=5, row=3)


def main():
    loginLabel.pack()
    window.title('Software')
    window.geometry("1000x750+300+300")
    Lines.Lines()
    window.mainloop()


if __name__ == '__main__':
    main()
