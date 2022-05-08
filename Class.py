class Car:
    def __init__(self, fuel, maxspeed):
        self.fuel = fuel
        self.maxspeed = maxspeed
    def refuel(self, amount):
        self.fuel += amount
    def drive(self):
        if self.fuel > 0:
            print('Driving')
            self.fuel -= 1
        else:
            print("No fuel")
polo = Car(10, 140)
print(polo.fuel)
print(polo.maxspeed)
ferrari = Car(15, 290)
print(ferrari.fuel)
print(ferrari.maxspeed)
print('-------------------')
print(polo.fuel)
polo.refuel(10)
print(polo.fuel)
print('-------------------')
print(ferrari.fuel)
ferrari.drive()
print(ferrari.fuel)
