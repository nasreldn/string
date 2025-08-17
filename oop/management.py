a = 2
p = """ """
while a < 3:
    print("welcome to user management system\n")
    print("choose an action:\n")
    print("1.add new user\n2.display all users\n3.exit\n")
    choice = int(input("enter your choice: "))
    
    if choice == 1:
        b = input("enter your first name: ")
        c = input("enter your last name: ")
        d = input("enter your email: ")
        e = input("enter your password: ")


        if b == "" or c == "" or d == "" or e == "":
            print("all fields are required")
        else:
            user = f"""
first_name: {b},
last_name: {c},
email: {d},
password: {e},
status: "inactive"
"""
            p +=user
            p= p.strip()
            print("successfully added user")
    elif choice == 2:
        print(f"{p}")
        print("----------------------\n")  
    elif choice == 3:
        break
    else:
        print("invalid choice")   
