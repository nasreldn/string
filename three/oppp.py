 
class humen:
    def __init__(self,name,age,contary):
        self.esm=name
        self.omar=age
        self.bald=contary
    def getomar(self):
        return self.omar
    def setomar(self,value):
        if 0<value<100:
            value=self.omar
            print("hello")
        else:
            print("hhhh")       
a=humen("nasr",20,"sudan") 
a.setomar(200)