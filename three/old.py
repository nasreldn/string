def a(y,m,d):
    import datetime
    new= datetime.datetime.now().date()
    meold=datetime.date(y,m,d)
    myoldnow=int((new-meold).days/365.25)
    print(myoldnow)
    print(new)
    print(meold)
a(2000,10,24)    