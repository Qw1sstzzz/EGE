from turtle import *

lt(90)
down()
m = 25
screensize(3000, 3000)
tracer(0)

for i in range(15):
    fd(4*m)
    rt(60)

up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*m, y*m)
        dot(5, 'darkred')
up()
goto(0*m, 0*m)
rt(180)
down()
fd(15*m)
goto(0*m, 0*m)
rt(90)
fd(15*m)

update()
done()