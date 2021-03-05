from task import task
from tkinter import Tk, Canvas, constants

if __name__ == '__main__':
    root = Tk()
    canvas = Canvas(root, width=1000, height=1000, bg="white", cursor="pencil")

    n = int(input("Введите количество углов: "))
    result = task(n, canvas)
    canvas.create_text(150, 100, text=result, justify=constants.CENTER)

    canvas.pack()
    root.mainloop()
