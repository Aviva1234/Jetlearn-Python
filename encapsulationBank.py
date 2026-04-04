class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if (amount <= self.__balance):
            self.__balance -= amount
        else:
            print("Insufficient balance")
    def get_balance(self):
        print(self.__balance)

a = BankAccount("Alice",100)
a.deposit(50)
a.get_balance()
a.withdraw(200)
a.withdraw(30)
a.get_balance()