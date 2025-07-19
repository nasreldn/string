def sayhello(name):
   if type(name)!= str:
        print("your name must be string")
    else:
            
        print(f"hello {name.strip().upper()}")
a,b,c="nasr","ali","omer"        
sayhello(a)
sayhello(b)
sayhello(c)
def a(n1,n2):
    if type(n1)!=int or type(n2)!=int: 
        print("your number must be int")
    else:
        print(n1+n2) 
    
    
b =(input("enter your first number: "))

c =(input("enter your scond number: "))
a(int(b),int(c)) 
def b(name,*maharat):
    print(f"hello {name} goood")
    for a in maharat:
        print(a)
b("nasr","html","css","c","python")
b("ali","js","css","php","sql")
         
def h(name,age,contary="unknown"):
    print(f"hello {name} your age is {age} and your contary is {contary}")
h("ali",5686) 
h("nasr","25","sudan")
def g()  
           