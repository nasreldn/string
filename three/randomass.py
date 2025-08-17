import random
a = random.randrange(1,10)
c = 3


while c > 0:

    b = int(input("khamin: "))


    if b>a:
        print("up")
        b = int(input("khamin: "))
      
    elif b<a:
        print("dawn")
        b = int(input("khamin: "))
        
    elif a ==b:
        print("you won")
        break

    
             
              
            