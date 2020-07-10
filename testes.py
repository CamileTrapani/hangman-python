# palavra = 'baunilha'
# tracinho = '_ '*len(palavra)
# print(tracinho)


import random
import os

with open('palavras.txt', 'rt') as f:
    banco = f.readlines() # Colocou as palavras de cada linha como um elemento da lista
    print(banco)
    palavra = (banco[random.randint(0, len(banco)-1)]).strip() # Do módulo "random" utilizou o randint em um intervalo dentro do index da lista banco
    print(palavra)
    print(len(palavra))

    print(list(palavra))
# palavra = 'palavra'
# print(palavra)
# letra = list(palavra)
# print(letra)


lista = ['M','i','l','e']
print(lista)
lista[2] = 't'
nome = ' '.join(lista)
print(nome)


