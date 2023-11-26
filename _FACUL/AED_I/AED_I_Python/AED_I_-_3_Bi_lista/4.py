def divi(x):
  if x <= 0:
    return 'Ensira um numero positivo'
  else:
    return [y for y in range(1, x + 1) if x % y == 0]
  
print(divi(12))