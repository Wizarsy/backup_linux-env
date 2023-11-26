a = [[0] * 7 for x in range(7)]
b = [[0] * 5 for x in range(5)]
c = [[1] * 2 for x in range(2)]

def status(j):
    pino_final = 0
    for linha in range(len(j)):
        for coluna in range(len(j[linha])):
            pino_final += j[linha][coluna]
            if pino_final > 1:
                return False
    return True

a[0][0] = 1
print(a)
print(status(a))

b[0][0] = 1
print(b)
print(status(b))

c[0][0] = 0
c[0][1] = 0
c[1][0] = 0
print(c)
print(status(c))