import random
import sys

win=0
lose=0
tie=0

while True:
  

    print("WIN="+str(win),"LOSE="+str(lose),"TIE="+str(tie))
    hum=int(input("enter the value 1)rock 2)paper 3)scissors 4)exit  "))
    if hum == 4:
            sys.exit()

    
    if hum == 1:
            print("your choice is ROCK")
    elif hum == 2:
            print("your choice is PAPER")
    elif hum == 3 :
            print("your chioce is SCISSORS")  
    guess=random.randint(1,3)
    if guess == 1 :
                comp="ROCK"
    elif guess == 2:
                comp="PAPER"
    elif guess == 3:
                comp="SCISSORS" 
    print("computer guess: ")
    print(comp)
    if guess == hum :
            print('TIE')
            tie+=1
    elif guess == 1 and hum == 2:
            print('YOU WON')
            win+=1
    elif guess == 2 and hum == 1:
            print('YOU LOST')
            lose+=1
    elif guess == 2 and hum == 3:
            print('YOU WON')      
            win+=1
    elif guess == 3 and hum == 1:
            print("YOU WON")
            win+=1
    elif guess == 1 and hum == 3:
            print("YOU LOST")
            lose+=1
    elif guess == 3 and hum == 2:
            print("YOU LOST")  
            lose+=1
    break
