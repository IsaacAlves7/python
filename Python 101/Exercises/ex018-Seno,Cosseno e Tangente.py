import math
an=float(input('Digite o Ângulo que voce deseja:'))
sen=math.sin(math.radians(an))
cos=math.cos(math.radians(an))
tan=math.tan(math.radians(an))
print('O angulo {:.0f}º tem o valor do SENO é {:.2f} , o valor do COSSENO é {:.2f} e o valor da TANGENTE é {:.2f}'.format(an,sen,cos,tan))