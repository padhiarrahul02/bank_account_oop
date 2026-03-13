class BankAccount():
    def __init__(self,balance=0):
        self.balance = balance

    def deposite(self,amount):
        self.balance += amount
        print("Deposit Successful")
        print("Deposited amount:",amount)
        print("Current balance:",amount)

    def withral(self,amount):
        if amount > self.balance:
            print("Insufficient balance..")

        else:
            self.balance -= amount
            print("Withral Sucessful")
            print("withrawn amount:",amount)
            print("Available balance:",self.balance)




d = BankAccount()

d.deposite(2000)
d.withral(1000)