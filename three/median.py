a= [1,2,3,4,5,6,7,8]
a.sort()
if len(a)%2==0:
    b=a[len(a)//2]
    c=a[len(a)//2-1]
    d=(b+c)/2
else:
    d=a[len(a)//2]
print(d)       