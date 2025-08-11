import random
play1= input("select : paper,hajar,mgas: ").lower()
play2=random.choice(["hajar","magas","paper"])
print(f"caputer= {play2}")

if play1=="paper" and play2=="hajar":
    print("you won ")
elif play1=="paper" and play2=="magas": 
    print("you loss")   
elif play1=="hajar" and play2=="paper":
    print("you loss")    
elif play1=="hajar" and play2=="magas":
    print("you won")   
elif play1=="magas" and play2=="paper":
    print("you won")     
elif play1=="magas" and play2=="hajar":
    print("you loss")
else:
    print("you ==computer")