class Node:
  def __init__(self, dado):
    self.dado = dado
    self.prox = None
    
class ListaEnc:
  def __init__(self):
    self.ini = None 
  
  def Inserir(self, dado, pos):
    if self.ini == None and pos <= self.Tamanho() + 1:
      self.ini = Node(dado)
    elif pos > 0 and pos <= self.Tamanho() + 1:
      aux = self.ini
      for i in range(1, pos - 1):
        aux = aux.prox
      if aux.prox != None:
        aux.prox.dado = dado
      else:
        aux.prox = Node(dado)
    else:
      return False
        
  def Remover(self, pos):
    if pos <= 0 or pos > self.Tamanho():
      return False
    aux = self.ini
    for i in range(1, pos - 1):
      aux = aux.prox
    aux.prox = aux.prox.prox
  
  def Tamanho(self):
    aux = self.ini
    tam = 0
    while aux != None:
      tam += 1
      aux = aux.prox
    return tam
  
  def Destruir(self):
    self.ini = None
  
  def Consultar(self, pos):
    if pos <= 0 or pos > self.Tamanho():
      return False
    aux = self.ini
    for i in range(1, pos):
      aux = aux.prox
    return aux.dado
  
  def Buscar(self, dado):
    aux = self.ini
    for i in range(1, self.Tamanho() + 1):
      if dado == aux.dado:
        return i
      aux = aux.prox
    return False
    
  def Reverter(self):
    aux = self.ini
    aux_list = ListaEnc()
    aux_list1 = aux_list.ini
    for i in range(self.Tamanho()):
      if aux_list.ini == None:
        aux_list.ini = Node(aux.dado)
      else:
        while aux_list1 != None:
          aux_list1 = aux_list1.prox
        aux_list1 = aux_list.ini
        aux_list2 = Node(aux.dado)
        aux_list.ini = aux_list2
        aux_list2.prox = aux_list1
      aux = aux.prox
    return aux_list
  
  def Comparar(self, lista):
    if self.Tamanho() != lista.Tamanho():
      return False
    aux = self.ini
    aux2 = lista.ini
    for i in range(1, self.Tamanho() + 1):
      if aux.dado != aux2.dado:
        return False
      aux = aux.prox
      aux2 = aux2.prox
    return True