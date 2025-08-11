def a(b):
    # b=set(b) 
    d=len(b)  
    e=[]
    for f in range(1,b[-1]):
        if f not in b:
            e.append(f)
    return e        
k=[1,2,3,5,6,8,9] 
print(a(k))       
a=[1,2,3,4,14,6,7,9]  
a.sort() 
print(a[-1])

                  
    