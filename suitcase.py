# Items in a suitcase in a cargo hold
class Item:

    def __init__(self, name: str, weight: int):
        self._name = name
        self._weight = weight

    def __str__(self):
        return f"{self._name} ({self._weight} kg)"
    
    def name(self):
        return self._name

    def weight(self):
        return self._weight

class Suitcase:

    def __init__(self, max_weight: int):
        self._max_weight = max_weight
        self._suitcase = []
        self._suitcase_weight = 0

    def add_item(self, item: Item):

        if self._suitcase_weight + item.weight() <= self._max_weight:
            self._suitcase.append(item)
            self._suitcase_weight = self._suitcase_weight + item.weight()    

    def __str__(self):
        items = len(self._suitcase)

        if items == 1:
            return f"{items} item ({self._suitcase_weight} kg)"
        else:
            return f"{items} items ({self._suitcase_weight} kg)"
        
    def print_items(self):
        for i in range(0, len(self._suitcase)):
            item = self._suitcase[i]

            print(f"{item.name()} ({item.weight()} kg)" )
    
    def weight(self):
        return self._suitcase_weight
    
    def heaviest_item(self):
        heaviest = self._suitcase[0]

        if len(self._suitcase) == 0:
            return None

        for i in range(0, len(self._suitcase)):
            item = self._suitcase[i]

            if item.weight() >= heaviest.weight():
                heaviest = item
            
            i += 1
        return heaviest

    def items(self):
        return self._suitcase

class CargoHold:

    def __init__(self, max_weight: int):
        self._max_weight = max_weight
        self._cargo = []
        self._cargo_weight = 0

    def add_suitcase(self, suitcase: Suitcase):
        if self._cargo_weight + suitcase.weight() <= self._max_weight:
            self._cargo.append(suitcase)
            self._cargo_weight = self._cargo_weight + suitcase.weight()
    
    def __str__(self):
        suitcases = len(self._cargo)
        remaining = self._max_weight - self._cargo_weight
        if suitcases == 1:
            return f"{suitcases} suitcase, space for {remaining} kg"
        else:
            return f"{suitcases} suitcases, space for {remaining} kg"

    def print_items(self):
        for suitcase in self._cargo:
            for item in suitcase.items():
                print(item)



if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()
