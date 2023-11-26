a = str(input("N1: "))
b = str(input("n2: "))
n = len(a) if len(a) > len(b) else len(b) 
r = [0] * (n + 1)

aux_div = 0
for i in range(n - 1, -1, -1):
  aux_sum = int(a[i]) + int(b[i]) + aux_div
  r[i + 1] = aux_sum % 10
  aux_div = aux_sum // 10
r[0] = aux_div
print(r)