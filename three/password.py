import getpass
a={"nasr":"1234","ali":"090909","omer":"77777"}
b = input("write you username : ") 
if b in a:
    c = 3
    password=getpass.getpass("werite your password:")    
    while c>0:
        print(f"you have {c} trys")
        # password=getpass.getpass("werite your password:")
        if password == a[b]:
            print("hello")
            break
        else:
            password=getpass.getpass("werite your password agin:")
            c -=1
    else:
        print(f"you trys={c}")
        print("good luck")        
else:
    print("your name is none ")                  
# a={"nasr":"1234","ali":"090909","omer":"77777"}
# username= input("write your name :")
# for b in a:
#     if username==b:

#         while username==b:
#             c =input("write your pass word: ")
#             if c == a[b]:
#                 print("nasreldine has beautifule wife in alfaw and the days give him two children grile and boy")
#                 break
#             else:
#                 print("yuor name none ")
#                 break        