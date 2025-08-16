class task: 
    def __init__(self,title,director,please_year,ginre):
        self.title=title
        self.director=director
        self.please_year=please_year
        self.ginre=ginre
    def new_director(self,director):
        self.director=director
    def say_all(self):
        print("_____movies_____")
        print(f"title:  {self.title}")
        print(f"director:  {self.director}")
        print(f"please_year:  {self.please_year}")
        print(f"ginre:  {self.ginre}")
       
movise1=task("see","joun","2015","action") 
movise2=task("army","nasr","2015","romance")        
movise3=task("geme strong","ahmed","2010","action")
movise1.say_all()
movise2.say_all()
movise3.say_all()
movise1.new_director("ali")
movise2.new_director("faez")
movise3.new_director("peter")
movise1.say_all()
movise2.say_all()
movise3.say_all()
