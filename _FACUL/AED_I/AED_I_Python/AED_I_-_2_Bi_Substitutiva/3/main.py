def datasimples(data):
  dataext=data.split(' ')
  meses=['janeiro','fevereiro','marco','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
  try:
    for cel in dataext:
      if cel.isdigit()==True:
        if int(cel) in range(1,32):
          dia=cel
      if cel.lower() in meses:
        if cel == 'fevereiro':
          if int(dia) in range(1,29):
            mes=2
          else:
            continue
        else:
          mes=meses.index(cel)+1
      ano=dataext[len(dataext)-1][:-1]
    return f'{dia}/{mes}/{ano}'
  except:
    return f'Invalido'

print(datasimples('Rio Grande, 28 de fevereiro de 2022.'))
print(datasimples('Rio Grande, 31 de fevereiro de 2022.'))
print(datasimples('Curitiba, de novembro de 1940.'))
print(datasimples('Rio Grande, 37 de dezembro de 2005.'))
print(datasimples('Porto Alegre, 23 de bolinha de 2009.'))
print(datasimples('25 de dezembro de 2009.'))
