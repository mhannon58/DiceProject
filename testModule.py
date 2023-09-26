'''
Created on Apr 29, 2020

@author: 17818
'''
import random


class dice:
    value = 0
    dice1 = "-----\n|   |\n| * |\n|   |\n-----" 
    dice2 = "-----\n|  *|\n|   |\n|*  |\n-----"
    dice3 = "-----\n|  *|\n| * |\n|*  |\n-----"
    dice4 = "-----\n|* *|\n|   |\n|* *|\n-----"
    dice5 = "-----\n|* *|\n| * |\n|* *|\n-----"
    dice6 = "-----\n|* *|\n|* *|\n|* *|\n-----" 
    
    def roll(self):
        value =  random.randint(1,6)
        if value == 1:
            print(dice.dice1)
        if value == 2:
            print(dice.dice2)
        if value == 3:
            print(dice.dice3)
        if value == 4:
            print(dice.dice4)
        if value == 5:
            print(dice.dice5)
        if value == 6:
            print(dice.dice6)
        return value
        
    
     
        
isOver = False

myDi = dice()


while(isOver == False):
    print("Press 'r' to roll dice or Press 'q' to quit")
    char = input()
    if char == 'q':
        isOver = True
        print('Thank you, and goodbye')
    elif char == 'r':
        print("Enter number of die")
        diAmt = int(input())
        total = 0
        for x in range(diAmt):
            total += myDi.roll()
        print("Your total is " + str(total))
    else:
        print('Unsupported Action, Please try again')
        
      
       
    