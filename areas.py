# Square as a special case of rectangle
class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def __str__(self):
        return f"rectangle {self.width}x{self.height}"

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side: int):
        super().__init__(side, side)

    def __str__(self):
        return f"square {self.width}x{self.height}"

if __name__ == "__main__":
    square = Square(4)
    print(square)
    print("area:", square.area())
    
