#coding=UTF-8
res='s'
maior_idade= float('-inf')
menor_idade= float('inf')
maior_salario=0
med_salario=0
loop=0
mulheres=0
while res == 's':
  idade=int(input('Digite uma idade: '))
  if idade <= 0:
    idade='erro'
    break
  sexo=input('Informe o sexo: M/F: ').lower()
  if sexo =='f':
    mulheres+=1        
  salario=float(input('Informe o salário: '))
  if salario > maior_salario:
    maior_salario=salario
    if sexo == 'f':
      maior_salario_sexo= 'mulher'
    else:
      maior_salario_sexo= 'homem'
    maior_salario_idade= idade    
  med_salario+=salario
  if idade > maior_idade:
    maior_idade= idade    
  if idade < menor_idade:  
    menor_idade= idade    
  loop+=1
  media= med_salario/loop
  res=input('Gostaria de coletar mais dados? S/N: ').lower()
if idade == 'erro':
  print('Idade inválida, ainda não forma lidos dados válidos')
else:
  print('Á média de salários é {0}, a menor idade é {1}, a maior idade é {2}, a região possui {3} mulher(es) e a pessoa que possui o maior sálario é um(a) {4} de {5} anos'.format(media, menor_idade, maior_idade, mulheres, maior_salario_sexo, maior_salario_idade))