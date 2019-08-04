#!/usr/bin/python3
import random


"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""


class Card:
    def __init__(self):
        self.card = [[], [], []]

    def __repr__(self):
        result = ''

        for row in self.card:
            for column in row:
                result += str(f'{column:>3} ')
            result += '\n'
        return result

    def prepare_card(self):
        for row in self.card:
            for column in range(0, 10):
                row.append(' ')

        numbers = random.sample(range(1, 91), 15)

        start = 0
        end = 5
        for row in self.card:
            positions = sorted(random.sample(range(9), 5))
            n_sorted = sorted(numbers[start:end])
            for i, column in enumerate(positions):
                row[column] = n_sorted[i]
            start += 5
            end += 5

    def has_any_numbers(self):
        return len([column for row in self.card for column in row if type(column) == int]) > 0

    def cross_out(self, number):
        for row in self.card:
            for i, column in enumerate(row):
                if(number == column):
                    row[i] = '_'
                    return True
        return False

    def has_number(self, number):
        for row in self.card:
            for i, column in enumerate(row):
                if (number == column):
                    return True
        return False


class LotoGame:
    def __init__(self, player_card, ai_card):
        self.player_card = player_card
        self.ai_card = ai_card
        self.barrels = []

    def show_stat_game(self, i, barrel):
        print(f"\nНовый бочонок: {barrel}. Осталось: {len(self.barrels) - i - 1}")
        print("----------- Ваша карточка ----------")
        print(self.player_card)
        print("------------------------------------")
        print("------- Карточка компьютера --------")
        print(self.ai_card)
        print("------------------------------------")

    def player_move(self, barrel):
        while True:
            answer = input("Зачеркнуть цифру? (y/n)\nq - выход\n")
            if answer == 'y':
                if not self.player_card.cross_out(barrel):
                    print("Данной цифры нет в карточке. Вы проиграли")
                    exit()
                break
            elif answer == 'n':
                if self.player_card.cross_out(barrel):
                    print("Данная цифра есть в карточке. Вы проиграли")
                    exit()
                break
            elif answer == 'q':
                exit()

    def ai_move(self, barrel):
        if self.ai_card.has_number(barrel):
            print(f"\nКомпьютер зачеркнул цифру {barrel}")
            self.ai_card.cross_out(barrel)
        else:
            print(f"\nКомпьютер не зачеркнул цифру {barrel}")

    def check_victory(self):
        if not self.player_card.has_any_numbers() and not self.ai_card.has_any_numbers():
            print("У вас ничья!")
            return True
        elif not self.player_card.has_any_numbers():
            print("Вы выиграли!")
            return True
        elif not self.ai_card.has_any_numbers():
            print("Вы выиграли!")
            return True
        return False

    def start_game(self):
        self.barrels = random.sample(range(1, 91), 90)
        print("Начало игры.")

        for i, barrel in enumerate(self.barrels):
            self.show_stat_game(i, barrel)
            self.player_move(barrel)
            self.ai_move(barrel)
            if self.check_victory():
                return


player_card_game = Card()
player_card_game.prepare_card()

ai_card_game = Card()
ai_card_game.prepare_card()

loto = LotoGame(player_card_game, ai_card_game)
loto.start_game()
