import random
from turtle import clear

class Die:
    __roll_value = 1

    def roll(self):
        self.__roll_value = random.randint(1,6)

    def get_rolled_value(self):
        return self.__roll_value

    def __str__(self):
        return 'The rolled value is: ' + format(self.__roll_value)
