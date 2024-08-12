from turtle import Turtle

FONT = ("Courier", 25, "normal")

class InfoBar(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.lives = 3
        self.score = 0
        self.update_info()
    
    def update_info(self):
        self.clear()
        self.goto(-230, 250)
        self.write(f"Lives: {self.lives}", align="center", font=FONT)
        self.goto(230, 250)
        self.write(f"Score: {self.score}", align="center", font=FONT)
    
    def lost_life(self):
        self.lives -= 1
        self.update_info()
    
    def upload_score(self):
        self.score += 1
        self.update_info()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)
    
    def win(self):
        self.goto(0,0)
        self.write("YOU WIN", align="center", font=FONT)