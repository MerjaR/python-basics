# Finding all books in the list that share the given genre

class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre 
        self.year = year

    ##STUB:# This enables easy printing of a Book object
    def __repr__(self):
        return f"{self.name} ({self.author}), {self.year} - genre: {self.genre}"


# -----------------------------
# Write your solution here
# -----------------------------

def books_of_genre(books: list, genre: str):
    new_list = []
    for i in range(0, len(books)):
        if books[i].genre == genre:
            new_list.append(books[i])
    return new_list
    



if __name__ == "__main__":
    python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
    everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
    norma = Book("Norma", "Sofi Oksanen", "crime", 2015)

    books = [python, everest, norma, Book("The Snowman", "Jo Nesbø", "crime", 2007)]

    print("Books in the crime genre:")
    for book in books_of_genre(books, "crime"):
        print(f"{book.author}: {book.name}")
