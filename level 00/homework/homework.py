from turtle import *
speed(3)
width(7)

# sahlistvis kubi
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)

# saxlistvis saxuravi
penup()
goto(200, 200)
pendown()
right(135)
begin_fill()
forward(150)
left(96)
forward(150)
end_fill()
#  kari
penup()
goto(130, 0)
pendown()
color("brown")
begin_fill()
right(142)
forward(130)
left(90)
forward(50)
left(90)
forward(130) 
end_fill()
# panjara 1
penup()
goto(200, 150)
pendown()
color("aqua")
begin_fill()
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()
# panjara 2
penup()
goto(0, 150)
pendown()
color("aqua")
begin_fill()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()
exitonclick()