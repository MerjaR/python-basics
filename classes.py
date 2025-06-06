#Defining classes for the first time
class Book:
    def __init__(self, name, author, genre: str, year: int):
        self.author = author
        self.name = name
        self.year = year
        self.genre = genre

if __name__ == "__main__":
    python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
    everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)

    print(f"{python.author}: {python.name} ({python.year})")
    print(f"The genre of the book {everest.name} is {everest.genre}")
