class pet:
    def __init__(self, name:str, age:int):
        self.name=name
        self.age=age
        assert age>=0, f"age {self.age} is invalid"
class rat(pet):
    def __init__(self, name: str, age: int, colour:str):
        super().__init__(name, age)
        self.colour = colour
pet1=pet('tom', 4)
print(pet1.name)  
pet2=rat('jerry', 2, 'black')
print(pet2.age, pet2.colour)      
print(f"Is jerry a pet?", isinstance(pet2, pet))
print(f"Is tom a rat?", isinstance(pet1, rat))           