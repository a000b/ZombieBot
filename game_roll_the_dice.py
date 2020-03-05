import random

class Dice():
    def __init__(self, sides = 7):
        self.sides = sides

    def roll(self):
        return random.randrange(1,self.sides)

class Player():
    def __init__(self, name):
        self.name = name
        self.result = None

    def __repr__(self):
        return f'{self.name} result {self.result}'

class Game():
    def __init__(self, dice, player, house):
        self.player = player
        self.house = house
        self.dice = dice
        self.winner = None

    def play(self):
        self.house.result = self.dice.roll()
        self.player.result = self.dice.roll()
        if self.house.result == self.player.result:
            self.winner = "remis"
        elif self.house.result > self.player.result:
            self.winner = self.house.name
        else:
            self.winner = self.player.name

    def __repr__(self):
        if self.winner == "remis":
            return f'Remis!'
        else:
            return f'{self.winner} is the winner!'