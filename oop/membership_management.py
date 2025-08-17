from oop.profile2 import user


a=4
b="""display all members\n """
while a<5:
    for i in range(1,10):
        print("welcome to gym membership management \n\n")
        print("choose an action:\n")
        print("1. Add new member\n2. Display all members\n3. Search member\n4. Exit\n")
        choice = int(input("enter your choice: "))
        if choice ==1:
            c[i]= input("enter member's first name: ")
            d[i]= input("enter member's last name: ")
            e[i]= int(input("enter member's id : "))
            f[i]= input("enter membership status,or click inter : ")

            if c[i]=="" or d[i]=="" or e[i]=="" :
                print("all fields are required")
                if f[i]=="":
                    f[i]="inactive"
                else:
                    f[i]=f[i]

            else:
                user[i] = f"""
first_name: {c[i]},
last_name: {d[i]},
membership_id: {e[i]},
membership_status: {f[i]},
-----------------------\n

"""
            b += user_i
            b = b.strip()
            print("successfully added member")
        elif choice ==2:
            print(f"{b}")
        elif choice ==3:
            print("searching by: \n")
            print("1. first name\n2. id\n3. membership status\n")
            search_choice = int(input("enter your choice: "))
            if search_choice == 1:
                search_term = input("enter first name: ")
                if search_term==ci:
                    print(f"{user_i}")
                else:
                    print("member not found \n")    

            # search logic here
            elif search_choice == 2:
                search_term = int(input("enter id: "))
                if search_term==ei:
                    print(f"{user_i}")
                else:
                    print("member not found \n")
            elif search_choice == 3:
                search_term = input("enter membership status: ")
                if search_term==fi:
                    print(f"{user_i}")
                else:
                    print("member not found \n")
            else:
                print("invalid choice")
        elif choice == 4:
            break 
    else:
        break       