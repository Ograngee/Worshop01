# app.py

class Weapon:
    def __init__(self, name, weapon_type, level=1):
        self.name = name
        self.type = weapon_type
        self.level = level

    def upgrade(self):
        self.level += 1

    def display(self):
        print(f"Weapon: {self.name}\nType: {self.type}\nLevel: {self.level}")

def run():
    weapon1 = Weapon("Sword", "Melee")
    weapon2 = Weapon("Bow", "Ranged")

    weapon1.upgrade()
    weapon2.upgrade()
    weapon2.upgrade()

    weapon1.display()
    weapon2.display()

run()
