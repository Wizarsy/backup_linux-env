class Node:
  def __init__(self, dado):
    self.dado = dado
    self.prox = None
    self.ant = None
    
class ListaEnc:
  def __init__(self):
    self.ini = None
    self.fim = None
  
  def Imprimir(self):
    aux = self.ini
    print("[", end =" ")
    while aux != None:
      print(aux.dado, end = " ")
      aux = aux.prox
    print("]")
      
  def Tamanho(self):
    aux = self.ini
    tam = 0
    while aux != None:
      tam += 1
      aux = aux.prox
    return tam
    
  def Inserir(self, dado, pos):
    if pos > 0 and pos <= self.Tamanho() + 1:
      new = Node(dado)
      if self.ini == None:
        self.ini = new
      else:
        aux = self.ini
        i = 1
        while i < pos - 1 and aux != None:
          aux = aux.prox
          i += 1
        if aux != None:
          new.ant = aux
          aux.prox = new
      
  def Remover(self, pos):
    if pos <= 0 or pos > self.Tamanho():
      return False
    aux = self.ini
    if pos == 1:
      self.ini = aux.prox
    else:
      i = 1
      while i < pos and aux != None:
        ant = aux
        aux = aux.prox
        i += 1
      if aux != None:
        ant.prox = aux.prox
        aux.ant = ant.ant
            
  def Destruir(self):
    self.ini = None
  
  def Consultar(self, pos):
    if pos <= 0 or pos > self.Tamanho():
      return False
    aux = self.ini
    i = 1
    while i < pos and aux != None:
      aux = aux.prox
    if i == pos and aux != None:
      return aux.dado
  
  def Buscar(self, dado):
    aux = self.ini
    i = 1
    while aux != None:
      if dado == aux.dado:
        return i
      aux = aux.prox
      i += 1
  
  def Comparar(self, lista):
    if self.Tamanho() != lista.Tamanho():
      return False
    aux = self.ini
    aux2 = lista.ini
    while aux != None:
      if aux.dado != aux2.dado:
        return False
      aux = aux.prox
      aux2 = aux2.prox
    return True
  
  def Reverter(self):
    aux = self.ini
    ant = aux
    while aux != None:
      if aux.dado > ant.dado:
        ant.ant =  aux
        aux.prox = ant
      ant = aux
      aux = aux.prox