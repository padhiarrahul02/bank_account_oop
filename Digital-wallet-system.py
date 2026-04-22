class Wallet:
    def __init__(self,owner):
        self.owner = owner
        self.__balance = 0
    def add_balance(self,amount):
        self.__balance += amount
    
    def spend_balance(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Ensufficient Balance..")
    def balance_check(self):
        return self.__balance

c= Wallet("Himanshu")
c.add_balance(1000)
c.spend_balance(500)
print(c.balance_check())
d = Wallet("Hari")
d.add_balance(5000)
d.spend_balance(6000)
print(d.balance_check())

f = Wallet("Mahesh")
f.add_balance(10000)
f.add_balance(5000)
f.add_balance(5000)
print(f.balance_check())
f.spend_balance(5000)
f.spend_balance(5000)
print(f.balance_check())
f.spend_balance(20000)
print(f.balance_check())

r= Wallet("Rajesh")
r.add_balance(500)
r.spend_balance(600)

        