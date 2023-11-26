# matrix = [[1, 3, 5, 8, 0], [2, 5, 7, 3, 77], [8, 33, 99, 2, 15], [7, 2, 0, 3, 2], [6, 9, 2, 4, 8], [55, 78, 99, 12, 45], [65, 39, 22, 96, 55], [83, 163, 777, 90, 43], [15, 234, 76, 45, 87], [33, 45, 12, 76, 83]]
matrix = []
sub_lista = []

for linha in range(5):
  for coluna in range(10):
    try:
      sub_lista.append(int(input('Digite um numero: ')))
    except:
      sub_lista.append(0)
  matrix.append(sub_lista)

print(matrix)
for coluna in range(len(matrix[0])):
  for linha in range(len(matrix)):
    print(f'[{matrix[linha][coluna]}]', end = '\t')
  print()