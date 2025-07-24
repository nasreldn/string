# import datetime
# # print(dir(datetime))
# # print(dir(datetime.datetime))
# print(datetime.datetime.new().year)
from datetime import datetime

print(datetime.now())
print(datetime.now().year)
print(datetime.now().month)
print(datetime.now().hour)
print(datetime.now().minute)
print(datetime.min)
print(datetime.max)
# print(dir(datetime.now()))
print(datetime.now().time())
print(datetime.now().time().hour)
print(datetime.now().time().minute)
print(datetime.now().time().second)

a = datetime(2000,10,24,1,1,1)
print(a)
b= datetime.now()
print(b)
print((b-a).days)