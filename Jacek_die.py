#new die
import random


class Die:

    def __init__(self):
        self.value = None

    def Die_roll(self):
        self.value = random.randint(1,6)
        return self.value

    def __str__(self):
        return (f'Dice shows  {self.value}')

    
    
    

