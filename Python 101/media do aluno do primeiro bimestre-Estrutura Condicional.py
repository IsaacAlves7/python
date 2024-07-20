n1 = float(input('Digite a nota do teste:'))
n2 = float(input('Digite a nota da prova:'))
m = (n1 + n2)/2
if m >= 6.0:
    print('Parabéns!Sua media foi boa!')
else:
    print('Ops,parece que voce está de Recuperação')
    recup = float(input('Digite a nota da Recuperação:'))
if n1 <= 6.0 and n2 >= 6.0:
    recup = (n1 + n2)/2
if n2 <= 6.0 and n1 >= 6.0:
    recup = (n1 + n2) / 2
if recup >= 6.0:
    print('{}pts,conseguiu atingir a media!'.format(recup))
else:
    print('Com a media de {}pts,Voce não conseguiu atingir a media!'.format(recup))