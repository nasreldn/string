import os
print(os.path.abspath("for.txt")) 
myfile = None
mytry= 5
while mytry > 0:
    try:
        print("write your path file")
        print("example home/ nasr/nieded.txt")
        print(f"yuo have {mytry}")
        mynewfile= input("write....  ").strip()
        myfile= open(mynewfile,"r")
        # myfile=(mynewfile,"r")
        print(myfile.read())
        break
    except FileNotFoundError:

             print("malgito")
             mytry -=1
    except:
        print("erorr")
    finally:
        if myfile is not None:
            myfile.close()             
else:
    print("you have zero tries  ")
   
    
