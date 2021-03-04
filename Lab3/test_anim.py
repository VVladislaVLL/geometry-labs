from tkinter import *
# Тут можешь просто посмотреть как функция работатет
# Так как двигать можно только изображение, в метод draw_point я добавил,
# чтобы изображение сохранялось в отдельное свойство picture

def motion():
    c.move(ball, 1, 0)
    if c.coords(ball)[2] < 300:
        root.after(10, motion)


root = Tk()
c = Canvas(root, width=300, height=200,
           bg="white")
c.pack()
ball = c.create_oval(0, 100, 40, 140,
                     fill='green')
motion()
root.mainloop()