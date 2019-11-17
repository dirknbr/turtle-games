
# baseball game, Dirk and M Nachbar

import turtle
import random
import time

w = 600
h = 600
leng = 10
teama = 'LA Dodgers'
teamb = 'LA Angels'
bgcol = 'green'
diamcol = 'black'
ballcol = 'white'
teamacol = 'blue'
teambcol = 'red'
basecol = 'light green'
scorea = 0
scoreb = 0
sbcol = 'black'

wn = turtle.Screen()
wn.title("Baseball by Michael & Dirk")
wn.bgcolor(bgcol)
wn.setup(width=w, height=h)
wn.tracer(0)

diam = turtle.Turtle()
diam.shape('square')
diam.color(diamcol)
diam.shapesize(leng, leng)
diam.rt(45)
diam.goto(0, -150)
diam.penup()

b1 = turtle.Turtle()
b1.shape('square')
b1.color(basecol)
b1.shapesize(.5, .5)
b1.penup()
b1.goto(150, -150)

b2 = turtle.Turtle()
b2.shape('square')
b2.color(basecol)
b2.shapesize(.5, .5)
b2.penup()
b2.goto(0, 0)

b3 = turtle.Turtle()
b3.shape('square')
b3.color(basecol)
b3.shapesize(.5, .5)
b3.penup()
b3.goto(-150, -150)

b4 = turtle.Turtle()
b4.shape('square')
b4.color(basecol)
b4.shapesize(.5, .5)
b4.penup()
b4.goto(0, -270)


# peopple
batsman = turtle.Turtle()
batsman.shape('square')
batsman.color(teamacol)
batsman.goto(0, -270)
batsman.shapesize(.8, .8)
batsman.penup()
batsman.speed(1)
batsman.running = False
batsman.lives = 3
batsman.dx = 0
batsman.dy = 0

pitcher = turtle.Turtle()
pitcher.shape('square')
pitcher.color(teambcol)
pitcher.goto(0, -150)
pitcher.shapesize(.8, .8)
pitcher.penup()

ss = turtle.Turtle()
ss.shape('square')
ss.color(teambcol)
ss.goto(0, 0)
ss.shapesize(.8, .8)
ss.penup()

catcher = turtle.Turtle()
catcher.shape('square')
catcher.color(teambcol)
catcher.goto(0, -290)
catcher.shapesize(.8, .8)
catcher.penup()

lf = turtle.Turtle()
lf.shape('square')
lf.color(teambcol)
lf.penup()
lf.goto(-150, 150)
lf.shapesize(.8, .8)

rf = turtle.Turtle()
rf.shape('square')
rf.color(teambcol)
rf.penup()
rf.goto(150, 150)
rf.shapesize(.8, .8)
	
cf = turtle.Turtle()
cf.shape('square')
cf.color(teambcol)
cf.penup()
cf.goto(0, 200)
cf.shapesize(.8, .8)

ball = turtle.Turtle()
ball.shape('circle')
ball.color(ballcol)
ball.goto(0, -150)
ball.shapesize(.5, .5)
ball.penup()
ball.speed(1)
ball.dx = 0
ball.dy = 0
ball.hit = False
ball.caught = False

sb = turtle.Turtle()
sb.color(sbcol)
sb.penup()
sb.hideturtle()
sb.goto(0, h / 2 - 30)
# sb.write(teama + ' vs ' + teamb + ' ' + str(scorea) + ':' + str(scoreb) + ' lives:' + str(batsman.lives), 
# 	align='center', font=("Courier", 8, "normal"))


def throw():
  ball.dy = -.3

def catch():
  for c in [catcher, cf, lf, ss, rf]:
    if ball.xcor() - 10 <= c.xcor() <= ball.xcor() + 10 and ball.ycor() - 10 <= c.ycor() <= ball.ycor() + 10:
  	  ball.dy = 0
  	  ball.dx = 0
  	  ball.caught = True

def hit():
  if ball.ycor() - 10 <= batsman.ycor() <= ball.ycor() + 10:
  	print('hit')
  	ball.dx = 1.2 * random.random() - .5
  	ball.dy = .7
  	ball.hit = True

def right():
  for p in [lf, cf, ss, rf]:
  	p.setx(p.xcor() + 10)

def left():
  for p in [lf, cf, ss, rf]:
  	p.setx(p.xcor() - 10)

def run():
  if ball.hit:
  	batsman.running = True

def stop():
  if batsman.running:
  	batsman.running = False

def in_or_out():
  for base in [b1, b2, b3]:
  	if base.xcor() - 10 <= batsman.xcor() <= base.xcor() + 10 and base.ycor() - 10 <= batsman.ycor() <= base.ycor() + 10:
  	  return 'in'
  return 'out'

def reset():
  ball.goto(0, -150)
  batsman.goto(0, -270)
  ball.dx = 0
  ball.dy = 0
  batsman.dx = 0
  batsman.dy = 0
  batsman.running = False
  ball.hit = False
  ball.caught = False

wn.listen()
wn.onkey(throw, 'Down')
# wn.onkey(catch, 'Up')
wn.onkey(right, 'Right')
wn.onkey(left, 'Left')
wn.onkey(hit, '6')
wn.onkey(run, '5')
wn.onkey(stop, '7')
wn.onkey(reset, 'space')

# TODO: catch for outfield, moving of outfield
# TODO: 3 strikes you are out


while True:
  wn.update()

  ball.sety(ball.ycor() + ball.dy)
  ball.setx(ball.xcor() + ball.dx)

  # bounce off walls
  if ball.xcor() > w / 2 or ball.xcor() < - w / 2:
  	ball.dx *= -1

  if batsman.running:
  	# starts at 0, -270
    x, y = batsman.xcor(), batsman.ycor()
    if x >= 0 and y <= b1.ycor():
       batsman.dx = .3
       batsman.dy = .3
    elif x >= 0 and y > b1.ycor():
      batsman.dx = -.3
    elif x < 0 and y > b2.ycor():
      batsman.dy = -.3
    elif x < 0 and y < b3.ycor():
      batsman.dx = .3
    batsman.setx(batsman.xcor() + batsman.dx)
    batsman.sety(batsman.ycor() + batsman.dy)

  catch()

  # batsman misses and catcher catches > batsman loses life
  if ball.caught and ball.xcor() - 10 <= catcher.xcor() <= ball.xcor() + 10:
    scoreb += 1
    print('catcher catches')
    reset()
  # ball is hit and outfield catches and batsman is out > batsman loses life
  if ball.caught and ball.hit and in_or_out() == 'out':
    scoreb += 1
    print('batsman out')
    reset()
  # ball is hit and goes outside field > teama gets 1 point
  if ball.hit and ball.ycor() > h / 2 and ball.caught == False:
    scorea += 1
    print('home run')
    reset()


  sb.clear()
  sb.write(teama + ' vs ' + teamb + ' ' + str(scorea) + ':' + str(scoreb), 
		align='center', font=("Courier", 10, "normal"))





