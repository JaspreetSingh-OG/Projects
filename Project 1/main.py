#Snake,Water,Gun Game
'''
1 for Snake
-1 for Water
0 for Gun
'''
import random
computer=random.choice([-1,0,1])
user=input("Enter your choice (s/w/g): ")
gameDict={"s":1,"w":-1,"g":0}
revDict={1:"Snake",0:"Gun",-1:"Water"}
you=gameDict[user]
print(f"You Choose {revDict[you]}\nComputer Chooses {revDict[computer]}")
if computer==you:
    print("It's a Draw!")

elif (computer==-1 and you==1) or (computer==1 and you==0) or (computer==0 and you==-1):
    print("You Win!")

else:
    print("You Lose!")