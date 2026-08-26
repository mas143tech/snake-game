import turtle as t

mas = t.Turtle()
screen = t.Screen()
mas.pensize(5)
mas.pencolor("red")

def move_up():
    mas.setheading(90)
    mas.forward(10)

def move_down():
    mas.setheading(270)
    mas.forward(10)

def move_left():
    mas.setheading(180)
    mas.forward(10)

def move_right():
    mas.setheading(0)
    mas.forward(10)
def clear():
    mas.clear()
    mas.penup()
    mas.home()
    mas.pendown()
screen.listen()

screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")
screen.onkeypress(clear, "q")
screen.exitonclick()
