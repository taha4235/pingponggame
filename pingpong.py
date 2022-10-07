from tkinter import CENTER
import turtle
wind = turtle.Screen()
wind.title("ping pong game")
wind.bgcolor("black")
wind.setup(width=800,height=600)
wind.tracer(0)
score1=1
score2 = 1
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
ping1 = turtle.Turtle()
ping1.speed(0)
ping1.shape("square")
ping1.color("blue")
ping1.shapesize(stretch_wid=5,stretch_len=1)
ping1.penup()
ping1.goto(-350,0)
#ping2
ping2 = turtle.Turtle()
ping2.speed(0)
ping2.shape("square")
ping2.color("red")
ping2.shapesize(stretch_wid=5,stretch_len=1)
ping2.penup()
ping2.goto(350,0)
#ping3
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.5
ball.dy = -0.5
def ping1_up():
    y = ping1.ycor()
    y += 20
    ping1.sety(y)
def ping1_down():
    y = ping1.ycor()
    y -= 20
    ping1.sety(y)
#ping2
def ping2_up():
    y = ping2.ycor()
    y += 20
    ping2.sety(y)
def ping2_down():
    y = ping2.ycor()
    y -= 20
    ping2.sety(y)
#keyboard binding
#keyboard binding
wind.listen()#tell the window to expext the input
wind.onkeypress(ping1_up,"w")#when i click in the w ping1 has been moved
wind.onkeypress(ping1_down,"s")
wind.onkeypress(ping2_up,"u")
wind.onkeypress(ping2_down,"j")
while True:
     wind.update()
     ball.setx(ball.xcor()+ball.dx)
     ball.sety(ball.ycor()+ball.dy)
     if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
     if ball.ycor() <- 290:
        ball.sety(-290)
        ball.dy *= -1
     if ball.xcor() >390:
        ball.goto(0,0)
        ball.dx *= -1
     if ball.xcor() <-390:
        ball.goto(0,0)
        ball.dx *= -1
     if (ball.xcor()>340 and ball.xcor()<350 and ball.ycor()<ping2.ycor()+40 and ball.ycor()>ping2.ycor()-40):
        ball.setx(340)
        ball.dx*= -1
        score+=1
        score.clear()
        score.write("player 1 : {} player 2 : {}".format(score1,score2),align=CENTER,font=30)
     if (ball.xcor()>-340 and ball.xcor()<-350 and ball.ycor()<ping2.ycor()-40 and ball.ycor()>ping2.ycor()-40):
        ball.setx(-340)
        ball.dx*= -1
        score+=1
        score.write("player 1 : {} player 2 : {}".format(score1,score2),align=CENTER,font=30)
  