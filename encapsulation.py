class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
    
    def deposit(amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance
    
a1 = BankAccount('Aliya',2500000)
print(a1.get_balance())

    
