# Create a program that allows a user to input an integer that calls a collatz()
# function on that number until the function returns the value 1.
import time

userInput = ''

def collatz(number):
    global userInput
    evaluateNumber = number % 2
    if evaluateNumber == 0:
        userInput = number // 2
        print(number)
    elif evaluateNumber == 1:
        userInput = 3 * number + 1
        print(number)

while userInput == '':
    try:
        userInput = int(input('Enter an integer other than 1.'))
    except ValueError:
        print('Not a valid integer. Please enter an integer other than 1.')

while userInput != 1:
    collatz(userInput)
    time.sleep(.25) #Pause for .25 seconds
else:
    print(userInput)

        #if number = even, then print number // 2
        #if number = odd, then print 3 * number + 1



