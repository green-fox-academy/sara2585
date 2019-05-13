class Station():
    def __init__(self, gas_amount):
        self.gas_amount = gas_amount

    def refill(self,Car):

        self.gas_amount -= Car.capacity
        Car.gas_amount = Car.capacity
        return self.gas_amount, Car.gas_amount


class Car():
    def __init__(self, gas_amount=0 , capacity=100):
        self.gas_amount = gas_amount
        self.capacity = capacity

station = Station(3000)
car = Car()
print(station.refill(car))

