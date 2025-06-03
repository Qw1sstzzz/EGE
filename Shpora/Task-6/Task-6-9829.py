from turtle import *

lt(90)
down()
screensize(2500, 2500)
m = 25
tracer(0)

rt(90)
for i in range(3):
    rt(45)
    fd(10*m)
    rt(45)

rt(315)
fd(10*m)

for i in range(2):
    rt(90)
    fd(10*m)

up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*m, y*m)
        dot(3, 'darkred')

update()
done()