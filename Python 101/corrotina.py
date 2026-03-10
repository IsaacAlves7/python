# -*- coding: utf-8 -*-
"""
Created on Tue May 25 10:38:51 2021

@author: smonteiro
"""
# Exemplo de co-rotina 
def imprimir_nome(nome):
	print("Procurando Nome:{}".format(nome))
	while True:
		texto_entrada = (yield)
		if nome in texto_entrada:
			print(nome, "foi encontrado no texto: ",texto_entrada)

# Chamando co-rotina. Nada irá acontecer.
co_rotina = imprimir_nome("teste")
# Isso iniciará a execução da co-rotina e
# Imprime a primeira linha "Procurando Nome ..."
# e avançar a execução para "yield"

co_rotina.__next__()

# Enviando entradas
co_rotina.send("teste 1")
co_rotina.send("teste 2")
co_rotina.send("este 3")
