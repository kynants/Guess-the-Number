import random   # Used to generate a random number

for x in range(1):
    randNum = random.randint(1, 6)

userInput = int(input('Enter a random number between 1 and 5: '))

while userInput != randNum:
    userInput = int(input('Try again: '))

if userInput == randNum:
    print('Correct!')