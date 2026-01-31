class Mobile:
    company = "TechOne"

    def __init__(self, model, price):
        self.model = model
        self.price = price
    
    def display():
        print(f"Model {self.model} costs ${self.price}")
    
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company
    
m1 = Mobile("Samsung", 1200)
m2 = Mobile("Apple", 1100)


