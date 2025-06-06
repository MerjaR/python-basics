#Defining classes for the first time
class Book:
    def __init__(self, name, author, genre: str, year: int):
        self.author = author
        self.name = name
        self.year = year
        self.genre = genre
        
class Checklist:
    def __init__(self, header: str, entries: list):
        self.header = header
        self.entries = entries
    
class Customer:
    def __init__(self, id: str, balance: float, discount: int):
        self.id = id
        self.balance = balance
        self.discount = discount

class Cable:
    def __init__(self, model: str, length: float, max_speed: int, bidirectional: bool):
        self.model = model
        self.length = length
        self.max_speed = max_speed
        self.bidirectional = bidirectional


if __name__ == "__main__":
    python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
    everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)

    print(f"{python.author}: {python.name} ({python.year})")
    print(f"The genre of the book {everest.name} is {everest.genre}")

