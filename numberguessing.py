import random,sys
n=random.randint(1,100)
tries=1

while True:
    z=int(input("you have to select a number from 1 to 100 or enter 1000 to exit "))
    if z==1000:
     sys.exit()
    print(f'tries {tries}')
    if z>n:
            print("your guess is high please select a number lesser ")
            tries+=1
    elif z<n:
            print("your guess is low please select a number higher")
            tries+=1
            
    elif z==n:
            print("the number you guessed is correct")   
            print("YOU WON")
             
            break    
      
         