try:
    print(10/0)
    print(x)
    print(int(input("yournumber")))
except ZeroDivisionError:
    print("your number no no ")
except NameError:
    print("your value is not ") 
except ValueError:
    print(" is you man ") 
except:
    print("in erorr")    
finally:
    print("hello nasr")          
        