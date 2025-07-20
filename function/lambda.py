def a(name) :
    return f"hello {name}"
naser = lambda a,b: f"hello {a} you can {b}"
print(a("nasr"))
c=(naser("gedo","bogba"))
print(c)
print(a.__name__)
print(naser.__name__)
print(type(a))
print(type(naser))