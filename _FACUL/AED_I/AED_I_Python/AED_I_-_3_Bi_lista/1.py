num_nega = []
num_posi = []
num = []
n = ''
while n != 'n':
  try:
    n = input('Digite um numero: N para encerrar ').lower()
    if n != 'n':
      num.append(int(n))
    else:
      break
  except:
    print('Digite um numero ou N para encerrar')
for item in num:
  if item >= 0:
    num_posi.append(item)
  else:
    num_nega.append(item)
    
print(f'numeros = {num}\nnumero positivos = {num_posi}\nnumeros negativos = {num_nega}')