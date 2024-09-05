class Account:
    def __init__(self,name,balance,min_balance):
        self.name=name
        self.balance=balance
        self.min_balance=min_balance

    def deposit(self,amount):
        self.balance +=amount

    def withdraw(self,amount):
        if self.balance-amount >= self.min_balance:
            self.balance -=amount
        else:
            print("Sorry, Insufficient Funds")
    def printStatement(self):
        print("Account Balance:",self.balance)
class Current(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance=-1000)
    def __str__(self):
        return f"{self.name}'s Current Account with Balance :{self.balance}"
class Savings(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance=0)
    def __str__(self):
        return f"{self.name}'s Savings Account with Balance :{self.balance}"

c=Savings("Sonam",10000)
print(c)
c.deposit(5000)
c.printStatement()
c.withdraw(16000) 
c.withdraw(15000)
print(c)

c2=Current('Muskan',20000)
c2.deposit(6000)
print(c2)
c2.withdraw(27000)
print(c2)
        

