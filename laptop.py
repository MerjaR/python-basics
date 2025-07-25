# Using a base class and derived class
class Computer:
    def __init__(self, model: str, speed: int):
        self.__model = model
        self.__speed = speed

    @property
    def model(self):
        return self.__model

    @property
    def speed(self):
        return self.__speed

class LaptopComputer(Computer):
    def __init__(self, model: str, speed: int, weight:int):
        self.__weight = weight
        super().__init__(model, speed)
    
    def __str__(self):
        return f"{self.model}, {self.speed} MHz, {self.__weight} kg"

if __name__ == "__main__":
    laptop = LaptopComputer("NoteBook Pro15", 1500, 2)
    print(laptop)
