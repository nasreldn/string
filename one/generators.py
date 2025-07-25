def a():
    yield 1
    yield 2
    yield 3
for b in a():
    print(b)
b = a()
print(next(b))
print("hello") 
print(next(b)) 
print("hello") 
print(next(b))  