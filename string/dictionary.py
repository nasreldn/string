a = {"name":"nasr",
     "age":25,
     }
a["contary"]="sudan"
print(a)
a.update({"nnn":"nidhidr"})
print(a)
b=a.copy()
print(b)
a.update({"ihiehe":"3333"})
print(a.keys())
print(a.values())
# print(a.clear())

print(a.setdefault("ioo","bebo"))
print(a.popitem())
c =  a.items()
print(c)
z =("ejdeji","jeieidjjk","j4jd")
q =("12")
print(dict.fromkeys(z,q))