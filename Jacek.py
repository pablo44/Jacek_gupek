#new game try one
from Jacek_die import Die


class YatzyGameClass:

    def __init__(self):
        self.ds = [Die(), Die(), Die(), Die(),Die()]
        self.goOn = True


    def my_yatzy(self):
        while self.goOn == True:
            intTurn = 0

            print('Welcome to Yahtzee')
            while intTurn < 3:
                print(f'starting turn: {intTurn +1} of 3, rolling dice')
                for i, d in enumerate(self.ds, 1):
                    print(f'{i}, {d}')
            return my_yatzy


