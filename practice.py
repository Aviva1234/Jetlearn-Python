class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self, amount):
        if (amount<=self.__balance):
            self.__balance-=amount
        else:
            print("Insufficient balance")
    def showBalance(self):
        print(self.__balance)

a1 = Account("Alice",300)
a2 = Account("Olivia")
a1.withdraw(400)
a1.withdraw(70)
a1.showBalance()
a2.deposit(250)
a2.showBalance()

