class ATM:
    def __init__(self,):
        self.balance = 0
        
    def deposite(self,amount):
        self.balance += amount
        print("Ammount deposited successfully")
        print("deposited amount:",self.balance)
    
    def withral(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withral successfully")
            print("Withral amount:",amount)
            print("Current balance:",self.balance)
        else:
            print("Insufficient balance:",self.balance)

    def balance_check(self):
        print("Your Total Balance:",self.balance)
    

# user1 = ATM()
# user.deposite(1000)
# user.withral(1000)
# user.balance_check()

user2 = ATM()
user2.deposite(2000)
user2.withral(500)
user2.balance_check()

