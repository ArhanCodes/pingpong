


#Function that will Draw Border

def drawborder():
    b=turtle.Turtle()
    b.ht()
    b.speed(0)
    b.up()
    b.goto(-390,290)
    b.down()
    b.pensize(8)
    for i in range(2):
          b.fd(775)
          b.rt(90)
          b.fd(575)
          b.rt(90)


 #Draw a Pong Ball
    

#Player A Drawing Function
def playerA():
    pA.speed(0)
    pA.shape("square")
    pA.shapesize(5,1)
    pA.up()
    pA.goto(-350,0)

def playerB():
    pB.speed(0)
    pB.shape("square")
    pB.shapesize(5,1)
    pB.up()
    pB .goto(350,0)



def move_upA():
    y=pA.ycor()
    y=y+50
    pA.sety(y)

def move_downA():
    y=pA.ycor()
    y=y-50
    pA.sety(y)


def move_upB():
    y=pB.ycor()
    y=y+50
    pB.sety(y)

def move_downB():
    y=pB.ycor()
    y=y-50
    pB.sety(y)



def pongball():
    ball.shape("circle")
    ball.color("red")
    ball.pu()
  




#Main Code




import os    
import turtle
s=turtle.Screen()
s.title("Pong Game")
s.setup(800,600)

drawborder()


pA=turtle.Turtle()
playerA()

pB=turtle.Turtle()
playerB()


s.listen()
s.onkey(move_upA,"a")
s.onkey(move_downA,"z")

s.onkey(move_upB,"b")
s.onkey(move_downB,"y")

ball=turtle.Turtle()
pongball()

ball.dx=3
ball.dy=3

pen=turtle.Turtle()
pen.up()
pen.speed(0)
pen.goto(0,250)
pen.ht()
pen.color("green")
pen.write("Score Player A: 0  Score Player B: 0 ",font=("Courier",13,"bold"), align="center")

score_a=0
score_b=0



try:
     while True:
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() - ball.dy)

        if ball.ycor()<-270:
            ball.sety(-270)
            ball.dy= ball.dy * -1

        if ball.xcor()>380:
            ball.setx(380)
            ball.dx= ball.dx* -1


            score_a=score_a+10
            pen.clear()
            pen.write("Player A:{},Player B:{}".format(score_a,score_b),font=("Courier",13,"bold"), align="center")


        

        if ball.ycor()>280:
            ball.sety(280)
            ball.dy= ball.dy* -1
        
        if ball.xcor()<-380:
            ball.setx(-380)
            ball.dx= ball.dy* -1

            score_b=score_b+10
            pen.clear()
            pen.write("Player A:{},Player B:{}".format(score_a,score_b),font=("Courier",13,"bold"), align="center")


        if (ball.xcor() <-330) and (ball.ycor()<pA.ycor()+50 and ball.ycor()>pA.ycor()-50):
            os.system("afplay Ball_Bounce.wav&")
            ball.setx(-330)
            ball.dx=ball.dx* -1

        if (ball.xcor() >330) and (ball.ycor()<pB.ycor()+50 and ball.ycor()>pB.ycor()-50):
            os.system("afplay Ball_Bounce.wav&")
            ball.setx(330)
            ball.dx=ball.dx* -1





except:
    print("Game Over")
    
 



