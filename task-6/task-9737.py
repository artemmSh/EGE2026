from turtle import *

screensize(3000, 3000)
tracer(0)
m = 30

for i in range(2):
    forward(10 * m)
    right(90)
    forward(18 * m)
    right(90)
up()
forward(5 * m)
right(90)
forward(7 * m)
left(90)

down()

for i in range(2):
    forward(10 * m)
    right(90)
    forward(7 * m)
    right(90)

up()

for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * m, y * m)
        dot(3, 'red')
print(11 * 19 + 11 * 8 - 6 * 8)
update()
done()
