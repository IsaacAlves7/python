rs=float(input('Qual é o preço do produto? R$'))
p=int(input('Qual é a taxa de desconto? %'))
desc= rs-(rs*p/100)
print('O produto que custava R${:.2f},com a taxa de desconto de {}% a promoção vai custar R${:.2f}'.format(rs,p,desc))
