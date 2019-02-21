from __future__ import print_function
import random


#########################################################################
############ functions

global count
        
def welcome():
    print("**************************************************************************************")
    print("*********************** Welcome to the slot machine program **************************")
    print("**************************************************************************************")

def play():
    print()
    print("******************************* Spinning Wheel ***************************************")
    print()
    wheels[0] = random.randint(1,3) 
    wheels[1] = random.randint(1,3) 
    wheels[2] = random.randint(1,3) 


def draw():
    print("************************** You Spun these numbers ************************************")
    print()
    print()
    print()
    print()
    print(wheels[0], '|', wheels[1], '|', wheels[2])   


def check_win():
        count = -1
        while (count <= 8):
            count += 1
            if wheels == jackpots[count]:
                print("win")
                break
            elif count > 8:
                print("lose")
                break



'''
    print(wheels)
    if wheels == jackpots[0]:
        print("win")
    elif wheels == jackpots[1]:
        print("win")
    elif wheels == jackpots[2]:
        print("win")
    elif wheels == jackpots[3]:
        print("win")
    elif wheels == jackpots[4]:
        print("win")
    elif wheels == jackpots[5]:
        print("win")
    elif wheels == jackpots[6]:
        print("win")
    elif wheels == jackpots[7]:
        print("win")
    elif wheels == jackpots[8]:
        print("win")
    elif wheels == jackpots[9]:
        print("win")
    else:
        print("lose")
'''








#########################################################################
############ program

wheels = [1, 1, 1]

jackpots = [[1, 1, 1], [1, 2, 1], [1, 2, 3], [1, 3, 1], [2, 1, 2], [2, 2, 2], [2, 3, 2], [3, 1, 3], [3, 2, 3], [3, 3, 3] ]

welcome()
play()
draw()
check_win()
