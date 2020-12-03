import turtle

# import the screen 
wind = turtle.Screen()

# set a title to the screen
wind.title("Ping Pong")

# set the background properties
wind.bgcolor("black")
wind.setup(width= 800, height= 600)
wind.tracer(0) # prevent the window from refreshing automatically

#madrab1
madrab1 = turtle.Turtle()
madrab1.speed(0) # draw madrab1 on the screen with maximum speed
madrab1.shape("square")
madrab1.color("blue")
madrab1.shapesize(stretch_wid= 5, stretch_len= 0.5) #make madrab1 more wider
madrab1.penup()
madrab1.goto(-350, 0)  

#madrab2
madrab2 = turtle.Turtle()
madrab2.speed(0) # draw madrab2 on the screen with maximum speed
madrab2.shape("square")
madrab2.color("red")
madrab2.shapesize(stretch_wid= 5, stretch_len= 0.5) #make madrab2 more wider
madrab2.penup()
madrab2.goto(350, 0) 

#ball
ball = turtle.Turtle()
ball.speed(0) # draw the ball on the screen with maximum speed
ball.shape("circle") #set the shape of the ball
ball.color("white")  # set the color of ball
ball.shapesize(stretch_wid= 1, stretch_len= 1) #make the ball more wider
ball.penup() # prevents the object from drawing lines
ball.goto(0, 0) # set the position of the ball
ball.dx = 0.24
ball.dy = 0.24

#Score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("yellow")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Plyer1  {} : player2  {}  ".format(score1, score2), align="center", font=("Courier", 24, "normal"))

#Show the winner

result = turtle.Turtle()
result.speed(0)
result.color("yellow")
result.penup()
result.hideturtle()
result.goto(0,0)
#result._write("Player1 is the winner", align="center", font=("Courier", 24, "normal"))

#Functions

#Set vertical motion of madrab1
def madrab1_up():
    y = madrab1.ycor() # get the y coordinate of madrab1
    y += 20            # Set the y to increased by 20
    madrab1.sety(y)    # Set the y of madrab1 to the new y

def madrab1_down():
    y = madrab1.ycor() # get the y coordinate of madrab1
    y -= 20            # Set the y to decreased by 20
    madrab1.sety(y)    # Set the y of madrab1 to the new y

# Set vertical motion of madrab2
def madrab2_up():
    y = madrab2.ycor() # get the y coordinate of madrab2
    y += 20            # Set the y to increased by 20
    madrab2.sety(y)    # Set the y of madrab2 to the new y

def madrab2_down():
    y = madrab2.ycor() # get the y coordinate of madrab2
    y -= 20            # Set the y to decreased by 20
    madrab2.sety(y)    # Set the y of madrab2 to the new y

# quit the game
running = True
def qu():
    global running
    running = False


#Keyboard bindings
wind.listen()          # Tell the window to expect keyboard input
wind.onkeypress(madrab1_up, "w")
wind.onkeypress(madrab1_down, "x")
wind.onkeypress(madrab2_up, "Up")
wind.onkeypress(madrab2_down, "Down")
wind.onkeypress(qu, "q")

# game loop
while running:
    if score1 >= 5 and score1 - score2 >= 2:
        result._write("Player1 is the winner", align="center", font=("Courier", 24, "normal"))
        
    if score2 >= 5 and score2 - score1 >= 2:
        result._write("Player2 is the winner", align="center", font=("Courier", 24, "normal"))
        
    wind.update() # update the screen every begining of the game
     
    # move the ball
    ball.setx(ball.xcor() + ball.dx) #ball starts 0 and everytime loop runs----> +0.19 x_axix
    ball.sety(ball.ycor() + ball.dy) #ball starts 0 and everytime loop runs----> +0.19 y_axix
    
    #border check , top boarder +300px, bottom border -300px, ball is 20px
    if ball.ycor() > 290: # if ball is at top border
        ball.sety(290)    # set y at +290    
        ball.dy *= -1     # reverse direction, making +0.19 ----> -0.19

    if ball.ycor() < -290: # if ball is at bottom border
        ball.sety(-290)    # set y at -290 
        ball.dy *= -1      # reverse direction, making +0.19 ----> -0.19
    
    if ball.xcor() > 390: # if ball is at the right corner
        ball.goto(0, 0)   # return the ball at the center
        ball.dx *= -1     #reverse the ball direction
        score1 += 1       # player2 gain a point
        score.clear()
        score.write("Plyer1  {} : player2  {} ".format(score1, score2), align="center", font=("Courier", 24, "normal"))


    if ball.xcor() < -390: # if ball is at the left corner
        ball.goto(0, 0)
        ball.dx *= -1    
        score2 += 1       #player1 gains a point
        score.clear()
        score.write("Plyer1  {} : player2  {} ".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    
    #when the ball touches either madrab
    if (ball.xcor() > 345 and ball.xcor() < 350) and (ball.ycor() < madrab2.ycor() + 40 and ball.ycor() > madrab2.ycor() - 40):
        ball.setx(345)
        ball.dx *= -1

    if (ball.xcor() < -345 and ball.xcor() > -350) and (ball.ycor() < madrab1.ycor() + 40 and ball.ycor() > madrab1.ycor() - 40):
        ball.setx(-345)
        ball.dx *= -1    

wind.bye()      