from turtle import *

screensize(4000, 4000)
m = 15
tracer(False)

for i in range(6):
    fd(33*m)
    rt(90)
    fd(20*m)
    rt(90)

up()

fd(3*m)
rt(90)
fd(9*m)
lt(90)

down()

for i in range(6):
    fd(24*m)
    rt(90)
    fd(25*m)
    rt(90)

up()

for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x*m, y*m)
        dot(4, 'red')

print(10*23)
update()
done()