class ArmoredBattleship:
    def __init__(self, fuel, maxprojectilespeed):
        self.fuel = fuel
        self.maxprojectilespeed = maxprojectilespeed
    def refuel(self, amount):
        self.fuel += amount
    def swim(self):
        if self.fuel > 0:
            print('Swimming')
            self.fuel -= 1
        else:
            print("No fuel")
htypearmoredboat = ArmoredBattleship (20, 220)
print(htypearmoredboat.fuel)
print(htypearmoredboat.maxprojectilespeed)
sentinelarmoredboats = ArmoredBattleship(55, 570)
print(sentinelarmoredboats.fuel)
print(sentinelarmoredboats.maxprojectilespeed)
print('-------------------')
print(htypearmoredboat.fuel)
htypearmoredboat.refuel(10)
print(htypearmoredboat.fuel)
print('-------------------')
print(sentinelarmoredboats.fuel)
sentinelarmoredboats.swim()
print(sentinelarmoredboats.fuel)
