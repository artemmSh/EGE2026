from turtle import *

screensize(4000, 4000)
m = 50
tracer(False)

rt(30)
for i in range(3):
    rt(150)
    fd(6 * m)
    rt(30)
    fd(12 * m)

up()

for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * m, y * m)
        dot(4, 'red')

print(30)

update()
done()
