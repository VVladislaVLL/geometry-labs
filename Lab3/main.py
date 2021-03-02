from task import task
from tkinter import Tk, Canvas

if __name__ == '__main__':
    root = Tk()
    canv = Canvas(root, width=1000, height=1000, bg="white", cursor="pencil")
    task(canv)

    canv.pack()
    root.mainloop()

