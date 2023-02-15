import turtle as trtl


# draw background
trtl.pensize(5)
trtl.fillcolor("green")
trtl.penup()
trtl.goto(-150, -100)
trtl.pendown()
trtl.setheading(-45)
trtl.begin_fill()
trtl.circle(200, 360, 4)
trtl.end_fill()
trtl.penup()


# draw top left apple
topleft = trtl.Turtle("circle")
topleft.fillcolor("red")
topleft.penup()
topleft.goto(-93, 130)


# draw top right apple
topright = trtl.Turtle("circle")
topright.fillcolor("red")
topright.penup()
topright.goto(80, 130)


# draw center apple
center = trtl.Turtle("circle")
center.fillcolor("red")
center.penup()
center.goto(-10, 40)


# draw bottom left apple
bottomleft = trtl.Turtle("circle")
bottomleft.fillcolor("red")
bottomleft.penup()
bottomleft.goto(-94, -52)


# draw bottom right apple
bottomright = trtl.Turtle("circle")
bottomright.fillcolor("red")
bottomright.penup()
bottomright.goto(80, -52)


# create snake
trtl_body = []
trtl.goto(-80, 40)
trtl.setheading(0)
trtl.turtlesize(2)
trtl.fillcolor("lime")
trtl.pencolor("black")


# first question
answer1 = input("What is 9 - 8?")
if(answer1 == "1"):


   # move snake to center
   for step in range(80):
       trtl.forward(1)
  
   # eat center apple
   center.hideturtle()
  
   # add first body segment
   body1 = trtl.Turtle()
   trtl_body.append(body1)
   body1.turtlesize(2)
   body1.fillcolor("lime")
   body1.penup()
   body1.goto(trtl.xcor() - 10, trtl.ycor())


   # print result
   print("Correct!")


else:
   # move snake to border
   trtl.setheading(180)
   for step in range(70):
       trtl.forward(1)
   trtl.fillcolor("red")


   # print result
   print("Game over!")
   exit()


# second question
answer2 = input("Is the current year 2023? y/n")
if(answer2 == "y"):


   # move snake to top right
   for step in  range(40):
       trtl.forward(2)
       body1.forward(2)
   trtl.left(90)
   for step in range(5):
       trtl.forward(2)
       body1.forward(2)
   body1.left(90)
   for step in range(45):
       trtl.forward(2)
       body1.forward(2)
  
   # eat top right apple
   topright.hideturtle()


   # add second body segment
   body2 = trtl.Turtle()
   trtl_body.append(body2)
   body2.turtlesize(2)
   body2.fillcolor("lime")
   body2.setheading(90)
   body2.penup()
   body2.goto(body1.xcor(), body1.ycor() - 10)


   # print result
   print("Correct!")


else:
   # move snake to border
   for step in range(68):
       trtl.forward(2)
       body1.forward(2)
   trtl.fillcolor("red")
   body1.fillcolor("red")


   # print result
   print("Game over!")
   exit()


# thrid question
answer3 = input("What is 70 divided by 7?")
if(answer3 == "10"):


   # move snake to top left
   trtl.left(90)
   for step in range(10):
       trtl.forward(2)
       body1.forward(1)
   body1.left(90)
   for step in range(10):
       body1.forward(1)
       body2.forward(2)
   body2.left(90)
   for step in range (52):
       trtl.forward(3)
       body1.forward(3)
       body2.forward(3)
  
   # eat top left apple
   topleft.hideturtle()


   # add third body segment
   body3 = trtl.Turtle()
   trtl_body.append(body3)
   body3.turtlesize(2)
   body3.fillcolor("lime")
   body3.setheading(180)
   body3.penup()
   body3.goto(body2.xcor() + 10, body2.ycor())


   # print result
   print("Correct!")


else:
   # move snake to border
   for step in range(15):
       trtl.forward(3)
       body1.forward(3)
       body2.forward(3)
   trtl.fillcolor("red")
   body1.fillcolor("red")
   body2.fillcolor("red")


   # print result
   print("Game over!")
   exit()


# fourth question
answer4 = input("Are you over 150 years old? y/n")
if(answer4 == "n"):


   # move snake to bottom left
   trtl.left(90)
   for step in range(15):
       trtl.forward(2)
       body1.forward(2/3)
   body1.left(90)
   for step in range(10):
       body1.forward(2)
       body2.forward(2)
   body2.left(90)
   for step in range(15):
       body2.forward(2/3)
       body3.forward(2)
   body3.left(90)
   for step in range(42):
       trtl.forward(4)
       body1.forward(4)
       body2.forward(4)
       body3.forward(4)
  
   # eat bottom left apple
   bottomleft.hideturtle()
  
   # add fourth body segment
   body4 = trtl.Turtle()
   trtl_body.append(body4)
   body4.turtlesize(2)
   body4.fillcolor("lime")
   body4.setheading(270)
   body4.penup()
   body4.goto(body3.xcor(), body3.ycor() + 10)


   # print result
   print("Correct!")


else:
   # move snake to border
   for step in range(14):
       trtl.forward(4)
       body1.forward(4)
       body2.forward(4)
       body3.forward(4)
   trtl.fillcolor("red")
   body1.fillcolor("red")
   body2.fillcolor("red")
   body3.fillcolor("red")


   # print result
   print("Game over!")
   exit()


# fifth Question
answer5 = input("What is 1 + 1?")
if(answer5 == "2"):


   # move snake to bottom right
   trtl.left(90)
   for step in range(20):
       trtl.forward(2)
       body1.forward(0.5)
   body1.left(90)
   for step in range(15):
       body1.forward(2)
       body2.forward(4/3)
   body2.left(90)
   for step in range(15):
       body2.forward(4/3)
       body3.forward(2)
   body3.left(90)
   for step in range(20):
       body3.forward(0.5)
       body4.forward(2)
   body4.left(90)
   for step in range(30):
       trtl.forward(5)
       body1.forward(5)
       body2.forward(5)
       body3.forward(5)
       body4.forward(5)
  
   # eat bottom right apple
   bottomright.hideturtle()


   # add fifth body segment
   body5 = trtl.Turtle()
   trtl_body.append(body5)
   body5.turtlesize(2)
   body5.fillcolor("lime")
   body5.setheading(0)
   body5.penup()
   body5.goto(body4.xcor() - 10, body4.ycor())


   # print result
   print("You win!")


else:
   # move snake to border
   for step in range(8):
       trtl.forward(5)
       body1.forward(5)
       body2.forward(5)
       body3.forward(5)
       body4.forward(5)
   trtl.fillcolor("red")
   body1.fillcolor("red")
   body2.fillcolor("red")
   body3.fillcolor("red")
   body4.fillcolor("red")


   # print result
   print("Game over!")
   exit()


wn = trtl.Screen()
wn.mainloop()
