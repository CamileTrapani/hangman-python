# -*- coding: utf-8 -*-

# Jogo da forca
# POO

# importar arquivos
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

#Classe
class Hangman:
      def __init__(self, word):  #isso aqui é um método
            self.word = word
            self.errou_letra = []
            self.acertou_letra = []

      def guess(self, letter):  #  para a pessoa chutar uma letra
                                # e o computador verificar se ela já foi utilizada
            if letter in self.word and letter not in self.acertou_letra:
                  self.acertou_letra.append(letter)
            elif letter not in self.word and letter not in self.errou_letra:
                  self.errou_letra.append(letter)
            else:
                  return False
            return True
            

      def forca_acabou(self):
            return self.forca_ganhou() or (len(self.errou_letra)==6)

      def forca_ganhou(self):
            if '_' not in self.hide_word():
                  return True
            return False

      def hide_word(self):
            rtn = ''
            for letter in self.word:
                  if letter not in self.acertou_letra:
                        rtn = '_'
                  else:
                        rtn = letter
            return rtn

      def print_game_status(self):
            print(board[len(self.errou_letra)])
            print('\nPalavra: '+self.hide_word())
            print('\nLetras erradas: ')
            for letter in self.errou_letra:
                  print(letter,' ', end='')
            print('Letras corretas:')
            for letter in self.acertou_letra:
                  prit(letter,' ', end='')

def rand_word():
      with open('palavras.txt', 'rt') as f:
            bank = f.readlines()
      return  bank[random.randint(0,len(bank))].strip()

def main():
      game = Hangman(rand_word())

      while not game.forca_acabou():
            game.print_game_status()
            user_input = input('\nDigite uma letra: ')
            game.guess(user_input)

      game.print_game_status()

      if game.forca_ganhou():
            print('Congrats you won!')
      else:
            print('Perdeu')
            print('A palavrra era:' + game.word)

if __name__ == '__main__':
      main()