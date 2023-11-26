from pilhaEnc import *

class Node():
  def __init__(self, dado):
    self.dado = dado
    self.prox = None
    
class FilaEnc:
  def __init__(self,):
    self.ini = None
    self.fim = None
  
  def Vazia(self):
    return self.ini == None
  
  def Consultar(self):
    if not self.Vazia():
      return self.ini.dado
  
  def Inserir(self, dado):
    new = Node(dado)
    if self.Vazia():
      self.ini = new
    else:
      self.fim.prox = new
    self.fim = new
    
  def Excluir(self):
    if not self.Vazia():
      self.ini = self.ini.prox

  def Destruir(self):
    while not self.Vazia():
      self.Excluir()
      
  def Ordenar(self):
    pord = PilhaEnc()
    paux = PilhaEnc()
    while not self.Vazia():
      if pord.Vazia() or pord.Consultar() > self.Consultar():
        pord.Empilhar(self.Consultar())
        self.Excluir()
      else:
        while not pord.Vazia() and self.Consultar() > pord.Consultar():
          paux.Empilhar(pord.Consultar())
          pord.Excluir()
        pord.Empilhar(self.Consultar())
        self.Excluir()
        while not paux.Vazia():
          pord.Empilhar(paux.Consultar())
          paux.Excluir()
    while not pord.Vazia():
      self.Inserir(pord.Consultar())
      pord.Excluir()