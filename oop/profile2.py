class user: 
    def __init__(self,firstname,last_name,email,password,status="inactive"):
        self.firstname=firstname
        self.last_name=last_name
        self.email=email
        self.password=password
        self.status=status
    def input_you(self):
        a=input("enter your first name:")
        b=input("enter your last name:")
        c=input("enter your email:")
        d=input("enter your password:")
        e=input("enter your status:")

        return user(a,b,c,d,e)


user1=user("","","","","")
user1=user1.input_you()
print(f"{user1.firstname} {user1.last_name} {user1.email} {user1.password} {user1.status}")