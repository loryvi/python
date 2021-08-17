import random

print("Hi whats your name?")        
name=input()
print("Nice you meet you,",name,"Let's play a game")
print("I will guess a number (1-20) and you have to guess it")
y=random.randint(1,20)
guesses=0
while(guesses<6):
    print("take a guess")
    x=input()
    x=int(x)
    guesses=guesses+1
    if (x==y):
        print("You guessed it congrats!")
        break;
    if (x>y):
        print("The number is more than what you guessed!")
    if (x<y):
        print("The number is less than what you guessed!")
if (x==y):
    print("You guessed it after",guesses,"times")
if (x!=y):
    print("please try again")
