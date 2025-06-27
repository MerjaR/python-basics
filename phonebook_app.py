
# Modified simple phonebook to use Person class
class Person:
    def __init__(self, name: str):
        self.__name = name
        self.__numbers = []
        self.__address = None

    def name(self):
        return self.__name
    
    def numbers(self):
        return self.__numbers
    
    def add_number(self, number):
        self.__numbers.append(number)
    
    def add_address(self, address):
        self.__address = address

    def address(self):
        return self.__address

    def __str__(self):
        address = self.__address if self.__address else "address unknown"
        numbers = ", ".join(self.__numbers) if self.__numbers else "phone number unknown"
        return f"{self.__name}\n {address}\n {numbers}"


class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            person = Person(name)
            self.__persons[name] = person
        self.__persons[name].add_number(number)

    def get_entry(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name]

    def all_entries(self):
        return self.__persons

    def add_address(self, name: str, address: str):
        if name not in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_address(address)

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)

    def search(self):
        name = input("name: ")
        person = self.__phonebook.get_entry(name)
       
        if person == None:
            print("address unknown")
            print("number unknown") 
            return 

        numbers = person.numbers()
        if not numbers:
            print("number unknown")
        else:
            for number in numbers:
                print(number) 

        address = person.address()
        if address is None:
            print("address unknown")
        else:
            print(address)  

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()



application = PhoneBookApplication()
application.execute()

# if __name__ == "__main__":
#     phonebook = PhoneBook()
#     phonebook.add_number("Eric", "02-123456")
#     print(phonebook.get_entry("Eric"))
#     print(phonebook.get_entry("Emily"))
