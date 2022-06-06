from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.b_list = []
        self.create_snake()
        self.head = self.b_list[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            b = Turtle()
            b.shape("square")
            b.color("white")
            b.penup()
            b.goto(x=position[0], y=position[1])
            self.b_list.append(b)

    def move(self):
        for number in range(len(self.b_list) - 1, 0, -1):
            new_x = self.b_list[number - 1].xcor()
            new_y = self.b_list[number - 1].ycor()
            self.b_list[number].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)