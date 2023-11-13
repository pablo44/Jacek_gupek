#new die
import random


class Die:
#we get out of functionality in __int__ and keep it in func Die_roll not to cofuse in the main code and avoid duble running diffrent functionalities
#Die_roll fixes the confusion from roll_start function that got error while reading first random turns from __init__ instance method and Die_roll at the same time
    def __init__(self):
        self.value = None

    def Die_roll(self):
        self.value = random.randint(1,6)
        return self.value

    def __str__(self):
        return (f'Dice shows  {self.value}')

    
    
    

