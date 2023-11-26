def somaIt(lista):
  res = 0
  for i in lista:
    res += i
  return res

def somaRec(lista):
  if len(lista) == 0:
    return 0
  return lista[0] + somaRec(lista[1:])

def fatorialIt(n):
  res = 1
  if n == 0:
    return 1
  while n > 1:
    res *= n
    n -= 1
  return res

def fatorialRec(n):
  if n == 0:
    return 1
  return n * fatorialRec(n - 1)

def fiboIt(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  a, b = 0, 1
  while n > 0:
    b, a = a, a+b
    n -= 1
  return a

def fiboRec(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  return fiboRec(n - 1) + fiboRec(n - 2)

def digitosIt(n):
  res = 0
  while n > 0:
    res += n % 10
    n //= 10
  return res

def digitosRec(n):
  if n < 10:
    return n
  return n % 10 + digitosRec(n // 10)




print(somaIt([1, 2, 3, 10]))
print(somaRec([1, 2, 3, 10]))

print(fatorialIt(10))
print(fatorialRec(10))

print(fiboIt(10))
print(fiboRec(10))

print(digitosIt(14))
print(digitosRec(14))