nome = str(input('Digite seu nome:'))
idade = int(input('Digite sua idade:'))
if idade >= 18:
  print(nome,"voce é maior de idade")
elif idade > 0 and idade < 18:
  print(nome,"voce é menor de idade")
if idade <= 0:
  print('Idade Invalida!')