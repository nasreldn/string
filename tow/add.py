a = ["nasr","ahmed","ali","omer"]
name =input("what\' is you name? ").strip()
if name in a:
    print(f"hello {name}")
    b = input("delete or update? ").strip()
    if b == "delete":
        a.remove(name)
        print("your name has been deleted")
        print(a)
    elif b == "update":
        c = input("write your new ").strip()
        d = a.index(name)
        a[d]=c
        print(a)
else:
    print(f"your name is not in the list")
    e = input("if you add in the list or not? ").strip() 
    if e == "add":
        a.append(name)
        print(a)
    else:
        print("ok,  bye")         