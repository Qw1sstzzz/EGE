from turtle import *

lt(90)
m = 25
screensize(3500, 3500)
tracer(0)

up()
for i in range(10):
    rt(120)
    fd(10*m)

down()
for i in range(7):
    fd(15*m)
    rt(90)
for i in range(5):
    rt(60)
    fd(20*m)
    rt(30)

up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*m, y*m)
        dot(3, 'darkred')

update()
done()
