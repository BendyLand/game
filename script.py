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
class Hero:
    def __init__(self, name):
        self.name = name
        self.character_class = None
        self.health = None
        self.damage = None
        self.defense = None
        self.speed = None
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