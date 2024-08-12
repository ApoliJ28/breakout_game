from turtle import Screen
from bar import Bar
from info_bar import InfoBar
from ball import Ball
from bricks import Bricks
import time

# Interfaz
screen = Screen()
screen.bgcolor("black")
screen.setup(width=720, height=600)
screen.title("Breakout")
screen.tracer(0)

# Se agrega la barra a la pantalla
bar = Bar()
# Se agrega la barra de informacion
info_bar = InfoBar()
# Se agrega la pelota
ball = Ball()
# Se agrega los bloques
bricks = Bricks()

screen.listen()
# screen.onkey(bar.go_left, "Left")
# screen.onkey(bar.go_right, "Right")

screen.onkeypress(bar.go_left, "Left")
screen.onkeypress(bar.go_right, "Right")

while True:
    screen.update()
    ball.move()
    # time.sleep(ball.move_speed)
    
    # Detectar colision con las paredes laterales
    if ball.xcor() > 340 or ball.xcor() < -340:
        ball.bounce_x()
    
    # Dectectar colision con la parte superior:
    if ball.ycor() > 280:
        ball.bounce_y()
    
    # Detectar colision con la barra horizontal
    if ball.distance(bar) < 80 and ball.ycor() < -185:
        ball.bounce_y()
    
    # Deectar si choca con la parte inferior
    if ball.ycor() < -280:
        # Verificar vidas
        info_bar.lives -= 1
        info_bar.update_info()
        if info_bar.lives:
            ball.reset_position()
        else:
            info_bar.game_over()
            break
    # Detectar colision con uno de los ladrillos
    for brick in bricks.all_brick:
        if brick.distance(ball) < 25:
            info_bar.score += 10
            info_bar.update_info()
            ball.bounce_y()
            bricks.all_brick.remove(brick)
            brick.clear()
            brick.hideturtle()
    
    #Detectar que no haya quedado mas ladrillos
    if not bricks.all_brick:
        screen.update()
        info_bar.win()
        break
    
# Cerrar ventana con un click
screen.exitonclick()