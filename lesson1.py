from turtle import *

#we want to paint a house

#step 1: draw a square

width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

color("brown")
begin_fill()
penup()
goto(0, 120)
pendown()
left(120)
forward(70)
left(90)
forward(80)
left(90)
forward(70)
left(90)
forward(80)
end_fill()

color("brown")
begin_fill()
penup()
left(90)
forward(130)
pendown()
forward(70)
left(90)
forward(80)
left(90)
forward(70)
left(90)
forward(80)
end_fill()






exitonclick()