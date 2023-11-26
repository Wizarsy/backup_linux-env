def credito(valor, parcelas):
  juros = parcelas * 2
  valor_juros = valor // juros
  valor_final= valor + valor_juros
  valor_parcelas = valor_final // parcelas
  return valor_parcelas
print(credito(1000,5))