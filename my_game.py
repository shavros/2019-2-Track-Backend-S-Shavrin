class Game(object):
    game_field = None
    player_X = None
    player_O = None
    is_game_finished = None
    whose_turn = None
    is_chosed = None

    def __init__(self, name):
        self.name = name

    def start_game(self):
        self.game_field = list(range(1,10))
        self.player_X = input('Введите имя игрока, играющего за крестики: ')
        self.player_O = input('Введите имя игрока играющего за нолики: ')
        print('Приятной игры, думайте, будьте внимательны и побеждайте!')
        for i in range (3):
            print('|', self.game_field[0 + i * 3], '|', self.game_field[1 + i * 3], '|', self.game_field[2 + i * 3], '|')
            print('____________')
        self.whose_turn = self.player_X
        self.is_game_finished = False

    def test_of_choosed(self):
        if 9 < self.is_chosed < 1 or self.game_field[self.is_chosed - 1] == 'X' or self.game_field[self.is_chosed - 1] == 'O' or type(self.is_chosed) != int:
            return False
        else:
            return True

    def new_turn(self, player):
        if player == self.player_X:
            self.is_chosed = int(input('Введите цифру, на место которой хотите поставить крестик: '))
        elif player == self.player_O:
            self.is_chosed = int(input('Введите цифру, на место которой хотите поставить нолик: '))
        while not self.test_of_choosed():
            self.is_chosed = int(input('''Пожалуйста, введите зниачение, удовлетворяющее требованиям:
            число от 1 до 9
            клетка не занята крестиком или ноликом'''))
        if player == self.player_X:
            self.game_field[self.is_chosed - 1] = 'X'
            print('{name} поставил/a крестик на клетку {number}'.format(name = player, number = self.is_chosed))
        elif player == self.player_O:
            self.game_field[self.is_chosed - 1] = '0'
            print('{name} поставил/a нолик на клетку {number}'.format(name=player, number=self.is_chosed))
        for i in range(3):
            print('|', self.game_field[0 + i * 3], '|', self.game_field[1 + i * 3], '|', self.game_field[2 + i * 3],
                  '|')
            print('____________')
        if self.whose_turn == self.player_X:
            self.whose_turn = self.player_O
        elif self.whose_turn == self.player_O:
            self.whose_turn = self.player_X

    def game_process(self):
        self.start_game()
        while not self.is_game_finished:
            self.new_turn(self.whose_turn)




tic_toc_game = Game('My_Game')
tic_toc_game.game_process()
