# Classes and operators
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        if self.__cents > 9:
            return f"{self.__euros}.{self.__cents} eur"
        elif self.__cents < 10:
            return f"{self.__euros}.0{self.__cents} eur"
    
    def __eq__(self, another):
        if self.__euros == another._Money__euros and self.__cents == another._Money__cents:
            return True
        else:
            return False
    
    def __lt__(self, another):
        if self.__euros < another._Money__euros:
            return True
        elif another._Money__euros == self.__euros and self.__cents < another._Money__cents:
            return True
        else:
            return False

    def __gt__(self, another):
        if self.__euros > another._Money__euros:
            return True
        elif another._Money__euros == self.__euros and self.__cents > another._Money__cents:
            return True
        else:
            return False


    def __ne__(self, another):
        if self.__euros != another._Money__euros:
            return True
        elif self.__euros == another._Money__euros and self.__cents != another._Money__cents:
            return True
        else:
            return False
    
    def __add__(self, another):
        euros = self.__euros + another._Money__euros
        cents = self.__cents + another._Money__cents

        if cents >=100:
            cents = cents - 100
            euros = euros + 1
        
        result = Money(euros, cents)
        return result
    
    def __sub__(self, another):
        euros = self.__euros - another._Money__euros
        
        if euros < 0:
            raise ValueError(f"a negative result is not allowed")
        
        if self.__cents < another._Money__cents:
            if euros >= 1:
                euros = euros - 1
                cents = 100 - another._Money__cents + self.__cents
            else: 
                raise ValueError(f"a negative result is not allowed")
        else:
            cents = self.__cents - another._Money__cents

        result = Money(euros, cents)

        return result
    
        

if __name__ == "__main__":
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2-e1

