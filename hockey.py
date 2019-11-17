
# hockey game, Michael and Dirk Nachbar

import turtle
import random
import time

w = 600
h = 300
goalh = 50
midline = w / 2
bgcolor = 'turquoise'
puckradius = 5
padh = 15
playercol1 = 'white'
playercol2 = 'dark blue'
linecol = 'black'
team1 = 'Tampa Bay Lightning'
team2 = 'Toronto Maple Leafs'
# score1 = 0
# score2 = 0
chg = 15
shoot = .15

wn = turtle.Screen()
wn.title("Ice Hockey by Michael & Dirk")
wn.bgcolor(bgcolor)
wn.setup(width=w, height=h)
wn.tracer(0)

# draw the mid line
# http://interactivepython.org/runestone/static/IntroPythonTurtles/Summary/summary.html
# https://docs.python.org/2/library/turtle.html

l1 = turtle.Turtle()
l1.shape('square')
l1.color('black')
l1.shapesize(stretch_wid=15, stretch_len=.1)
l1.penup()
l1.goto(0, 0)

g1 = turtle.Turtle()
g1.shape('square')
g1.color('black')
g1.shapesize(stretch_wid=5, stretch_len=1)
g1.penup()
g1.goto(- w / 2 + 20, 0) # left goal
g1.goals = 0

g2 = turtle.Turtle()
g2.shape('square')
g2.color('black')
g2.shapesize(stretch_wid=5, stretch_len=1)
g2.penup()
g2.goto(w / 2 - 30, 0) # right goal
g2.goals = 0

p1 = turtle.Turtle()
p1.shape('square')
p1.color(playercol1)
p1.penup()
p1.goto(- w / 2 + 100, 0) # netminder

p2 = turtle.Turtle()
p2.shape('square')
p2.color(playercol1)
p2.penup()
p2.goto(- w / 2 + 200, 0) # center man

p3 = turtle.Turtle()
p3.shape('square')
p3.color(playercol2)
p3.penup()
p3.goto(w / 2 - 100, 0) # netminder

p4 = turtle.Turtle()
p4.shape('square')
p4.color(playercol2)
p4.penup()
p4.goto(w / 2 - 200, 0) # center man

puck = turtle.Turtle()
puck.shape('circle')
puck.color('grey')
puck.penup()
puck.goto(0, 0)
puck.shapesize(.5, .5)
puck.dx = .1
puck.dy = -.1
puck.speed(1)

sb = turtle.Turtle()
sb.color('green')
sb.penup()
sb.hideturtle()
sb.goto(0, h / 2 - 30)
sb.write(team1 + ' vs ' + team2 + ' ' + str(g2.goals) + ':' + str(g1.goals), align='center', font=("Courier", 8, "normal"))


# left team: p1: q a, p2: w s, pass: 1, shoot: 2-4

# right team: p3: p l, p4: o k, pass: 0, shoot: 7-9

def move_p1_up():
  y = p1.ycor()
  y += chg
  if player_has_puck(p1, puck):
    puck.sety(y)
  p1.sety(y)

def move_p1_down():
  y = p1.ycor()
  y -= chg
  if player_has_puck(p1, puck):
    puck.sety(y)
  p1.sety(y)

def move_p2_up():
  y = p2.ycor()
  y += chg
  if player_has_puck(p2, puck):
    puck.sety(y)
  p2.sety(y)

def move_p2_down():
  y = p2.ycor()
  y -= chg
  if player_has_puck(p2, puck):
    puck.sety(y)
  p2.sety(y)

def move_p3_up():
  y = p3.ycor()
  y += chg
  if player_has_puck(p3, puck):
    puck.sety(y)
  p3.sety(y)

def move_p3_down():
  y = p3.ycor()
  y -= chg
  if player_has_puck(p3, puck):
    puck.sety(y)
  p3.sety(y)

def move_p4_up():
  y = p4.ycor()
  y += chg
  if player_has_puck(p4, puck):
    puck.sety(y)
  p4.sety(y)

def move_p4_down():
  y = p4.ycor()
  y -= chg
  if player_has_puck(p4, puck):
    puck.sety(y)
  p4.sety(y)

def pass1():
  if player_has_puck(p1, puck):
    puck.setx(p2.xcor())
    puck.sety(p2.ycor())
  elif player_has_puck(p2, puck):
    puck.setx(p1.xcor())
    puck.sety(p1.ycor())

def pass2():
  if player_has_puck(p3, puck):
    puck.setx(p4.xcor())
    puck.sety(p4.ycor())
  elif player_has_puck(p4, puck):
    puck.setx(p3.xcor())
    puck.sety(p3.ycor())

def t1_shoot_up():
  if player_has_puck(p1, puck) or player_has_puck(p2, puck):
    puck.setx(puck.xcor() + 16)
    puck.dx = shoot
    puck.dy = shoot

def t1_shoot_right():
  if player_has_puck(p1, puck) or player_has_puck(p2, puck):
    puck.setx(puck.xcor() + 16)
    puck.dx = shoot

def t1_shoot_down():
  if player_has_puck(p1, puck) or player_has_puck(p2, puck):
    puck.setx(puck.xcor() + 16)
    puck.dx = shoot
    puck.dy = -shoot

def t2_shoot_up():
  if player_has_puck(p3, puck) or player_has_puck(p4, puck):
    puck.setx(puck.xcor() - 16)
    puck.dx = -shoot
    puck.dy = shoot

def t2_shoot_left():
  if player_has_puck(p3, puck) or player_has_puck(p4, puck):
    puck.setx(puck.xcor() - 16)
    puck.dx = -shoot

def t2_shoot_down():
  if player_has_puck(p3, puck) or player_has_puck(p4, puck):
    puck.setx(puck.xcor() - 16)
    puck.dx = -shoot
    puck.dy = -shoot

wn.listen()
wn.onkey(move_p1_up, 'q')
wn.onkey(move_p1_down, 'a')
wn.onkey(move_p2_up, 'w')
wn.onkey(move_p2_down, 's')
wn.onkey(move_p3_up, 'p')
wn.onkey(move_p3_down, 'l')
wn.onkey(move_p4_up, 'o')
wn.onkey(move_p4_down, 'k')
wn.onkey(pass1, '1')
wn.onkey(pass2, '0')
wn.onkey(t1_shoot_up, '2')
wn.onkey(t1_shoot_right, '3')
wn.onkey(t1_shoot_down, '4')
wn.onkey(t2_shoot_up, '9')
wn.onkey(t2_shoot_left, '8')
wn.onkey(t2_shoot_down, '7')

def touch_edge(puck):
  if puck.xcor() > w / 2 or puck.xcor() < - w / 2:
    puck.dx = -puck.dx 
  if puck.ycor() > h / 2 or puck.ycor() < - h / 2:
    puck.dy = -puck.dy

def touch_goal(puck, goal):
  if goal.xcor() - 20 < puck.xcor() < goal.xcor() + 20 and \
      goal.ycor() - 60 < puck.ycor() < goal.ycor() + 60:
    goal.goals += 1
    print('goal')
    sb.clear()
    sb.write(team1 + ' vs ' + team2 + ' ' + str(g2.goals) + ':' + str(g1.goals), align='center', font=("Courier", 8, "normal"))
    # reset the puck
    puck.goto(0, 0)
    time.sleep(1)
    puck.dx = random.uniform(-.2, .2)
    puck.dy = random.uniform(-.2, .2)

def player_has_puck(player, puck):
  return player.xcor() == puck.xcor() and player.ycor() == puck.ycor()

def touch_player(puck, player):
  # puck attached to player
  if player.xcor() - 15 < puck.xcor() < player.xcor() + 15 and \
      player.ycor() - 15 < puck.ycor() < player.ycor() + 15:
    puck.setx(player.xcor())
    puck.sety(player.ycor())
    puck.dx = 0
    puck.dy = 0

while True:
  wn.update()	

  puck.sety(puck.ycor() + puck.dy)
  puck.setx(puck.xcor() + puck.dx)

  touch_edge(puck)

  touch_player(puck, p1)
  touch_player(puck, p2)
  touch_player(puck, p3)
  touch_player(puck, p4)

  touch_goal(puck, g1)
  touch_goal(puck, g2)

