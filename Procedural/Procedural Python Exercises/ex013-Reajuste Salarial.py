sal=float(input('Digite seu salário: R$'))
p=int(input('Digite a taxa de aumento: %'))
reaj=sal+(sal * p/ 100)
print('Voce ganhava um salário de R${:.2f} e a sua taxa de aumento é de {}%,então, seu salário aumentou para R${:.2f}'.format(sal,p,reaj))