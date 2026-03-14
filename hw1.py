class Car:
    def move(self):
        print("Car is moving")
class Bike:
    def move(self):
        print("Bike is riding")
class Bus:
    def move(self):
        print("Bus is transporting passengers")

vehicles = [Car(),Bike(),Bus()]
for v in vehicles:
    v.move()