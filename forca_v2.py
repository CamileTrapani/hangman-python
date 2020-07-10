# -*- coding: utf-8 -*-

# Jogo da forca
# POO

# # importar arquivos
# import random

# Criar tabuleiro usando LISTA
tabuleiro=['''
 +----+
 |    |
      |
      |
      |
      |
==========''', '''
 +----+
 |    |
 O    |
      |
      |
      |
==========''','''
 +----+
 |    |
 O    |
 |    |
      |
      |
==========''', '''
 +----+
 |    |
 O    |
/|    |
      |
      |
==========''', '''
 +----+
 |    |
 O    |
/|\   |
      |
      |
==========''', '''
 +----+
 |    |
 O    |
/|\   |
/     |
      |
==========''', '''
 +----+
 |    |
 O    |
/|\   |
/ \   |
      |
==========''']

# Etapas
# inicial
# 1 ou 2 Jogadores
# escolha da palavra
# mostrar palavra e tabuleiro _ _ _ _
# chutar letra
# terminar o jogo

class Hangman:
    def __init__(self):
        self.errou_letra = []
        self.acertou_letra = []
        self.qtdJogador = 0
        self.word = []
        self.tracinho = []
        self.letra = []

    def jogadores(self):
        self.qtdJogador = int(input('1 ou 2 Jogares? '))

    def palavra(self):
        if self.qtdJogador == 1:
            self.word = 'baunilha' #palavra do banco de dados
        else:
            self.word = input('Jogador 2 digite uma palavra: ')
            # depois precisa limpar pro jogador 1 não ler kkkkk

    def hide(self):
        for self.letra in
        self.tracinho = '_ '*len(self.word)

    def chute(self):
        self.letra = input('Chute uma letra: ')
        while self.letra in self.errou_letra or self.letra in self.acertou_letra:
            self.letra = input('ESSA LETRA JÁ FOI!!! \nChute outra letra: ')
        if self.letra not in self.word:
            self.errou_letra.append(self.letra)
        else:
            self.acertou_letra

        # if self.errou_letra < 6:
        #     self.letra = input('Chute uma letra: ')
        #     while self.letra in self.errou_letra or self.letra in self.acertou_letra:
        #         self.letra = input('ESSA LETRA JÁ FOI!!! \nChute outra letra: ')
        #
        # else:


hangman = Hangman()
hangman.jogadores()
hangman.palavra()
hangman.hide()

print(hangman.word) #apagar isso depois

print(hangman.tracinho)
print(tabuleiro[len(hangman.errou_letra)])