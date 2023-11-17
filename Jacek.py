#new game try one
from Jacek_die import Die

#in general code is devided in a structure so it is like this: basic game my_yatzhy is send to another function -decorator yatzy_go and ther it is run and undercontrol of diffret conditions. function my_yatzy uses a little helpin function on it's run-roll_start

#all the decorator's code should be outside a class
def yatzy_go(f):
        
        def wrapper(self):
            flag = True

# here comes while loop to wrapp the conditions of the game:
            while self.intTurn < 3: 
                if len(self.ds)== 0:
                    self.roll_start()
                for j in range(1,5):    
                    if len(self.ds) > 0 and self.ds[j].value != self.ds[j-1].value:
                        flag = False
                        
                if flag:
                    print(f'You got Yatzy in {self.ds[0].value}s')
                    return
                elif self.intTurn != 2:
                    if input('want to throw again?( "y" for yes anything else for no)') == 'y':
                        self.intTurn += 1
                        self.roll_start()
                    else:

                        self.goOn = not self.goOn
                        break
                    #to avoid infinit loop after game over since we are calling roll_start, we call the whole game instead by calling main() and setting constraint int.Turn<3 to avoid infinit loop-everything here is a secure the game since the intTurn variable is not exactly clear thought over in my game logic
                else:
                    if input( 'Game Over want to play again?')== 'y':
                        while self.intTurn < 3:
                            main()                      
                      
                    else:
                        self.goOn = not self.goOn
                    break
            result = f(self)
            return result               
        
        return wrapper



class YatzyGameClass:

    def __init__(self):
        self.ds = []
        self.goOn = True
        self.intTurn = 0    
    
    
    def roll_start(self):
                
        for i in range(5):
            d = Die()
            d.Die_roll()
            self.ds.append(d)
            print(f'{i+1}, {d}')     
            
             
           
    
    #creating en decorator in order to reuse this func my_yatzy in a another function-yatzy_go to modifie game conditions inuti this function's wrapper
    @yatzy_go
    def my_yatzy(self):
        while self.goOn:
            print(f'starting turn: {self.intTurn +1} of 3, rolling dice')
            self.roll_start()
    #we move the control function to decorator yatzy_go so while loop is there, here is only basic function that runs and the control is in the decorator
          
           
        
def main():
    print('Welcome to Yahtzee')
    game = YatzyGameClass()
    game.my_yatzy()


if __name__ == '__main__':
        main()



