class name:
    def __init__(name,fname,mname,lname,gender):
        name.frname=fname
        name.mdrname=mname
        name.lsname=lname
        name.ngender=gender
    def fullname(name):
        return f"{name.frname} {name.mdrname} {name.lsname}"
    def hello(name):
        if name.ngender=="male":
             return f"hello mr {name.frname}"
        elif name.ngender=="female":
            return f"hello miss {name.frname}"
        else:
             return f"hello {name.frname}"  
    def all(name):
        return f"{name.fullname()} {name.hello()}"      
a= name("nasr","altayeb","abdalla","male")
b= name("ali","ebrahim","alkhider","male")
c= name("ashraf","aljaile","aljined","female")
 
# print(dir(name))
# print(dir(str))
# print(a.__class__)
# print(a.frname,a.mdrname,a.lsname)
# print(b.frname,a.mdrname,a.lsname)
# print(c.frname,a.mdrname,a.lsname)         
print(a.all())
print(b.all())
print(c.all())

