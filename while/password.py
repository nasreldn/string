password = "nasr123"
a = 4
b = input("enter your password: ")
while password != b:

    print(f"you have {"last" if a ==0 else a -1} try")
    a -=1

    b = input("enter your password: ") 
    if a==0:
        break

if b == password:
    print("welcome ")    