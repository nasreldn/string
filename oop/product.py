class product: 
    def __init__(self,name,price): 
        self.name=name
        self.price=price

product_one=product("Laptop",1000)
product_two=product("Phone",500)
print(f"name: {product_one.name}, price:{product_one.price}")
print(f"name: {product_two.name}, price:{product_two.price}")
