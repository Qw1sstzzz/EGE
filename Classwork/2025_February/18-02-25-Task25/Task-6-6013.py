from turtle import *

lt(90)
down()
screensize(2500, 2500)
m = 35
tracer(0)

for i in range(2):
    rt(120)
    fd(7*m)
rt(300)
for i in range(2):
    rt(120)
    fd(7*m)

up()

for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*m, y*m)
        dot(4, 'darkred')

update()
done()