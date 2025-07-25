def a(bnana):
    def b():
        print("#" * 20)
        bnana()
        print("#" * 20)
    return b   
@a        
def c():
    print("nasor")
# d =a(c) 
# d()
c()
    
 
         