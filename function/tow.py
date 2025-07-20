# def a(name,*ttt,**diccc):
#     print(f"{name}")
#     for b in ttt:
#         print(f"{b}") 
#     for c,d in diccc.items(): 
#         print(f"{c}==>{d}") 
# e =("mdjeeodj","oooojd33k","pqkdekmem")
# f ={"nasr":"data analyst","amro":"develober",}  
# a("nasr",*e,**f) 


def clean(stringg):
   if len(stringg)<=1:
       return stringg
   if stringg[0]==stringg[1]:
       return clean(stringg[1:])
   return stringg[0]+clean(stringg[1:])
print(clean("nnnssssikkk"))          
# def a(name):
#     print(name[1:]) 
# a("nasr")