from turtle import *

screensize(2500, 2500)
tracer(0)
m = 20
lt(90)
down()

for i in range(2):
    fd(28*m)
    rt(90)
    fd(18*m)
    rt(90)

up()
fd(14*m)
rt(90)
fd(10*m)
lt(90)
down()

for i in range(2):
    fd(30*m)
    rt(90)
    fd(7*m)
    rt(90)

up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*m, y*m)
        dot(5, 'darkred')

update()
done()

print(19*29 + 31*8 - 15*8)