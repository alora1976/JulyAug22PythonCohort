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
        return(self)
        
    
    def enroll(self):
        print(self.first_name + " is enrolled in rewards."+"\n"+"Gold Card Points: " + str(self.gold_card_points))
        print("-----------------------------------------------------")
        self.is_rewards_member = True
        self.gold_card_points += 200
        return(self)
        
        

        
    def test_enroll(self):
        if self.is_rewards_member == False:
            
            print(self.first_name + " is not enrolled in rewards.")
            self.enroll()
        if self.is_rewards_member == True:
            
            print(self.first_name + " is now enrolled in rewards."+"\n"+"Gold Card Points: " + str(self.gold_card_points))   
            print("-----------------------------------------------------")
        return(self)
            
        
        
    
    def spend_points(self,amount):
        self.gold_card_points -= amount
        
        print(self.first_name + " has spent " + str(amount) + " points.")
        if self.gold_card_points < 0:
            
            print(self.first_name + " has insufficient points.")
            self.gold_card_points = 0
            
            print("-----------------------------------------------------")
        return(self)
        

    def earn_points(self,amount):
        self.gold_card_points += amount
        
        print(self.first_name + " has earned " + str(amount) + " points.")
        if self.gold_card_points > 10000:
            
            print(self.first_name + " has exceeded the maximum points.")
            self.gold_card_points = 10000
            
            print("-----------------------------------------------------")
        return(self)
        
lori=User("Lori","Smith","lori@email.com",25)
lori.display_user_info().enroll().test_enroll().spend_points(500).earn_points(500).display_user_info()

