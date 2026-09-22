# import turtle
#
# def turtle_square(t, side):
#     for i in range(4):
#         t.forward(side)
#         t.left(90)
#
# turtle.screensize(500, 500)
# t = turtle.Turtle()
# t.speed(1)
# t.shape('turtle')
# t.width(3)
#
# turtle_square(t, 100)
# t.pu()
# t.fd(200)
# t.pd()
# turtle_square(t, 100)
#
# turtle.done()

# import turtle
# t = turtle.Turtle()
# wid = 20
# t.width(wid)
# t.speed(0)
#
# colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# R = 200
#
# t.pu()
# t.goto(-R, 0)
# t.pd()
#
# for color in colors:
#     t.color(color)
#     step = 3.14 * R / 180
#     t.left(90)
#     for i in range(180):
#         t.fd(step)
#         t.rt(1)
#     t.rt(90)
#     t.pu()
#     t.fd(2 * R - wid)
#     t.pd()
#     t.rt(180)
#     R -= wid
#
# turtle.done()

import turtle

def coh_line(t, l, n):
    if n == 0:
        t.fd(l)
        return
    coh_line(t, l / 3, n - 1)
    t.left(60)
    coh_line(t, l/ 3, n - 1)
    t.right(120)
    coh_line(t, l / 3, n - 1)
    t.left(60)
    coh_line(t, l / 3, n - 1)

n = 5
l = 300
t = turtle.Turtle()
t.speed(0)

for i in range(3):
    coh_line(t, l, n)
    t.rt(120)

turtle.done()







