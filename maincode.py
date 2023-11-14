'''
File: maincode.py
Description: A brief description of this Python module.
Author: Mahir Lubana
StudentID: 110408840
EmailID: Lubmy007
This is my own work as defined by the University's Academic Misconduct Policy.
'''
#Alchemist class 
class Alchemist:
    def __init__(self, attack, strength, magic, defense, ranged, laboratory, necromancy):
        self.attack = attack
        self.strength = strength
        self.magic = magic 
        self.defense = defense
        self.ranged = ranged
        self.laboratory = Laboratory()
        self.necromancy = necromancy
        self.recipes = {
            "Super Attack": ["Irit", "Eye of Newt"],
            "Super Strength": ["Kwuarm", "Limpurt Root"],
            "Super Defence": ["Cadantine", "White Berries"],
            "Super Magic": ["Lantadyme", "Potato Cactus"],
            "Super Ranging":["Dwarf Weed", "Wine of Zamorak"],
            "Super Necromancy":["Arbuck", "Blood of Orcus"],
            "Extreme Attack":["Avantoe", "Super Attack"],
            "Extreme Strength":["Dwarf Weed", "Super strength"],
            "Extreme Defence":["Lantadyme", "Super Defence"],
            "Extreme Magic":["Ground Mud Rune", "Super Magic"],
            "Extreme Ranging":["Grenwall Spike", "Super Ranging"],
            "Extreme Necromancy":["Ground Miasama Rune", "Super Necromancy"] 
        }

class Laboratory:
    def __init__(self):
        self.potions = []
        self.herbs = []
        self.catalysts = []







