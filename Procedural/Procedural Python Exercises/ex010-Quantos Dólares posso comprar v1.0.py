print('R$->US$')
print('-------')
real=float(input('Digite a sua quantia em reais:R$'))
dolar=float(input('Quanto vale o dólar ATUALMENTE?US$'))
carteira=real/dolar
print('')
print('Com R${:.2f} voce pode comprar US${:.2f}'.format(real,carteira))