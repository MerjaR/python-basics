# Using two classes.

class Pet:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description


    def __str__(self):
        return f"{self.name}, a {self.description}"

class Person:
    def __init__(self, name: str, pet: Pet):
        self.name = name
        self.pet = pet

    def __str__(self):
        
        return f"{self.name}, whose pal is {self.pet}"

