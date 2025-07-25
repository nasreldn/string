def a(bnana):
    def b(n1,n2):
        print("#" * 20)
        bnana(n1,n2)
        print("#" * 20)
    return b   
@a        
def c(n1,n2):
    print(n1+n2)
# d =a(c) 
# d()
c(2,9)
    
 
         