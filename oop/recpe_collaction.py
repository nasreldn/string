class RecipeCollection:
    def __init__(self,name, ingredients, instructions, cooking_time):
        self.name=name
        self.ingredients=ingredients
        self.instructions=instructions
        self.cooking_time=cooking_time
    def display(self):
        print(f"recipe name: {self.name}")
        print(f"ingredients: {self.ingredients}")
        print(f"instructions: {self.instructions}")
        print(f"cooking time: {self.cooking_time}")
def run():
    print("recipe added successfully\n\n")
    name=input("enter recipe name: ")
    ingredients=input("enter ingredients: ")
    instructions=input("enter recipe instructions: ")
    cooking_time=input("enter cooking time: ")
    print("*"*20)

    return RecipeCollection(name, ingredients, instructions, cooking_time)
taga = run()

taga.display()

