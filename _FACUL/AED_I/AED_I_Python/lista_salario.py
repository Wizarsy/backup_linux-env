salario=[5000,8000,4500,4000,1200,700,2000]
meses=[]
maior_ant=[]
for mes in range(len(salario)):
  if salario[mes] > 5000:
    meses.append(mes+1)
  if mes!=0 and salario[mes] > salario[mes-1]:
    maior_ant.append(mes+1)


print(meses)
print(maior_ant)