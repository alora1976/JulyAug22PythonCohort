class BankAccount:
    def __init__(self, name, balance,interest_rate):
        self.name = name
        self.balance = balance
        self.interest_rate = interest_rate
        self.account={
            "checking": BankAccount("checking",0,0.01),
            "savings": BankAccount("savings",0,0.05)
        }
    
        
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
    
    def everything(self):
        print(f"{self.name}'s balance is ${self.balance} your interest rate is {self.interest_rate}")
        return(self)
    
    def transfer_money(self,amount,other_user):
        self.balance -= amount
        self.account["checking"].withdraw(amount)
        other_user.account["checking"].deposit(amount)
        print(self.name + " has transferred " + str(amount) + " to " + other_user.name + "'s checking account.")
        print("-----------------------------------------------------")
        return(self)



class User :
    
    def __init__(self, first_name,last_name, email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        
    def display_user_info(self):
        print("Name: " + self.first_name + " " + self.last_name)
        print("Email: " + self.email)
        print("Age: " + str(self.age))
        print("Rewards Member: " + str(self.is_rewards_member))
        print("Gold Card Points: " + str(self.gold_card_points))
        print("-----------------------------------------------------")
    
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points += 200
        print(self.first_name + " is enrolled in rewards."+"\n"+"Gold Card Points: " + str(self.gold_card_points))
        print("-----------------------------------------------------")

    def test_enroll(self):
        if self.is_rewards_member == False:
            print(self.first_name + " is not enrolled in rewards.")
            self.enroll()
        if self.is_rewards_member == True:
            print(self.first_name + " is now enrolled in rewards."+"\n"+"Gold Card Points: " + str(self.gold_card_points))   
            print("-----------------------------------------------------")
            
        
        
    
    def spend_points(self,amount):
        self.gold_card_points -= amount
        print(self.first_name + " has spent " + str(amount) + " points.")
        if self.gold_card_points < 0:
            print(self.first_name + " has insufficient points.")
            self.gold_card_points = 0
            print("-----------------------------------------------------")
        

    def earn_points(self,amount):
        self.gold_card_points += amount
        print(self.first_name + " has earned " + str(amount) + " points.")
        if self.gold_card_points > 10000:
            print(self.first_name + " has exceeded the maximum points.")
            self.gold_card_points = 10000
            print("-----------------------------------------------------")

    

lori=User("Lori", "Smith", "email@email.com", age=25,)
lori=BankAccount("checking",0,0.01).deposit(50)
