from turtle import *

screensize(3000, 3000)
m = 30
tracer(False)

for i in range(4):
    fd(10 * m)
    rt(270)
up()
fd(3 * m)
rt(270)
fd(5 * m)
rt(90)
down()
for i in range(2):
    fd(10 * m)
    rt(270)
    fd(12 * m)
    rt(270)

up()

for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * m, y * m)
        dot(4, 'dark blue')

print(11 * 11 + 11 * 13 - 6 * 8)

update()
done()
