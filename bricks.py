from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

SIZES_BRICKS = [1,2]

class Bricks:
    
    def __init__(self):
        self.all_brick = []
        self.create_all_breacks()
    
    def create_all_breacks(self):
        y = 200
        
        for _ in range(1,5):
            x = -350
            acum = 0
            size_len_ant = 0
            while acum < 700:
                
                size_len = random.choice(SIZES_BRICKS)
                colors = random.choice(COLORS)
                
                if acum == 680 and size_len ==2 :
                    new_breacks = Turtle('square')
                    new_breacks.shapesize(stretch_wid=1, stretch_len=1)
                    new_breacks.penup()
                    variable=0
                elif x == 340:
                    new_breacks = Turtle('square')
                    new_breacks.shapesize(stretch_wid=1, stretch_len=1)
                    new_breacks.penup()
                    variable=0
                else:
                    new_breacks = Turtle('square')
                    new_breacks.shapesize(stretch_wid=1, stretch_len=size_len)
                    new_breacks.penup()
                    variable = 10 if (size_len == 2 and acum != 0) or (size_len_ant == 2 and acum != 0) else 0
                new_breacks.color(colors)
                new_breacks.goto(x + variable,y)
                acum += 20 + variable
                x += 20 + variable
                size_len_ant = size_len
                self.all_brick.append(new_breacks)
            y -= 21