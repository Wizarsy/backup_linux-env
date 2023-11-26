from graphics import *
import random as rd
import math

win = GraphWin('Rotation', 500, 500, autoflush = False)
circle = Circle(Point(250, 250), 50).draw(win)
poly = Polygon(Point(240, 280), Point(220, 220), Point(280, 240), Point(250, 250))
init_coord = poly.getPoints()
key = win.checkKey()
mxy = win.checkMouse()
pi = math.pi
a = 0

def poly_np(coord, angle, cx, cy): # gira a forma
  sin = math.sin(angle * pi / 180 )
  cos = math.cos(angle * pi / 180 )
  new_coord = []
  for p in coord:
    x = p.getX() - cx
    y = p.getY() - cy
    new_x = cx + (x * cos - y * sin)
    new_y = cy + (x * sin + y * cos)
    new_coord.append(new_x), new_coord.append(new_y)
  return new_coord

# def guia_point(x, y, cx, cy):
#   sin = math.sin(1 * pi / 180 )
#   cos = math.cos(1 * pi / 180 )
#   x = x - cx
#   y = y - cy
#   nx = cx + (x * cos - y * sin)
#   ny = cy + (x * sin + y * cos)
#   return nx, ny

# mover o ponto não o poly
#poly segue o ponto
guia_p = Circle(Point(170, 170), 2)

while True:
  try:
    new_poly.undraw()
    # nose.undraw()
  except:
    pass

  np = poly_np(init_coord, a, init_coord[3].getX(), init_coord[3].getX())
  new_poly = Polygon(Point(np[0], np[1]), Point(np[2], np[3]), Point(np[4], np[5]), Point(np[6], np[7]))
  new_poly.draw(win).setFill('Purple')
  # print(f'{np[2]:.2f}, {np[3]:.2f}, {mxy[0].getX()}, {mxy[0].getY()}, {a}')

  # ngx, ngy = guia_point(guia_p.getCenter().getX(), guia_p.getCenter().getY(), np[2], np[3])
  # guia = Circle(Point(ngx, ngy), 2).draw(win)

  # if key == 'w':
  #   if int(np[2]) < mxy[0].getX():
  #     new_poly.move(1, 0)
  #   if int(np[2]) > mxy[0].getX():
  #     new_poly.move(-1, 0)
  #   if int(np[3]) < mxy[0].getY():
  #     new_poly.move(0, 1)
  #   if int(np[3]) > mxy[0].getY():
  #     new_poly.move(0, -1)

  if key == 'Right':
    a += 2
  if key == 'Left':
    a -= 2
  if key == 'space':
    a = 0
  init_coord = new_poly.getPoints()
  # guia_p = guia
  key = win.checkKey()
  mxy = win.checkMouse()
  print(np[2], np[3])
  update(144)