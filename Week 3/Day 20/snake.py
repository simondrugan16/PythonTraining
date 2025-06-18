from turtle import Turtle, Screen
from scoreboard import Scoreboard
from food import Food

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self) -> None:
        self.positions = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = self.make_segments()
        self.head: Turtle = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def make_segment(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        last_segment_direction = self.segments[-1].heading()
        last_segment_position = self.segments[-1].pos()
        new_segment.seth(last_segment_direction)
        new_segment.goto(last_segment_position)
        new_segment.forward(-20)
        self.segments.append(new_segment)

    def make_segments(self):
        segments = []
        positions = [(0, 0), (-20, 0), (-40, 0)]
        for pos in positions:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(pos)
            segments.append(segment)
        self.segments = segments
        return segments
    
    def check_eat(self, food: Food, scoreboard: Scoreboard):
        snake_head_location = self.head.pos()
        food_location = food.food.pos()

        if (snake_head_location[0] - 10) < food_location[0] < (snake_head_location[0] + 10) and (snake_head_location[1] - 10) < food_location[1] < (snake_head_location[1] + 10):
            scoreboard.gain_point()
            scoreboard.print_score()
            food.new_food_position(self.head)
            self.make_segment()

    def check_collision(self, scoreboard: Scoreboard, screen: Screen,):
        snake_head_location = self.head.pos()
        if (snake_head_location[0] >= 300 or snake_head_location[0] <= -300 or
            snake_head_location[1] >= 300 or snake_head_location[1] <= -300):
            screen.clearscreen()
            scoreboard.print_final_score()
            return True         
        else:
            for i in range(1, len(self.segments)):
                segment_location = self.segments[i].pos()
                if ((snake_head_location[0] - 10) < segment_location[0] < (snake_head_location[0] + 10) and
                    (snake_head_location[1] - 10) < segment_location[1] < (snake_head_location[1] + 10)):
                    scoreboard.print_final_score()
                    return True
            return False




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