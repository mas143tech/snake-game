import turtle as s
POSITIONS=[(0,0),(-20,0),(-40,0)]


class Snake:

    def __init__(self,):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for n in POSITIONS:
            self.add_segment(n)

    def add_segment(self,positions):
        snake = s.Turtle()
        # snake.shapesize(0.2, 0.2)
        snake.shape("square")
        snake.color("red")
        snake.penup()
        snake.goto(positions)

        self.segments.append(snake)

    def move_up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)


    def move_down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)


    def move_left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)


    def move_right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)


    def move(self):
        for x in range(len(self.segments) - 1, 0, -1):
            self.add_segment(x)
        self.segments[0].forward(20)


    def and_segment(self,x):
        new_x = self.segments[x - 1].xcor()
        new_y = self.segments[x - 1].ycor()
        self.segments[x].goto(new_x, new_y)

    def extend(self):
       pass



