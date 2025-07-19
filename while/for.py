a = [1,2,3,4,5,6,7,8,9]
for number in a :
    # print(f"[ {number}  ]") 
    if number % 2 ==0:
        print(f"{number}even")
    else:
        print(f"{number}odd")    
a =range(1,100)
for b in a:
    print(b)
a = {
    "html": "93%", 
    "sql": "85%", 
    "python": "50%"
    }
for b in a:
    print(f"{b}:{a[b]}")
a = {
    "nasr":{
    "age":"30",
    "jop":"developer",
   },
     "ali":{
         "age":"25",
         "job":"doctor"
     }
}
for b in a:
    print(b)
    for c in a[b]:
        print(f"{c}=>{a[b][c]}")

a = {"html":{
    "nasr":"93%",
    "ali":"85%"
},
     "css":{
         "nasr":"90%",
         "ali":"80%"
     }
     } 
for b,c in  a.items():
    print(f"{b}") 
    for e,f in c.items():
        print(f"{e}==>{f}") 
print(a.items())             