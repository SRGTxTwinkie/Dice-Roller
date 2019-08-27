from random import randint ### Given

def diceNumber(): ### Takes the number of dice, Obv.
    x = True
    print('How many dice would you like to roll?')  
    while  x == True:

        diceNum = input('Number: ')
        
        try: ### Makes sure you put a number in
            diceNumber = int(diceNum)
            x = False
        except:
            print('Please put in a number')
            x = True
    rollCommand(diceNumber)

def rollCommand(diceNumber): ### Just an in-between, for to feel like you're actually doing something  
    num = diceNumber
    input('Press any button to roll!')
    print('Rollin!')
    roll(num)
    
def roll(num): ### Rolls the dice, also I just noticed that I took num variable thru 3 functions
    sumList = [] ### List for the adding up the sum at the end
    x = True  
    while num > 0:
        sumList.append(randint(1,6)) ### Puts all the numbers in the sumList
        num -= 1 ### Litteraly don't know what this does, I can't figure it out
    for i in sumList:
        print(i)
    print('The sum of your roll is...')
    print(sum(sumList))
    while x == True: ### Just a go again, probably should have been a new function, but oh well
        userAnswer = input('Would you like to go again? Y/N: ')
        if userAnswer.upper() == 'Y':
            diceNumber()
        elif userAnswer.upper() != 'N':
            print('Goodbye!')
            kill()
diceNumber()
