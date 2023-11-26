class Pilha:
  def __init__(self, tamanho):
    self.vetor = [None] * tamanho
    self.lim = tamanho -1
    self.base = 0
    self.topo = self.base - 1
    
  def Empilhar(self,dado):
    if self.topo < self.lim:
      self.topo += 1
      self.vetor[self.topo] = dado
      
  def Remover(self):
    if self.topo >= self.base:
      self.topo-=1
  
  def Consultar(self):
    if self.topo >= self.base:
      return self.vetor[self.topo]
  
  def Destruir(self):
    self.topo = self.base - 1