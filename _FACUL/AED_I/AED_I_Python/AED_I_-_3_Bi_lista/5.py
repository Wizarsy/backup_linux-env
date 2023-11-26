def pow(x, a):
  p = 1
  while a > 0:
    p *= x
    a -= 1
  return p


print(pow(2, 3))