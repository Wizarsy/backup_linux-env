a=['.','.','.']
b=['.','.','.']
c=['.','.','.']
winner = 0
position=[]
print('\nJOGO DA VELHA\n     ')
print('Indique a posição do X e Bolinha pra jogar, exemplo: X no C2 ou Bolinha no B3 (pode usar letras minusculas)\n')
print('    1    2    3')
print(f'A {a}\nB {b}\nC {c}\n')
for ind in range(4):
  x=''
  o=''
  while 'a' not in x and 'b' not in x and 'c' not in x or x in position:
    x=input('Indique a posição do X: ').lower()
  position.append(x)
  if 'a' in x:
    if '1' in x:
      a[0]='X'
    elif '2' in x:
      a[1]='X'
    elif '3' in x:
      a[2]='X'
  if 'b' in x:
    if '1' in x:
      b[0]='X'
    elif '2' in x:
      b[1]='X'
    elif '3' in x:
      b[2]='X'
  if 'c' in x:
    if '1' in x:
      c[0]='X'
    elif '2' in x:
      c[1]='X'
    elif '3' in x:
      c[2]='X'
  if a[0] == 'X' and b[0] == 'X' and c[0] == 'X':
    winner=1
    break
  elif a[1] == 'X' and b[1]  == 'X' and c[1] == 'X':
    winner=1
    break
  elif a[2] == 'X' and b[2] == 'X' and c[2] == 'X':
    winner=1
    break
  elif a[0] == 'X' and a[1] == 'X' and a[2] == 'X':
    winner=1
    break
  elif b[0] == 'X' and b[1] == 'X' and b[2] == 'X':
    winner=1
    break
  elif c[0] == 'X' and c[1] == 'X' and c[2] == 'X':
    winner=1
    break
  elif a[0] == 'X' and b[1] == 'X' and c[2] == 'X':
    winner=1
    break
  elif a[2] == 'X' and b[1] == 'X' and c[0] == 'X':
    winner=1
    break
  print('\n    1    2    3')
  print(f'A {a}\nB {b}\nC {c}\n')
  while 'a' not in o and 'b' not in o and 'c' not in o or o in position:
    o=input('Indique a posição da Bolinha: ').lower()
  position.append(o)
  if 'a' in o:
    if '1' in o:
      a[0]='O'
    elif '2' in o:
      a[1]='O'
    elif '3' in o:
      a[2]='O'
  if 'b' in o:
    if '1' in o:
      b[0]='O'
    elif '2' in o:
      b[1]='O'
    elif '3' in o:
      b[2]='O'
  if 'c' in o:
    if '1' in o:
      c[0]='O'
    elif '2' in o:
      c[1]='O'
    elif '3' in o:
      c[2]='O'
  if a[0] == 'O' and b[0] == 'O' and c[0] == 'O':
    winner=2
    break
  elif a[1] == 'O' and b[1] == 'O' and c[1] == 'O':
    winner=2
    break
  elif a[2] == 'O' and b[2] == 'O' and c[2] == 'O':
    winner=2
    break
  elif a[0] == 'O' and a[1] == 'O' and a[2] == 'O':
    winner=2
    break
  elif b[0] == 'O' and b[1] == 'O' and b[2] == 'O':
    winner=2
    break
  elif c[0] == 'O' and c[1] == 'O' and c[2] == 'O':
    winner=2
    break
  elif a[0] == 'O' and b[1] == 'O' and c[2] == 'O':
    winner=2
    break
  elif a[2] == 'O' and b[1] == 'O' and c[0] == 'O':
    winner=2
    break
  print('\n    1    2    3')
  print(f'A {a}\nB {b}\nC {c}\n')
if winner == 1:
  print('\nO X ganhou!\n')
if winner == 2:
  print('\nA Bolinha ganhou!\n')
if winner == 0:
  print('\nEmpate, não foi dessa vez\n')
print('    1    2    3')
print(f'A {a}\nB {b}\nC {c}\n')