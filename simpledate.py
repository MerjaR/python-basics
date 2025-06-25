# Simple date calculations
class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"
    
    def __eq__(self, another):
        if self.year == another.year and self.month == another.month and self.day == another.day:
            return True
        else:
            return False
    
    def __ne__(self, another):
        if self.year != another.year or self.month != another.month or self.day != another.day:
            return True
        else:
            return False

    def __lt__(self, another):
        if self.year < another.year:
            return True
        elif self.year == another.year and self.month < another.month:
            return True
        elif self. year == another.year and self.month == another.month and self.day < another.day:
            return True
        else:
            return False

    def __gt__(self, another):
        if self.year > another.year:
            return True
        elif self.year == another.year and self.month > another.month:
            return True
        elif self. year == another.year and self.month == another.month and self.day > another.day:
            return True
        else:
            return False
    
    def __add__(self, number: int):
        total_days = self.day + number
        new_day = total_days % 30
        total_months = self.month + (total_days // 30)
        new_month = total_months % 12
        new_year = self.year + (total_months // 12)

        if new_day == 0:
            new_day = 30
            new_month -= 1
            if new_month == 0:
                new_month = 12
                new_year -= 1
        
        return SimpleDate(new_day, new_month, new_year)
    
    def __sub__(self, another):
        days1 = (self.year * 12 * 30) + (self.month *30) + self.day
        days2 = (another.year * 12 * 30) + (another.month *30) + another.day

        result = days1 - days2
        if result < 0:
            result = result * -1

        return result


    

if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)
