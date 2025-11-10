from turtle import *

screensize(4000, 4000)
m = 30
tracer(False)

rt(90)
for i in range(7):
    rt(45)
    fd(11 * m)
    rt(45)

up()

for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x * m, y * m)
        dot(4, 'red')

print(15 + 2 * 13 + 2 * 11 + 2 * 9 + 2 * 7 + 2 * 5 + 2 * 3 + 2 * 1)

update()
done()
