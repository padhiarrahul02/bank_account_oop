class BankAccount():
    def __init__(self,balance=0):
        self.balance = balance

    def deposite(self,amount):
        self.balance += amount
        print("Deposited amount:",amount)
        print("Current balance:",amount)

    def withral(self,amount):
        if amount > self.balance:
            print("Insufficient balance..")

        else:
            self.balance -= amount
            print("withrawn amount:",amount)
            print("Available balance:",self.balance)




d = BankAccount()

d.deposite(100)
d.withral(50)