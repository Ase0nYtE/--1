import copy
from dataclasses import dataclass
from typing import List

@dataclass
class Weapon:
    name: str
    damage: int

@dataclass
class Armor:
    name: str
    defense: int

@dataclass
class Skill:
    name: str
    power: int

class Character:
    def __init__(self,
                 name: str,
                 health: int = 100,
                 strength: int = 10,
                 agility: int = 10,
                 intelligence: int = 10):
        self.name = name
        self.health = health
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.weapon: Weapon | None = None
        self.armor: Armor | None = None
        self.skills: List[Skill] = []

    def add_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def add_armor(self, armor: Armor):
        self.armor = armor

    def add_skill(self, skill: Skill):
        self.skills.append(skill)

    def clone(self) -> 'Character':
        return copy.deepcopy(self)

    def show_info(self):
        print(f"Character: {self.name}")
        print(f"  Health: {self.health}")
        print(f"  Strength: {self.strength}")
        print(f"  Agility: {self.agility}")
        print(f"  Intelligence: {self.intelligence}")
        if self.weapon:
            print(f"  Weapon: {self.weapon.name} (damage {self.weapon.damage})")
        if self.armor:
            print(f"  Armor: {self.armor.name} (defense {self.armor.defense})")
        if self.skills:
            print("  Skills:")
            for s in self.skills:
                print(f"    - {s.name} (power {s.power})")
        print("-" * 40)

if __name__ == "__main__":
    template = Character("Template", health=120, strength=18, agility=8, intelligence=12)
    template.add_weapon(Weapon("Sword", 25))
    template.add_armor(Armor("Chainmail", 15))
    template.add_skill(Skill("Strike", 40))

    player1 = template.clone()
    player1.name = "Player1"
    player1.health = 150

    template.show_info()
    player1.show_info()