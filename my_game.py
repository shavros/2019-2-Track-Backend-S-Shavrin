# -*- coding: utf-8 -*-
'''ага'''
from __future__ import print_function

class Game(object):
    '''Класс игры крестики -нолики'''
    game_field = None
    player_X = None
    player_O = None
    is_game_finished = None
    whose_turn = None
    is_input = None
    winner = None

    def __init__(self, name):
        self.name = name

    def start_game(self):
        '''Создает новую игру, обнуляет результаты старой игры'''
        self.game_field = list(range(1, 10))
        self.player_X = input('Введите имя игрока, играющего за крестики: ')
        self.player_O = input('Введите имя игрока играющего за нолики: ')
        f = True
        while f:
            if self.player_O == self.player_X:
                self.player_O = (input('Это имя занято, введите другое: '))
            if self.player_O != self.player_X:
                f = False
        print('Приятной игры, думайте, будьте внимательны и побеждайте!')
        for i in range(3):
            print('|', self.game_field[0 + i * 3], '|', self.game_field[1 + i * 3], '|', self.game_field[2 + i * 3], '|')
            print('____________')
        self.whose_turn = self.player_X
        self.is_game_finished = False

    def test_of_input(self):
        '''Проверяет пользовательский ввод, чтобы он соответствовал требованиям игры'''
        if (not self.is_input.isdigit()) or (int(self.is_input) <= 0) or (int(self.is_input) >= 10) or \
                (self.game_field[int(self.is_input) - 1] == 'X') or (self.game_field[int(self.is_input) - 1] == 'O'):
            return False

        return True

    def new_turn(self, player):
        '''Это метод хода, ставит в выбранную ячейку крестик или нолик'''
        if player == self.player_X:
            self.is_input = input('Введите цифру, на место которой хотите поставить крестик: ')
        elif player == self.player_O:
            self.is_input = input('Введите цифру, на место которой хотите поставить нолик: ')
        s = self.test_of_input()
        while not s:
            self.is_input = input('''Пожалуйста, введите зниачение, удовлетворяющее требованиям:
            число от 1 до 9
            клетка не занята крестиком или ноликом
            ''')
            s = self.test_of_input()
        if player == self.player_X:
            self.game_field[int(self.is_input) - 1] = 'X'
            print('{name} поставил/a крестик на клетку {number}'.format(name=player, number=int(self.is_input)))
        elif player == self.player_O:
            self.game_field[int(self.is_input) - 1] = 'O'
            print('{name} поставил/a нолик на клетку {number}'.format(name=player, number=int(self.is_input)))
        for i in range(3):
            print('|', self.game_field[0 + i * 3], '|', self.game_field[1 + i * 3], '|', self.game_field[2 + i * 3],
                  '|')
            print('____________')
        if self.whose_turn == self.player_X:
            self.whose_turn = self.player_O
        elif self.whose_turn == self.player_O:
            self.whose_turn = self.player_X

    def finish_checking(self):
        '''Проверяет, не закончилась ли игра победой одного из
        игроков или ничьей'''
        if self.game_field[0] == self.game_field[1] == self.game_field[2] or \
                self.game_field[3] == self.game_field[4] == self.game_field[5] or \
                self.game_field[6] == self.game_field[7] == self.game_field[8] or \
                self.game_field[0] == self.game_field[3] == self.game_field[6] or \
                self.game_field[1] == self.game_field[4] == self.game_field[7] or \
                self.game_field[2] == self.game_field[5] == self.game_field[8] or \
                self.game_field[0] == self.game_field[4] == self.game_field[8] or \
                self.game_field[2] == self.game_field[4] == self.game_field[6]:
            if self.whose_turn == self.player_X:
                self.winner = self.player_O
            elif self.whose_turn == self.player_O:
                self.winner = self.player_X
            self.is_game_finished = True
        elif self.game_field.count('X') + self.game_field.count('O') == 9:
            self.winner = 'draw'
            self.is_game_finished = True

    def game_process(self):
        '''Основной метод, ответсвенный за ход игры, запускает все остальные методы в нужном для игры порядке'''
        self.start_game()
        while not self.is_game_finished:
            self.new_turn(self.whose_turn)
            self.finish_checking()
        if self.winner == 'draw':
            print('Игра закончилась в ничью, {player_1} и {player_2} молодцы!'
                  .format(player_1=self.player_X, player_2=self.player_O))
        else:
            print('Победил {player}, поздравляем!'.format(player=self.winner))
        question = input('Желаете сыграть еще разок? Если да - введите да, если нет - Hет.')
        if question == 'Да':
            self.game_process()
        elif question == 'Нет':
            print('Пока :)')


TIC_TOC_GAME = Game('My_Game')
TIC_TOC_GAME.game_process()
