def lista():
  lista=[]
  tamanho=int(input('tamanho: '))
  for x in range(tamanho):
    valores=int(input('valores: '))
    lista.append(valores)
  return lista

def buscador():
  lista_busca=lista()
  busca=int(input('busca: '))
  for ind in range(len(lista_busca)):
    if busca == lista_busca[ind]:
      return print('posição:',ind+1)
  return print('O elemento não está na lista')

buscador()