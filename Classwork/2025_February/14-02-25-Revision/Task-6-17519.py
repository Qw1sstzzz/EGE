from turtle import *

lt(90)
tracer(0)
screensize(2000, 2000)
m = 20

for i in range(9):
    fd(22*m)
    rt(90)
    fd(6*m)
    rt(90)

up()
fd(1 * m)
rt(90)
fd(5 * m)
lt(90)
down()

for i in range(9):
    fd(53*m)
    rt(90)
    fd(75*m)
    rt(90)

up()
for x in range(-20, 20):
    for y in range(-20, 30):
        goto(x * m,y * m)
        dot(5, 'white')

update()
done()