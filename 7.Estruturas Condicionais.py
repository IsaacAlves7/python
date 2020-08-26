'''ESTRUTURAS CONDICIONAIS'''

#Realiza testes condicionais
#Realiza se uma determinada condição for atendida
#Avalia se a condição é verdadeira ou não

'''SINTAXE'''
#BLOCO->Trecho de código que depende de outro trecho
'''INDENTAÇAO'''
#No Python blocos são definidos pelo espaçamento da linha
#Pode ser feito com espaços ou tabulações
#Tecla TAB

# if condição:
#    execute_esta_linha
print('COMANDO IF')
x = 1
y = 100000000

if x > y:
    print('x é maior que y')
if y > x:
    print('y é maior que x')

"""Comando ELSE"""
#Executado caso a condição do comando if não seja atendida
print('COMANDO ELSE')
x = 1
y = 2

if x > y:
    print('x maior que y')
else:
    print('x não é maior que y')

'''Comando ELIF'''
#Caso haja necessidade de mais condições entre o if e o else

#if condição:
#    execute_esta_linha
#elif condição:
#    execute_esta_linha
#else:
#    execute_esta_linha

print('Comando ELIF')
x = 1
y = 2

if x == y:
    print('Numeros iguais')
elif x > y:
    print('x maior que y')
elif y > x:
    print('y maior que x')
else:
    print('Numeros diferentes')

