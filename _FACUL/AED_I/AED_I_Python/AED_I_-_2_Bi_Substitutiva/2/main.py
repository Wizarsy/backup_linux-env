def segundo_bimestre(aluno,avaliacao):
  aluno=open(aluno,'r')
  alunos=aluno.read().split('\n')
  aluno.close()
  avaliacao=open(avaliacao,'r')
  notas=avaliacao.read().split('\n')
  avaliacao.close()
  l_alunos=[]
  l_notas=[]
  final=['matricula','nota final']
  for a in alunos:
    l_alunos.append(a.split(';'))
  for n in notas:
    l_notas.append(n.split(';'))
  for celx in range(1,len(l_alunos)-1):
    for cely in range(1,len(l_notas)):
      if l_alunos[celx][1] == l_notas[cely][0]:
        final.append(l_alunos[celx][0])
        if l_notas[cely][1] >= l_notas[cely][2]:
          final.append(l_notas[cely][1])
        else:
          final.append(l_notas[cely][2])
  arq_fim=open(r'_FACUL/AED_I/AED_I_-_2_Bi_Substitutiva/2/arq_final.csv','w')
  vezes=0
  for cel in range(len(final)):
    arq_fim.write(final[cel])
    vezes+=1
    if vezes >= 2:
      vezes=0
      arq_fim.write('\n')
    else:
      arq_fim.write(';')
  arq_fim.close()


segundo_bimestre(r'_FACUL/AED_I/AED_I_-_2_Bi_Substitutiva/2/aluno.csv', r'_FACUL/AED_I/AED_I_-_2_Bi_Substitutiva/2/avaliacao.csv')
