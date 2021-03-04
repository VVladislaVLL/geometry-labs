from tkinter import *
# Тут можешь просто посмотреть как функция работатет
# Так как двигать можно только изображение, в метод draw_point я добавил,
# чтобы изображение сохранялось в отдельное свойство picture

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.picture = 0

    def print_point(self):
        print('(' + str(self.x) + ', ' + str(self.y) + ')')

    def draw_point(self, canvas, text, shift=-15):
        self.picture = canvas.create_oval(
            self.x - 2,
            self.y - 2,
            self.x + 2,
            self.y + 2,
            fill='black',
            outline='black'
        )

        canvas.create_text(
            self.x + shift,
            self.y + shift,
            text=(text + ' (' + str(self.x) + ', ' + str(self.y) + ')'),
            justify=constants.CENTER
        )

def motion():
    canvas.move(ball, 1, 0)
    if canvas.coords(ball)[2] < 300:
        root.after(10, motion)


root = Tk()
canvas = Canvas(root, width=500, height=500,
           bg="white")
canvas.pack()
ball = canvas.create_oval(0, 100, 40, 140,
                     fill='green')
motion()
root.mainloop()