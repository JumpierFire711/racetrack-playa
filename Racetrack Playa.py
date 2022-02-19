import turtle
import random
t=turtle.Pen()
u=turtle.Pen()
v=turtle.Pen()
w=turtle.Pen()
x=turtle.Pen()
lwt=[0.5, 0.5, 0.5, 0.5, 0.5]
direction = 0
turtle.bgcolor("black")
turtles = [t,u,v,w,x]
colors = ["red", "green", "blue", "yellow", "white"]
for i in range(0,4):
    turtles[i].pencolor("white")
    turtles[i].fillcolor(colors[i])
    turtles[i].speed(0)
    turtles[i].rt(90)
    turtles[i].pu()
    turtles[i].fd(300)
    turtles[i].lt(90)
    turtles[i].pd()
    turtles[i].circle(300)
    turtles[i].speed(2)
    turtles[i].pu()
    turtles[i].sety(0)
    turtles[i].pd()
    turtles[i].seth(225)

for i in range(0,999):
    turtles[i % 5].fd(6)
    if random.random()<lwt[i % 5]:
        turtles[i % 5].lt(random.randint(0,50))
    elif random.random()>lwt[i % 5]:
            turtles[i % 5].rt(random.randint(0,50))

    direction = turtles[i % 5].heading()

    if direction > 270:
        lwt[i % 5] -= (direction - 270)/360
    elif direction < 180:
        lwt[i % 5] += (180 - direction)/360
    else:
        lwt[i % 5] = 0.5
