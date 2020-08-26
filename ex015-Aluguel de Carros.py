al=int(input('Quantos dias alugados?'))
km=float(input('Quantos Km rodados?'))
car=(60*al)+(0.50*km)
print('O total a pagar é de R${:.2f}'.format(car))