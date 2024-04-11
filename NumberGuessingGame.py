# Number guessing game
import random
import math

a=int(input("Enter lower bound :- "))
b=int(input("Enter uper bound :- "))

x=random.randint(a,b)

chances=round(math.log(b-a+1,2))
print("You have ",chances," to guess the number")
while chances>0:
    guess=int(input("Guess the number..."))
    if guess == x:
        print("Success you guess is correct")
        break
    elif guess > x:
        print("your guess is max")
    elif guess < x:
        print("your guess is small")
    chances-=1

if chances==0:
    print("Sorry, You have no more chances to guess ",x)