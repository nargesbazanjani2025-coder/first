#import turtle
#t=turtle.Pen()
#t.reset()
#for X in range(1,19):
 #   t.fd(100)
  #  if X%2==0:
   #     t.left(175)
    #else:
     #   t.left(225)
    
    

import turtle
t=turtle.Pen()
t.reset()
t.color(1,0,0)
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(20)
t.left(90)
t.forward(20)
t.right(90)
t.fd(20)
t.left(90)
t.forward(60)
t.left(90)
t.fd(20)
t.right(90)
t.fd(20)
t.left(90)
t.fd(20)
t.end_fill()


t.color(0,0,0)
t.up()
t.fd(10)
t.down()
t.begin_fill()
t.circle(10)
t.end_fill()


t.setheading(0)
t.up()
t.fd(90)
t.right(90)
t.fd(10)
t.setheading(0)
t.begin_fill()
t.down()
t.circle(10)
t.end_fill()

