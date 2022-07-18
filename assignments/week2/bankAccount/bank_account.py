class BankAccount:
    def __init__(self, name, balance,interest_rate):
        self.name = name
        self.balance = balance
        self.interest_rate = interest_rate
        
    def deposit(self, amount):
        self.balance += amount
        print(f"You have deposited, ${amount} {self.name}'s balance is now ${self.balance}")  
        return(self)
    
    def withdraw(self, amount):
        self.balance -= amount
        print(f"{self.name}'s balance is now ${self.balance}")
        return(self)
        
    
    def get_balance(self):
        print(f"{self.name}'s balance is ${self.balance}")
        return(self)
    
    
        
    def interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.interest_rate
            print(f"{self.name}'s balance is now ${self.balance}")
            return(self)
    
    #use a class method to print all instances of the class
    def everything(self):
        print(f"{self.name}'s balance is ${self.balance} your interest rate is {self.interest_rate}")




lori=BankAccount("Lori", 100, 0.05)
john=BankAccount("John", 200, 0.05) 
lori.deposit(50).get_balance().withdraw(25).get_balance().deposit(25).get_balance().withdraw(25).get_balance().interest().get_balance()
john.deposit(50).get_balance().withdraw(25).get_balance().deposit(25).get_balance().withdraw(25).get_balance().interest().get_balance()
lori.everything()