
from Jacek_die import Die
from Jacek import YatzyGameClass
import pytest
# here we assum that first item in a ds list is predifined and it should send an error
def test_is_yahtzee_when_all_dice_matches():
    for i in range(5):
            d = Die()
            d.Die_roll()
            assert YatzyGameClass.ds[0].value == 2

#same here we assume that flag is true while it should be false and show error
def test_no_yahtzee_all_not_matching():
    while YatzyGameClass.intTurn < 3: 
                if len(YatzyGameClass.ds)== 0:
                    YatzyGameClass.roll_start()
                for j in range(1,5):    
                    if len(YatzyGameClass.ds) > 0 and YatzyGameClass.ds[j].value != YatzyGameClass.ds[j-1].value:
                        assert YatzyGameClass.flag == True


if __name__ == '__main__':
            pytest.main()