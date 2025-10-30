from turtle import *
screensize(3000, 3000)
tracer(0)
m = 30
for i in range(2):
    fd(13*m)
    rt(90)
    fd(20*m)
    rt(90)
up()
fd(8*m)
rt(90)
bk(3*m)
lt(90)
down()
for i in range(2):
    fd(16*m)
    rt(90)
    fd(8*m)
    rt(90)

up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*m, y*m)
        dot(3, 'red')
print(14*21+17*9-6*6)
update()
done()