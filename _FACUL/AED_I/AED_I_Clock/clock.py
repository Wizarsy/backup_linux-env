from graphics import *
import datetime
import time
import math

win = GraphWin('Relógio Analógico', 500, 500)
clock_border = Circle(Point(250, 250), 210).draw(win).setFill('Black')
clock = Circle(Point(250, 250), 200).draw(win).setFill('White')
calendar = Rectangle(Point(290, 235), Point(380, 265)).draw(win)
calendar_div = Line(Point(335, 235), Point(335, 265)).draw(win)
day = Text(Point(312.5, 250), '').draw(win)
month = Text(Point(357.5, 250), '').draw(win)
day.setStyle('bold')
month.setStyle('bold')
clock_center = 250
pi = math.pi

# hour_arrow = Polygon(Point(245, 75), Point(250, 55), Point(255, 75))
hour_arrow_coord = [[245, 250], [250, 105], [255, 250]]
# minute_arrow = Polygon(Point(245, 85), Point(250, 65), Point(255, 85))
minute_arrow_coord = [[247, 250], [250, 65], [253, 250]]
# second_arrow = Polygon(Point(245, 95), Point(250, 75), Point(255, 95))
second_arrow_coord = [[249, 250], [250, 90], [251, 250]]

def hand_rot(x, y, angle, b):
  sin = math.sin(angle * pi / b )
  cos = math.cos(angle * pi / b )
  x = x - clock_center
  y = y - clock_center
  nx = clock_center + (x * cos - y * sin)
  ny = clock_center + (x * sin + y * cos)
  return nx, ny

def poly_np(points, angle, cx, cy, b):
  sin = math.sin(angle * pi / b )
  cos = math.cos(angle * pi / b )
  np=[]
  for p in range(len(points)):
    x = points[p][0] - cx
    y = points[p][1] - cy
    nx = cx + (x * cos - y * sin)
    ny = cy + (x * sin + y * cos)
    np.append(nx), np.append(ny)
  return np

def dash():
  for i in range(1,13):
    tx, ty = hand_rot(250, 50, i, 6)
    tx1, ty1 = hand_rot(250, 60, i, 6)
    tx2, ty2 = hand_rot(250, 75, i, 6)
    num_hour = Text(Point(tx2, ty2), i).draw(win).setSize(18)
    dash_hour = Line(Point(tx, ty), Point(tx1, ty1)).draw(win).setWidth(3)
  for i in range(60):
    tx, ty = hand_rot(250, 50, i, 30)
    tx1, ty1 = hand_rot(250, 55, i, 30)
    dash_minute = Line(Point(tx, ty), Point(tx1, ty1)).draw(win).setWidth(1.2)

def getday():
  return datetime.datetime.now().strftime('%d')

def getmonth():
  return datetime.datetime.now().strftime('%b')

def gethour():
  return int(datetime.datetime.now().strftime('%I'))

def getminute():
  return int(datetime.datetime.now().strftime('%M'))

def getsecond():
  return int(datetime.datetime.now().strftime('%S'))

dash()

while True:
  # nhx, nhy = hand_rot(250, 125, hour(), 6)
  # hour_hand = Line(Point(clock_center, clock_center), Point(nhx, nhy)).draw(win)
  # hour_hand.setFill('Blue')
  # hour_hand.setWidth(4)

  # nmx, nmy = hand_rot(250, 85, minute(), 30)
  # minute_hand = Line(Point(clock_center, clock_center), Point(nmx, nmy)).draw(win)
  # minute_hand.setFill('Green')
  # minute_hand.setWidth(3.5)

  # nsx, nsy = hand_rot(250, 110, second(), 30)
  # second_hand = Line(Point(clock_center, clock_center), Point(nsx, nsy)).draw(win)
  # second_hand.setFill('Red')
  # second_hand.setWidth(3)

  nph = poly_np(hour_arrow_coord, gethour(), clock_center, clock_center, 6)
  hour_arrow = Polygon(Point(nph[0], nph[1]), Point(nph[2], nph[3]), Point(nph[4], nph[5])).draw(win)
  hour_arrow.setOutline('Black')
  hour_arrow.setFill('Black')
  hour_arrow.setWidth(2)

  npm = poly_np(minute_arrow_coord, getminute(), clock_center, clock_center, 30)
  minute_arrow = Polygon(Point(npm[0], npm[1]), Point(npm[2], npm[3]), Point(npm[4], npm[5])).draw(win)
  minute_arrow.setOutline('Black')
  minute_arrow.setFill('Black')
  minute_arrow.setWidth(2)

  nps = poly_np(second_arrow_coord, getsecond(), clock_center, clock_center, 30)
  second_arrow = Polygon(Point(nps[0], nps[1]), Point(nps[2], nps[3]), Point(nps[4], nps[5])).draw(win)
  second_arrow.setFill('Red')
  second_arrow.setOutline('Red')
  second_arrow.setWidth(2)

  center = Circle(Point(250, 250), 5).draw(win)
  center.setFill('Red')
  center.setOutline('Red')
  day.setText(getday())
  month.setText(getmonth())

  time.sleep(1)
  center.undraw()
  hour_arrow.undraw()
  minute_arrow.undraw()
  second_arrow.undraw()
  # hour_hand.undraw()
  # minute_hand.undraw()
  # second_hand.undraw()