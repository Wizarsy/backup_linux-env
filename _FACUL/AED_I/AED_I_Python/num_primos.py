inicio = 0
fim = 1000
for num in range(inicio, fim+1):
  if num == 1:
    continue
  else:
    resto = num % 2
    if resto != 0 or num == 2:
      for div in range(2, num):
        resto = num % div
        if resto == 0:
          break
      if resto != 0 or num == 2:
        print(num, end='\t')