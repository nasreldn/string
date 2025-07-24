from functools import reduce
def a(num1,num2):
    return num1 +num2
b=[1,2,3,4,5,6,7]
c =reduce(a,b)
print(c)
print("#"*20)
d = [100,56,87,33]
e= reduce(lambda num1, num2:num1+num2,d)
print(e)