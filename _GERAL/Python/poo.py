class triangulo:
  def __init__(self, a, b, c):
    self.ladoA = a
    self.ladoB = b
    self.ladoC = c
    
  def calcularPerimetro(self):
    return self.ladoA + self.ladoB + self.ladoC
  
  def obterMaiorLado(self):
    return max(self.ladoA, self.ladoB, self.ladoC)
  
  def ehTriangulo(self):
    if (self.ladoA + self.ladoB <= self.ladoC) or (self.ladoA + self.ladoC <= self.ladoB) or (self.ladoB + self.ladoC <= self.ladoA):
      return False
    return True
  
  def informaTipoTriangulo(self):
    if self.ehTriangulo() == False:
      return False
    if self.ladoA == self.ladoB == self.ladoC:
      return 'Equilatero'
    if self.ladoA == self.ladoB or self.ladoB == self.ladoC or self.ladoC == self.ladoA:
      return 'Isosceles'
    else:
      return 'Escaleno'
       
a = triangulo(15, 12, 23)

print(a.calcularPerimetro())
print(a.obterMaiorLado())
print(a.ehTriangulo())
print(a.informaTipoTriangulo())