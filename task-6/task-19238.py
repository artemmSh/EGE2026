from turtle import *

screensize(4000, 4000)
m = 25
tracer(False)

for i in range(8):
    fd(16 * m)
    rt(90)
    fd(22 * m)
    rt(90)

up()

fd(5 * m)
rt(90)
fd(5 * m)
lt(90)

down()

for i in range(8):
    fd(52 * m)
    rt(90)
    fd(77 * m)
    rt(90)

up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(4, 'red')

print(11 * 17)

update()
done()
