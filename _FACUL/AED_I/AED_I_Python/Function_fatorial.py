def fatorial(a):
  if a == 0:
    return 1
  else:
    for b in range(1, a):
      multi = a * b
      a = multi
  return a
print(fatorial(50))