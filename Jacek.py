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
        #initialise flag as a boolean variable to control the loop logic and becomes as " stop button"
        def wrapper(self):
            flag = True

# here comes while loop to wrapp the conditions of the game:
            while self.intTurn < 3:
                for j in range(1,5):
                    if YatzyGameClass.ds[j].value != YatzyGameClass.ds[j-1].value:
                        flag == False
                if flag == True:
                    print(f'You got Yatzy in {YatzyGameClass.ds[0].value}s')
                    return
                elif YatzyGameClass.intTurn != 2:
                    if input('want to throw again?( "y" for yes anything else for no)') == 'y':
                        YatzyGameClass.intTurn =+ 1
                    else:

                        YatzyGameClass.goOn != YatzyGameClass.goOn
                        break
                else:
                    if input( 'Game Over want to play again?')== 'y':
                        YatzyGameClass.intTurn = 0
                    else:
                        YatzyGameClass.goOn = not YatzyGameClass.goOn
                    break
            result = f(YatzyGameClass.intTurn)
            return result               
        
        return wrapper


    

    #creating en decorator in order to reuse this func my_yatzy in a another function-yatzy_go to modifie game conditions inuti this function's wrapper
    @yatzy_go
    def my_yatzy(self):
        while self.goOn == True:
            intTurn = 0

            print('Welcome to Yahtzee')
            while intTurn < 3:
                print(f'starting turn: {intTurn +1} of 3, rolling dice')
                for i, d in enumerate(self.ds, 1):
                    print(f'{i}, {d}')
            return YatzyGameClass.my_yatzy
        
def main():
    YatzyGameClass()
    if __name__ == '__main__':
        main()



