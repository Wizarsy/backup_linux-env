#coding=UTF-8
horas=int(input('Informe o horário de partida (horas): '))
minutos=int(input('Informe o horário de partida (minutos): '))
viagem_horas=int(input('Informe o tempo de viagem (horas): '))
viagem_minutos=int(input('Informe o tempo de viagem (minutos): '))
fuso=int(input('Informe o fuso horário: '))

chegada_horas=horas+viagem_horas
chegada_minutos=minutos+viagem_minutos
chegada_horas-=fuso

if chegada_horas > 24:
  chegada_horas%=24
print('O horário previsto para chegada no destino é {0}:{1}'.format(chegada_horas,chegada_minutos))