#Area de Preenchimento de dados
aluno = str(input('Digite o nome completo do aluno:'))
Matricula = float(input('Digite sua matrícula:'))
print('')

#Media do Primeiro Bimestre
t1 = float(input('Digite a nota do teste1:'))
p1 = float(input('Digite a nota da prova1:'))
primeiro_bimestre =(t1+p1)/2
print('1ºBim:',primeiro_bimestre)
print('')

#Media do Segundo Bimestre
t2 = float(input('Digite a nota do teste2:'))
p2 = float(input('Digite a nota da prova2:'))
segundo_bimestre =(t2+p2)/2
print('2ºBim:',segundo_bimestre)
print('')

#Recuperação Semestral
mb = primeiro_bimestre + segundo_bimestre >= 12.0:
    print(aluno,'- Situação:Cursando')

if mb < 12.0:
    print(aluno,'- Situação:Recuperação')
    rec = float(input('Digite a nota da recuperação:'))
if rec >= 6.0:
    print(aluno,'- Situação:Cursando')
else:
    print('')
    print(aluno,'- Situação:Abaixo da Média')
    print('')

#Media do Terceiro Bimestre
t3 = float(input('Digite a nota do teste3:'))
p3 = float(input('Digite a nota da prova3:'))
terceiro_bimestre =(t3+p3)/2
print('3ºBim',terceiro_bimestre)
print('')

#Media do Quarto Bimestre
t4 = float(input('Digite a nota do teste4:'))
p4 = float(input('Digite a nota da prova4:'))
quarto_bimestre =(t4+p4)/2
print('4º',quarto_bimestre)
print('')

#Resultado Final
rf = primeiro_bimestre + segundo_bimestre + terceiro_bimestre + quarto_bimestre
rf >= 24

if rf < 24:
    print(aluno,'- Situação:Recuperação')
    rec2 = float(input('Digite a nota da Prova Final:'))
    rec2 = primeiro_bimestre or segundo_bimestre or terceiro_bimestre or quarto_bimestre < 6.0
if rec2 >= 6.0:
    print('')
    print(aluno,'- Situação:Aprovado')
else:
    print('')
    print(aluno,'- Situação:Reprovado')