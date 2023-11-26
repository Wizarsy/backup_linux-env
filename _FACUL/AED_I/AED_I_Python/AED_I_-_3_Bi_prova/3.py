def diagonal(matriz):
    prin = 0
    sec = 0
    for linha in range(len(matriz)):
        prin += matriz[linha][linha]
        sec += matriz[linha][-(linha + 1)]
    if prin >= sec:
        return True
    return False



a = [[1, 2, 3], [2, 3, 4], [4, 5, 6]]
b = [[1, 2, 3, 8], [2, 3, 4, 7], [4, 5, 6, 3], [4, 5, 6, 5]]
print(diagonal(a))
print(diagonal(b))