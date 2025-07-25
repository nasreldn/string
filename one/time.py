from time import time 
def a(b):
    def c():
        d = time()
        b()
        e= time()
        print(f"time do is {e-d}")
    return c
@a
def f():
    for g in range(1,2000):
        print(g)
f()        
    