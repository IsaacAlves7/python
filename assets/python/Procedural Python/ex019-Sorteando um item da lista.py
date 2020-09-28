import random
import emoji
print('O professor vai escolher um aluno como representante da turma!')
n1 = str(input('Primeiro aluno:'))
n2 = str(input('Segundo aluno:'))
n3 = str(input('Terceiro aluno:'))
n4 = str(input('Quarto aluno:'))
lista = [n1,n2,n3,n4]
escolhido=random.choice(lista)
print('O professor escolheu o {} como representante da turma'.format(escolhido))
print(emoji.emojize('Desenvolvido por Isaac Alves :skull::computer: ',use_aliases=True))