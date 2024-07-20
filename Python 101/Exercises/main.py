import aleatorio as a
import media as m

lista = a.geraListaInteiro(2)
print('Minha lista:',lista)

media = m.media(lista)
mediana = m.mediana(lista)
moda = m.moda(lista)

print('Média:'+str(media))
print('Mediana:'+str(mediana))
print('Moda:'+str(moda))