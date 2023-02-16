from turtle import *
import turtle as t

def draw_circle():
    color('red', 'yellow')
    begin_fill()

    while True:
        forward(100)
        left(335)
        print(abs(pos()))
        if abs(pos()) < 1:
            break

    end_fill()
    done()


def draw_line():
    t.Screen()
    t.setup(900, 800, 100, 200)
    t.bgcolor('SpringGreen')
    t.title('Show Turtle')
    t.shape('turtle')

    for pixel in range(30):
        print(pixel)
        t.forward(pixel)
    t.done()
    t.bye()

if __name__ == '__main__':
    draw_line()