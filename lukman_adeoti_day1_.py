import random

guessesInput = 0

print('Hello! What is your name?')
myName = input()

numberGuess = random.randint(1, 100)
print('Well, ' + myName + ', I am thinking of a number between 1 and 100.')

while guessesInput < 6:
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    guessesInput = guessesInput + 1

    if guess < numberGuess:
        print('Your guess is too low.')

    if guess > numberGuess:
        print('Your guess is too high.')

    if guess == numberGuess:
        break

if guess == numberGuess:
    guessesInput = str(guessesInput)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesInput + ' guesses!')

if guess != numberGuess:
    numberGuess = str(numberGuess)
    print('Nope. The number I was thinking of was ' + numberGuess)
