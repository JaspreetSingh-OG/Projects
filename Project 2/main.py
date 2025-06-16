#Number Guessing Game
from random import randint
n=randint(1,100)
a=-1
guesses=0
while(a!=n):
    a=int(input("Guess the number:"))
    if a>n:
        print("Lower number please!")
        guesses+=1
    elif a<n:
        print("Higher number please")
        guesses+=1
print(f"You've Guessed the number {n} correctly in {guesses} attempts")