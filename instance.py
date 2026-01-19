class Car:
    showroom = "AVI Motors"
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price

car1 = Car("OpenCV", 100000)

print(car1.price,car1.showroom)

