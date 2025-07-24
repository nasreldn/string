def a(nubmer) :
    return nubmer > 5
b = [1,2,3,4,5,6,7,8,9,10]
c = filter(a,b)
for d in c :
    print(d)
print("#"*30) 
e = ["a","b","c","d","bkld","bknqn"] 
for f in filter(lambda taxt :taxt.startswith("b"),e):
    print(f)  