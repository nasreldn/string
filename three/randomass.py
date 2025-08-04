import random
a = random.randrange(1,10)
c = 3


while c > 0:
    print(f" you have {c}")
    b = int(input("khamin: "))


    if b>a:
        print("up")
        b = int(input("khamin: "))
        c -=1
    elif b<a:
        print("dawn")
        b = int(input("khamin: "))
        c -=1
    elif a ==b:
        print("you won")
        break

    
             
              
            