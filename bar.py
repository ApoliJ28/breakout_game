from turtle import Turtle

class Bar(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=8)
        self.penup()
        self.goto(0,-200)
    
    def go_left(self):
        new_x = self.xcor() - 20
        if new_x > (-360 + 60):
            self.goto(new_x, self.ycor())
        else:
            print("limit x left")
    
    def go_right(self):
        new_x = self.xcor() + 20
        if new_x < (360 - 60):
            self.goto(new_x, self.ycor())
        else:
            print("limit x right")
