import sys
count =1
while True:
        c=input("Enter the operator,To exit enter 0 : ") 
        if c=="0":
                sys.exit()      
        a=int(input("Enter the first operand : "))
        b=int(input("Enter the second operand : "))
        
        print(f"You selected this : {c}")
        print(f"operation{count}")
        count+=1
        if c=="+":
                print(f"performing addition  {a}+{b}:",end='')
                print(a+b)
                
                
        elif c=="-":
                print(f"performing subtraction  {a}-{b}:",end='')    
                print(a-b)
                

        elif c=="*":
                print(f"performing multiplication {a}*{b}:",end='')    
                print(a*b)
                
        elif c=="/":
                if b ==0:
                        print("error occured,not divisible by 0") 
                else:
                        print(f"performing divison {a}/{b}:",end='')
                        print(a/b)
                        
        elif c=="%":
                print(f"performing modulo operator {a}%{b}:",end='')
                print(a%b) 
                
        
                
 