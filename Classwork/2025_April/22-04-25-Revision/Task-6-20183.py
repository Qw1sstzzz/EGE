from turtle import *

lt(90)
down()
screensize(2500, 2500)
tracer(0)
m = 20

for i in range(7):
    fd(9*m)
    rt(90)
    fd(16*m)
    rt(90)

up()
fd(3*m)
rt(90)
fd(4*m)
lt(90)
down()

for i in range(4):
    fd(7*m)
    rt(90)
    fd(13*m)
    rt(90)

up()

for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*m, y*m)
        dot(5, 'white')

update()
done()