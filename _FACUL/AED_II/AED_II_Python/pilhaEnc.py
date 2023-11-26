class Node:
  def __init__(self, dado):
    self.dado = dado
    self.prox = None

class PilhaEnc:
  def __init__(self):
    self.topo = None
  
  def Vazia(self):
    return self.topo == None
  
  def Empilhar(self,dado):
    new = Node(dado)
    if not self.Vazia():
      new.prox = self.topo 
    self.topo = new
  
  # def Remover(self):
  #   if not self.Vazia():
  #     self.topo = self.topo.prox
      
  def Remover(self):
    if not self.Vazia():
      aux = self.topo
      self.topo = aux.prox
      del aux
  
  def Consultar(self):
    if not self.Vazia():
      return self.topo.dado
  
  def Destruir(self):
    while not self.Vazia():
      self.Excluir()