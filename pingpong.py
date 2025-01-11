import turtle
import winsound

wn= turtle.Screen()
wn.title("Pong by Agus")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#score
score_a = 0
score_b = 0

#game objects
#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape ("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#paddel B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape ("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball 1
ball1= turtle.Turtle()
ball1.speed(0)
ball1.shape ("square")
ball1.color("blue")
ball1.penup()
ball1.goto(0, 0)
ball1.dx = 2
ball1.dy = -2

#Ball2 (optional : add more balls)
ball2= turtle.Turtle()
ball2.speed(0)
ball2.shape ("square")
ball2.color("red")
ball2.penup()
ball2.goto(0, 0)
ball2.dx = -2
ball2.dy = -2

balls = [ball1 , ball2]

#pen (for scores)
pen= turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup() #to avoid line mooving
pen.hideturtle() #we only see text in this way
pen.goto(0 , 260)
pen.write("Player A: 0  Player B: 0" , align="center" , font=("Courier", 24, "normal"))

#functions
def paddle_a_up():
    y = paddle_a.ycor()
    y +=  20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -=  20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b. ycor()
    y +=  20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -=  20
    paddle_b.sety(y)

#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#main game loop
def game_loop():
    global score_a, score_b  # Declare the variables as global
    
    wn.update()
    for ball in balls:
        #move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
   
        #BORDER CHECKING
        #left and right
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            winsound.PlaySound("bounce.wav" , winsound.SND_ASYNC)

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            winsound.PlaySound("bounce.wav" , winsound.SND_ASYNC)

        #up and down
        if ball.xcor() > 390:
            ball.goto(0 , 0)
            ball.dx *= -1
            score_a += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b) , align="center" , font=("Courier", 24, "normal"))

        if ball.xcor() < -390:
            ball.goto(0 , 0)
            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b) , align="center" , font=("Courier", 24, "normal"))
    
        #paddle and ball collisions
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor () + 40 and ball.ycor() > paddle_b.ycor() -50):
            ball.setx(340)
            ball.dx *= -1
            winsound.PlaySound("bounce.wav" , winsound.SND_ASYNC)

        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor () + 40 and ball.ycor() > paddle_a.ycor() -50):
            ball.setx(-340)
            ball.dx *= -1
            winsound.PlaySound("bounce.wav" , winsound.SND_ASYNC) 

    #IA Player (movement logic) 
    #which one is the closest ball?
    closest_ball = balls[0]
    for ball in balls:
        if ball.xcor() > closest_ball.xcor():
            closest_ball = ball
    #after deciding that,the paddle will look for the closest ball
    if paddle_b.ycor() < closest_ball.ycor() and abs(paddle_b.ycor() - closest_ball.ycor()) > 10 :
            paddle_b_up()
    elif paddle_b.ycor() > closest_ball.ycor() and abs(paddle_b.ycor() - closest_ball.ycor()) > 10 :
            paddle_b_down()

    #Schedule the next vall to game_loop
    wn.ontimer (game_loop, 10)

#start the game loop
game_loop()

#start the event loop
wn.mainloop()