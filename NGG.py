import random
def getRandomNumber():
    return random.randrange(1,100)
def giveHint(number,guess):
    if guess>(number+10) or guess<(number-10):
        return "You are far to find me! Keep try to find me!"
    elif number==guess:
        return 'You catched me!!'
    else:
        return "You are near to find me! Do another try to find me!"
def runGuess():
    secretNumber=getRandomNumber()
    while True:
        user_guess=int(input("Enter a number between 1 and 100: "))
        hint=giveHint(secretNumber,user_guess)
        if hint=="You catched me!!":
            print("You guessed it correctly!")
            break
        else:
            print(hint)
if __name__=='__main__':
    runGuess()