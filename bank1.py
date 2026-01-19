class account:
    def __init__(self, accountHolderName, balance):
        self.accountHolderName = accountHolderName
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

a1 = account("Rahul", 5000)
a1.deposit(1500)
print(a1.balance)
print(a1.accountHolderName)