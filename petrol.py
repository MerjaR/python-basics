# Encapsulated attributes
class Car:
    def __init__(self):
        self.__petrol = 0
        self.__odometer = 0

    def __str__(self):
        reading = self.__odometer
        remaining = self.__petrol
        return f"Car: odometer reading {reading} km, petrol remaining {remaining} litres"
    
    def fill_up(self):
        self.__petrol = 60
    
    def drive(self, km: int):
        if self.__petrol - km >= 0:
            self.__odometer = self.__odometer + km
            self.__petrol = self.__petrol - km
        else:
            self.__odometer = self.__odometer + self.__petrol
            self.__petrol = 0
    
if __name__ == "__main__":
    car = Car()
    print(car)
    car.fill_up()
    print(car)
    car.drive(20)
    print(car)
    car.drive(50)
    print(car)
    car.drive(10)
    print(car)
    car.fill_up()
    car.fill_up()
    print(car)
        

    


