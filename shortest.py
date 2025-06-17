# Find the shortest person in the room. 
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return f"{self.name} ({self.height} cm)"

class Room:
    def __init__(self):
        self.persons = []

    def add(self, person: Person):
        self.persons.append(person)
    
    def is_empty(self):
        if len(self.persons) == 0:
            return True
        else:
            return False
    
    def print_contents(self):
        for i in range(0, len(self.persons)):
            printout = self.persons[i]
            print(printout)

    def shortest(self):
        if not self.persons:
            return None
        
        shortest_person = self.persons[0]
        for person in self.persons[1:]:
            if person.height < shortest_person.height:
                shortest_person = person
        return shortest_person

    def remove_shortest(self):
        if not self.persons:
            return None
        
        shortest_person = self.shortest()
        self.persons.remove(shortest_person)
        return shortest_person
        
