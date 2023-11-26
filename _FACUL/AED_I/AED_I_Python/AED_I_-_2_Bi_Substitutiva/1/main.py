def compras(arq):
  doc=open(arq,'r')
  compras=doc.read().split('\n')
  doc.close()
  l_compras=[]
  total=0
  for item in compras:
    l_compras.append(item.split(';'))
  for cel in range(2,len(l_compras)-1):
    quantidade=l_compras[cel][1]
    preco=l_compras[cel][2]
    total=total+int(quantidade)*float(preco)
  return f'Preço total: {total:.2f}'


print(compras(r'_FACUL/AED_I/AED_I_-_2_Bi_Substitutiva/1/compras.csv'))