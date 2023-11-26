class Lista:
  def __init__(self, max):
    self.max = max
    self.vetor = [None] * self.max
    self.ini = -1
    self.fim = -1

  def Vazia(self):
    return self.ini == -1 or self.fim == -1

  def Tamanho(self):
    if self.Vazia():
      return 0
    return self.fim - self.ini + 1
      
  def Inserir(self, posicao, dado):
    if (self.ini != 0 or self.fim != self.max - 1) and posicao > 0:
      if self.Vazia():
        print("Vazia")
        self.ini = self.max // 2
        self.fim = self.max // 2
      elif self.fim != self.max - 1:
        if posicao > self.Tamanho() + 1:
          print('corrigido')
          posicao = self.fim // 2
        print("moveu -->")
        for i in range(self.fim, self.ini + posicao - 2, -1):
          self.vetor[i + 1] = self.vetor[i]
        self.fim += 1
      else:
        print("moveu <--")
        for i in range(self.ini, self.ini + posicao - 1):
          self.vetor[i - 1] = self.vetor[i]
        self.ini -= 1
      self.vetor[self.ini + posicao - 1] = dado
      print(self.vetor, self.ini, self.fim)
      return True
    else:
      return False
    
  def Consultar(self, posicao):
    if not self.Vazia():
      return self.vetor[self.ini + posicao - 1]
    
  def Destrui(self):
    self.ini = -1
    self.fim = -1
    
  def Buscar(self, dado):
    if not self.Vazia():
      for i in range(self.ini, self.fim + 1):
        if self.vetor[i] == dado:
          return i - self.ini
        
      
  def Remover(self, posicao):
    if self.Vazia():
      return False
    elif posicao in range(self.Tamanho() + 1):
      print("excluiu <--")
      for i in range(self.ini + posicao, self.fim + 1):
        self.vetor[i] = self.vetor[i + 1]
      self.fim -= 1
      print(self.vetor, self.ini, self.fim)
      return True
    else:
      return False