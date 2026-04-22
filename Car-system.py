class Car:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed
        self.__fuel = 50  #private vaiable(encapsulation)


    def drive(self):
        if self.__fuel > 0:
            self.__fuel -= 10
            print(f"{self.brand} is driving at {self.speed} km/h")
        else:
            print("No Fuel...")
    def add_fuel(self,amount):
        self.__fuel += amount
        print(f"{amount} fuel added...")
    def check_fuel(self):
        return self.__fuel

#Inheritance
class Electric_car(Car):
    def __init__(self,brand,speed,battery):
        super().__init__(brand, speed)
        self.__battery = battery
    #Polymorphism(methods over-riding)
    def drive(self):
        if self.__battery > 0:
            self.__battery -= 10
            print(f"{self.brand} (Electric is driving silently...)")
        else:
            print("Battery Empty !")
    def charge(self):
        self.__battery += 20
        print("Battery changed...")
    def check_battery(self):
        return self.__battery
    
c = Car("BMW",200)
c.drive()
c.add_fuel(50)

print(c.check_fuel())

print("------------")

e = Electric_car("TATA",120,50)
e.drive()
e.charge()
print("Battery:",e.check_battery())