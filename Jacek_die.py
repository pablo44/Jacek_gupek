#new die
import random


class Die:
#we get out of functionality in __int__ and keep it in func Die_roll not to cofuse in the main code and avoid duble running diffrent functionalities
    def __init__(self):
        self.value = None

    def Die_roll(self):
        self.value = random.randint(1,6)
        return self.value

    def __str__(self):
        return (f'Dice shows  {self.value}')

    
    
    

