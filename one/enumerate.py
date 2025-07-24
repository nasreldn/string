a = ["namr","ali","ahmed","omer"]
# b = enumerate(a,1)
for c,d in enumerate(a,1):
    print(f"{c}-{d}")
for e in reversed(a):
    print(e)    

import random
# print(dir(random))  #تعرف بيها كل الفينكشنات داخل الملف
from random import randint  #استدعاء فينكشن من الملف
print(randint(1,9)) 
import sys
sys.sayhello("nasr")#دي فونكشن تجيب لبك رقم عشوائي
import bess as ee
print()
ee.sayhello("nasr")
from bess import sayhow
sayhow("nasr")    
# pypi.org #تبحث عن جميع البكجس 
# docs.python.org/3/py-modindex.html#يظر لك كل المويل العندي ومعلومات عنها
# pip list
# pip install NameError
# pip instal name --upgrade
# ctrl + p >reload
# name --version   
import numpy
print(dir(numpy))
import pyfiglet 
print(pyfiglet.figlet_format("N A S R"))
import termcolor
print(termcolor.colored(pyfiglet.figlet_format("N A S R"),color="red"))

