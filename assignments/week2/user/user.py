
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
    
lori=User("Lori","Smith","lori@email.com",25)
lori.display_user_info()
lori.enroll()
lori.display_user_info()
lori.earn_points(500)
lori.display_user_info()
lori.spend_points(500)
lori.display_user_info()
second_user=User("John","Doe","john@email.com",30)
second_user.display_user_info()
second_user.enroll()
second_user.display_user_info()
second_user.earn_points(500)
second_user.display_user_info()
second_user.spend_points(500)
second_user.display_user_info()
second_user.test_enroll()
third_user=User("Jane","Doe","email@email.com",30)
third_user.test_enroll()
third_user.display_user_info()
third_user.spend_points(500)
third_user.display_user_info()