from graphics import *
import time

win = GraphWin('Sprites', 1000, 500, autoflush=False)
idle = []
dead = []
jump = []
walk = []
run = []
key = ''
action = 0
jump_st = 0
sprites_path = '_FACUL/AED_I/game_graphics/sprites'

action_st = {
  'jump_st' : 0,
  'run_st' : 0,
  'walk_st' : 0,
}

for i in range(1, 16):
  idle.append(Image(Point(350, 260), f'{sprites_path}/Idle ({i}).png'))
  dead.append(Image(Point(350, 260), f'{sprites_path}/Dead ({i}).png'))
  jump.append(Image(Point(350, 260), f'{sprites_path}/Jump ({i}).png'))
  walk.append(Image(Point(350, 260), f'{sprites_path}/Walk ({i}).png'))
  run.append(Image(Point(350, 260), f'{sprites_path}/Run ({i}).png'))

x, y = 4, 0
while True:
  print(key)
  if action >= 15:
    action = 0
    
  if action_st['walk_st'] >= 15:
    action_st['walk_st'] = 0

  if action_st['run_st'] >= 15:
    action_st['run_st'] = 0
   
  if action_st['jump_st'] >= 15:
    action_st['jump_st'] = 0

  if key == 'Right' or action_st['walk_st'] > 0:
    if action_st['walk_st'] == 0:
      action = 0
    walk[action].draw(win).move(x, y)
    idle[action].move(x, y)
    jump[action].move(x, y)
    update()
    action_st['walk_st'] += 1
    time.sleep(0.025)
    walk[action].undraw()

  elif key == 'd' or action_st['run_st'] > 0:
    if action_st['run_st'] == 0:
      action = 0
    run[action].draw(win).move(x, y)
    walk[action].move(x, y)
    idle[action].move(x, y)
    jump[action].move(x, y)
    update()
    action_st['run_st'] += 1
    time.sleep(0.025)
    run[action].undraw()

  elif key == 'space' or action_st['jump_st'] > 0:
    if action_st['jump_st'] == 0:
      action = 0
    jump[action].draw(win)
    update()
    action_st['jump_st'] += 1
    time.sleep(0.025)
    jump[action].undraw()
    
  elif key == '':
    idle[action].draw(win)
    update()
    time.sleep(0.025)
    idle[action].undraw()
  key = win.checkKey()
  action += 1