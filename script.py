'''
Create a Game Using Classes and Objects
Welcome! You should now be equipped with everything you need to make a complicated program that uses multiple classes that interact with each other. This is where we turn the creativity over to you.
For this project, we want you to create a fully functional system that involves multiple classes. We’ll give more details on the specific requirements below.
We know that it can sometimes be hard to come up with an idea on your own. Take some time to think of what you want to create — it truly can be anything. This step is important! We want you to feel motivated to complete this project, so pick something you’re excited to make.
Requirements
1.
You must create at least TWO classes.
For now, just focus on:
Planning Your Two Classes
Creating a Basic Constructor (__init__() method)
2.
Each of those classes must have at least THREE attributes and THREE methods.
You may need to create some instances of your classes to test your methods.
3.
Your classes should be able to describe themselves (through a __repr__() method).
You will need to create at least one instance of your classes to test your __repr__() method.
4.
If you haven’t already, create at least TWO instances of every one of your classes.
Test all of the methods you created on both of the objects you create.
5.
Create some methods, or additional attributes, that make your two Classes able to interact with each other.
'''

import random

CHARACTER_STATS = {
    "knight": {
        "health": 100,
        "damage": 20,
        "defense": 15,
        "speed": 1
    },
    "wizard": {
        "health": 80,
        "damage": 25,
        "defense": 8,
        "speed": 1.5
    },
    "goblin": {
        "health": 65,
        "damage": 15,
        "defense": 3,
        "speed": 2
    }
}

ENEMY_STATS = {
    "orc": {
        "health": 150,
        "damage": 30,
        "defense": 30,
        "speed": 0.5
    },
    "spirit": {
        "health": 20,
        "damage": 150,
        "defense": 0.1,
        "speed": 3
    },
    "zombie": {
        "health": 20,
        "damage": 10,
        "defense": 5,
        "speed": 1.5
    }
}
class Hero:
    def __init__(self, name):
        self.name = name
        self.character_class = None
        self.health = None
        self.damage = None
        self.defense = None
        self.speed = None
        self.is_turn = True
        self.choose_character()

    def __repr__(self):
        return f"{self.name} is a {self.character_class}!"

    def choose_character(self):
        character_class = input("Please select either 'knight', 'wizard', or 'goblin': ").lower()
        while character_class not in CHARACTER_STATS:
            print("Not a valid character class!")
            character_class = input("Please select either 'knight', 'wizard', or 'goblin': ").lower()

        self.character_class = character_class
        self.health = CHARACTER_STATS[character_class]['health']
        self.damage = CHARACTER_STATS[character_class]['damage']
        self.defense = CHARACTER_STATS[character_class]['defense']
        self.speed = CHARACTER_STATS[character_class]['speed']
        self.start_game(Enemy(self.select_random_enemy()))

    def attack(self, other):
        attack_damage = self.damage * self.speed
        effective_damage = attack_damage - other.defense
        other.health -= abs(effective_damage)
        return f"The {other.type} now has {other.health} health."

    def select_random_enemy(self):
        return random.choice(['orc', 'spirit', 'zombie'])

    def check_win(self, other):
        if self.health <= 0:
            return f"{self.name} has succumbed to their injuries!"
        elif other.health <= 0:
            return f"{self.name} has defeated the {other.type}"
        else:
            if self.is_turn:
                print(f"{other.type} is still alive with {other.health}!")
            else:
                print(f"You're still alive with {self.health}, keep it up!")
            other.change_turns(self)

    def start_game(self, other):
        print(\
            f"""
            Welcome, {self.name}!
            It is great to have you here.
            We are in need of a Hero such as yourself!
            A(n) {other.type} has attacked, and we are all in danger!
            Please, save us!
            """
            )
        while self.health > 0 and other.health > 0:
            if self.is_turn:
                print(f"You attack the {other.type}.")
                self.attack(other)
                self.check_win(other)
            else:
                other.attack(self)
                self.check_win(other)
        return "Thanks for playing!"


class Enemy:
    def __init__(self, type):
        self.type = type
        self.health = None
        self.damage = None
        self.defense = None
        self.speed = None
        self.is_turn = False
        self.assign_stats()

    def __repr__(self):
        return \
        f"""
        This enemy is a(n) {self.type}.
        It has {self.health} health.
        It has {self.damage} damage.
        It has {self.defense} defense.
        It has {self.speed} speed.
        It is my turn: {self.is_turn}.
        """

    def assign_stats(self):
        if self.type not in ENEMY_STATS.keys():
            print("Invalid enemy type")
            raise ValueError

        self.health = ENEMY_STATS[self.type]['health']
        self.damage = ENEMY_STATS[self.type]['damage']
        self.defense = ENEMY_STATS[self.type]['defense']
        self.speed = ENEMY_STATS[self.type]['speed']

    def attack(self, other):
        attack_damage = self.damage * self.speed
        effective_damage = attack_damage - other.defense
        other.health -= abs(effective_damage)
        return f"You now have {other.health} health."

    def change_turns(self, other):
        if self.is_turn:
            self.is_turn = False
            other.is_turn = True
        else:
            other.is_turn = False
            self.is_turn = True



ben = Hero('Ben')



