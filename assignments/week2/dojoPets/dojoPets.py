class Pet:

    # implement __init__( name , type , tricks ):
    def __init__(self, name , type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50
        self.noise = noise

    # implement the following methods:
    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        return self

    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    # play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        self.energy -= 15
        return self

    # noise() - prints out the pet's sound
    def noise(self):
        print("Ruff!")
        return self



class Ninja:
    # implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name, last_name , treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        return self

    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):

        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            print(f"Feeding {self.pet.name} {food}!")
            self.pet.eat()
        else:
            print("You are out of food!")
        return self

    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.noise()
        return self
# use inheritance to create a class called Cat that inherits from Pet
class Cat(Pet):
    def __init__(self, name, type, tricks, noise):
        super().__init__(name, type, tricks, noise)
        self.health = 100
        self.energy = 50
        self.noise = noise
    def play(self):
        self.health += 5
        self.energy -= 15
        return self
    def noise(self):
        print("meow")
        return self
        
my_treats = ['Sandwich','Bacon',"Trash Bag"]
my_pet_food = ['Pizza','Burger']

copper = Pet("Copper","Dog",['barks a lot','is cute'],"RUFF RUFF")

lori = Ninja("lori","T",my_treats,my_pet_food, copper)

lori.feed()
lori.feed()
lori.feed()
lori.bathe()

