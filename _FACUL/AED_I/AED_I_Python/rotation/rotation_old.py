from graphics import *
import random as rd
import math

win = GraphWin('', 500, 500)
circle = Circle(Point(250, 250), 50).draw(win)
radius = circle.getRadius()
pol = Polygon(Point(240, 280), Point(220, 220), Point(280, 240), Point(250, 250))
pol.draw(win).setFill('yellow')
key = win.checkKey()
pi = math.pi
a = 0

def pol_np(points, angle, cx, cy):
  sin = math.sin(angle * pi / 180 )
  cos = math.cos(angle * pi / 180 )
  np=[]
  for p in points:
    x = p.getX() - cx
    y = p.getY() - cy
    nx = cx + (x * cos - y * sin)
    ny = cy + (x * sin + y * cos)
    np.append(nx)
    np.append(ny)
  return np

while True:
  points = pol.getPoints()

  if a != 0:
    np = pol_np(points, a, points[3].getX(), points[3].getY())
    pol.undraw()
    pol = Polygon(Point(np[0], np[1]), Point(np[2], np[3]), Point(np[4], np[5]), Point(np[6], np[7]))
    pol.draw(win).setFill(color_rgb(rd.randrange(256),rd.randrange(256),rd.randrange(256)))
    time.sleep(0.000001)
  if a == 0:
    pol.undraw()
    pol.draw(win).setFill(color_rgb(rd.randrange(256),rd.randrange(256),rd.randrange(256)))
    time.sleep(0.000001)

  if key == 'Up':
    pol.move(0, -5)

  if key == 'Down':
    pol.move(0, 5)

  if key == 'Right':
    a += 1

  if key == 'Left':
    a -= 1

  if key == 'Escape':
    a = 0

  key = win.checkKey()