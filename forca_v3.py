# -*- coding: utf-8 -*-

# Jogo da forca
# POO

# importar arquivos
import random

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
        print('VAMOS COMEÇAR!!! \n================\n    HANGMAN\n================\n')
        self.qtdJogador = int(input('1 ou 2 Jogares? '))

    def palavra(self):
        if self.qtdJogador == 1:
            with open('palavras.txt', 'rt') as f: #lendo o arquivo txt do mesmo projeto
                self.banco = f.readlines()  # Colocou as palavras de cada linha como um elemento da lista
                self.word = (self.banco[random.randint(0, len(self.banco) - 1)]).strip()# Do módulo "random" utilizou o randint em um intervalo dentro do index da lista banco
                print('\n' * 100, '\n================\n    HANGMAN\n================\n')
        else:
            self.word = input('Jogador 2 digite uma palavra: ')
            print('\n'*100, '\n================\n    HANGMAN\n================\n')
            # depois precisa limpar pro jogador 1 não ler kkkkk
        self.acertou_letra = list(self.word)
        self.hide_letra = '-'*len(self.word)
        self.hide_list = list(self.hide_letra)

    def game_status(self):
        print('\n' * 100, '\n================\n    HANGMAN\n================\n')
        self.hide_letra = ''.join(self.hide_list)
        print(tabuleiro[len(hangman.errou_letra)])
        print('Palavra: {}'.format(self.hide_letra))

    def guess(self):
        while len(self.errou_letra) < 6 and '-' in self.hide_letra:
            self.letra = input('Chute uma letra: ')
            while self.letra in self.errou_letra or self.letra in self.hide_list:
                self.letra = input('ESSA LETRA JÁ FOI!!! \nChute outra letra: ')
            if self.letra not in self.word:
                self.errou_letra.append(self.letra)
                print(self.game_status())
            else:
                self.cont = 0
                for i in self.word:
                    if i==self.letra:
                        self.hide_list[self.cont] = self.letra
                        self.cont +=1
                    else:
                        self.cont += 1
                print(self.game_status())
        if len(self.errou_letra) ==6:
            print('LOSER!!!')
        else:
            print('GANHOU!!!')





hangman = Hangman()
hangman.palavra()
hangman.game_status()
hangman.guess()
