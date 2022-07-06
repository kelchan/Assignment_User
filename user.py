class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        info = [
            self.first_name,
            self.last_name,
            self.email,
            "Age - " + str(self.age),
            "Reward Member - " + str(self.is_rewards_member),
            "Gold Points - " + str(self.gold_card_points)
        ]
        print(info)
        return self

    def enroll(self):
        if self.is_rewards_member == True:
            print( "Is already a member!" )
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print( "Not enough points!" )
        elif self.gold_card_points >= amount:
            self.gold_card_points = self.gold_card_points - amount

Kelvin = User("Kelvin", "Chan", "kelvin.chan131@gmail.com", 23)
Kelvin.enroll().spend_points(50)

User2 = User("Jane", "Doe", "janedoe@gmail.com", 24)
User2.enroll().spend_points(80)

Kelvin.display_info(), User2.display_info()

Kelvin.enroll()

User3 = User("Billy", "Bob", "billybob@gmail.com", 25)
User3.display_info().spend_points(40)
