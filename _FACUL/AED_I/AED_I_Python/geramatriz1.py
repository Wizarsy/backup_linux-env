def geraMatriz(x, y):
  matriz =[]
  for linha in range(x):
    matriz.append([])
    for coluna in range(y):
      matriz[linha].append(0)
  return matriz

m1 = geraMatriz(3, 3)
m2 = geraMatriz(2, 3)
m3 = geraMatriz(3, 2)
print(f'{m1}\n{m2}\n{m3}\n')
m1[0][0] = 1
m2[1][0] = 4
m3[2][1] = 8
print(f'{m1}\n{m2}\n{m3}\n')


def geraMatrix2(x, y):
  return [[0] * y for i in range(x)]

m4 = geraMatrix2(3, 3)
print(m4)
m4[1][0] = 6
print(m4)