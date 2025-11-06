from turtle import *

screensize(4000, 4000)
m = 30
tracer(False)

rt(270)

for i in range(2):
    fd(8 * m)
    rt(120)

rt(120)

for i in range(2):
    rt(120)
    fd(3 * m)
    rt(240)

rt(240)

for i in range(2):
    fd(14 * m)
    rt(120)

up()

for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * m, y * m)
        dot(4, 'red')

print(14 * 12 / 2)

update()
done()
