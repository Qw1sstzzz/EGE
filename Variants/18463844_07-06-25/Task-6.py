from turtle import *

lt(90)
down()

screensize(2500, 2500)
tracer(0)
m = 25

for i in range(9):
    fd(22*m)
    rt(90)
    fd(6*m)
    rt(90)

up()
fd(1*m)
rt(90)
fd(5*m)
lt(90)
down()

for i in range(9):
    fd(53*m)
    rt(90)
    fd(75*m)
    rt(90)

up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*m, y*m)
        dot(5, 'white')

update()
done()