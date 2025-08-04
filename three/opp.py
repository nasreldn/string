class name:
    names= ["fefe","zezo","nano"]
    number_user =0
    def __init__(name,fname,mname,lname,gender):
        name.frname=fname
        name.mdrname=mname
        name.lsname=lname
        name.ngender=gender
        name.number_user +=1
    def fullname(name):
        if name.frname in name.names:
            raise ValueError("your name is none")
        else:
            return f"{name.frname} {name.mdrname} {name.lsname}"
    def hello(name):
        if name.ngender=="male":
             return f"hello mr {name.frname}"
        elif name.ngender=="female":
            return f"hello miss {name.frname}"
        else:
             return f"hello {name.frname}"  
    def all(name):
        return f"{name.fullname()}, {name.hello()}" 
    def delete(name):
        name.number_user -=1
        return f"user {name.fname}is delete"
print(name.number_user)           
a= name("nasr","altayeb","abdalla","male", )
b= name("ali","ebrahim","alkhider","male",)
c= name("fairs","aljaile","aljined","female")
print(name.number_user) 
# print(dir(name))
# print(dir(str))
# print(a.__class__)
# print(a.frname,a.mdrname,a.lsname)
# print(b.frname,a.mdrname,a.lsname)
# print(c.frname,a.mdrname,a.lsname) 
# print(name.number_user)        
# print(a.all())
# print(b.all())
# print(c.all())
# print(name.number_user)    

