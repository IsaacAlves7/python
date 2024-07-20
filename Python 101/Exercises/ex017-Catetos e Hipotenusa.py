'''ca = float(input('Digite o valor do Cateto Adjacente:'))
co = float(input('Digite o valor do Cateto Oposto:'))
hip = (ca**2)+(co**2)**(1/2)
print('O valor da Hipotenusa é {:.2f}'.format(hip))'''
'''import math
ca = float(input('Digite o valor do Cateto Adjacente:'))
co = float(input('Digite o valor do Cateto Oposto:'))
hip = math.hypot(ca,co)
print('O valor da Hipotenusa é {:.2f}'.format(hip))'''
from math import hypot
ca = float(input('Digite o valor do Cateto Adjacente:'))
co = float(input('Digite o valor do Cateto Oposto:'))
hip = hypot(ca,co)
print('O valor da Hipotenusa é {:.2f}'.format(hip))
