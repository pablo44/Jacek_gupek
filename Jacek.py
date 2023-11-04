#new game try one
from Jacek_die import Die


class YatzyGameClass:

    def __init__(self):
        self.ds = [Die(), Die(), Die(), Die(),Die()]
        self.goOn = True
        self.intTurn = 0


    def yatzy_go(f):
        #while YatzyGameClass.goOn == True:
            #YatzyGameClass.intTurn = 0
# here we should have some start and stop option in order to control the function my_yatzy
        #flag = True
        #initialise "flag" as a boolean variable to control the loop logic and becomes as " stop button"
        def wrapper(self):
            flag = True

# here comes while loop to wrapp the conditions of the game:
            while self.intTurn < 3:
                for j in range(1,5):
                    if self.ds[j].value != self.ds[j-1].value:
                        flag == False
                if flag == True:
                    print(f'You got Yatzy in {self.ds[0].value}s')
                    return
                elif self.intTurn != 2:
                    if input('want to throw again?( "y" for yes anything else for no)') == 'y':
                        self.intTurn += 1
                        self.roll_start()
                    else:

                        self.goOn = not self.goOn
                        break
                else:
                    if input( 'Game Over want to play again?')== 'y':
                        self.intTurn = 0
                    else:
                        self.goOn = not self.goOn
                    break
            result = f(self)
            return result               
        
        return wrapper
    
    def roll_start(self):

        print('Welcome to Yahtzee')
    
        print(f'starting turn: {self.intTurn +1} of 3, rolling dice')
        #while len(self.ds) < 6:
        for i, d in enumerate(self.ds, 1):
            d.Die_roll()
            print(f'{i}, {d}')
                #self.ds.append(turn)


    

    #creating en decorator in order to reuse this func my_yatzy in a another function-yatzy_go to modifie game conditions inuti this function's wrapper
    @yatzy_go
    def my_yatzy(self):
        while self.goOn:
            print(self.roll_start())
#we move the control function to decorator yatzy_go so while loop is there, here is only basic function that runs and the control is in the decorator
            
            #return self.my_yatzy
        
def main():
    game = YatzyGameClass()
    game.my_yatzy()


if __name__ == '__main__':
        main()



