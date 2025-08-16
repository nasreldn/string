class profile:  
    def __init__(self,name,age,language): 
        self.name=name
        self.age=age
        self.language=language
user_one=profile("nasr",24,"python")
user_two=profile("ahmed",30,"java")
print(f"name: {user_one.name}, age:{user_one.age},language:{user_one.language}")
print(f"name: {user_two.name}, age:{user_two.age},language:{user_two.language}")
