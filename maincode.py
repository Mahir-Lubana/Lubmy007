'''
File: maincode.py
Description: Main code file for assignment 2 
Author: Mahir Lubana
StudentID: 110408840
EmailID: Lubmy007
This is my own work as defined by the University's Academic Misconduct Policy.
'''




class Alchemist:
    def __init__(self, attack, strength, magic, defense, ranged, laboratory, necromancy):
        self.attack = attack
        self.strength = strength
        self.magic = magic 
        self.defense = defense
        self.ranged = ranged
        self.laboratory = laboratory
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
    

    def getLaboratory(self):
        return self.laboratory
    
    def getRecipes(self):
        return self.recipes 
    
    def mixpotion(self, potion_name):
        if potion_name in self.recipes:
            ingredients = self.recipes[potion_name]
            primary_ingredient, secondary_ingredient = ingredients
            self.laboratory.mixPotion(potion_name, "some_type", "some_stat", primary_ingredient, secondary_ingredient)
        else:
            print(f'Error: Unknown potion recipe {potion_name} ')
    
    def drinkPotion(self, potion):
        pass

    def collectReagent(self, reagent, amount):
        self.laboratory.addReagent(reagent, amount)
    
    def refineReagents(self):
        self.laboratory.refineReagents()




class Laboratory:
    def __init__(self):
        self.potions = []
        self.herbs = []
        self.catalysts = []

    def addPotion(self, potion):
        self.potions.append(potion)
    
    def addHerb(self, herb):
        self.herbs.append(herb)

    def addCatalyst(self, catalyst):
        self.catalysts.append(catalyst)

    def mixPotion(self, name, type, stat, primaryIngredient, secondaryIngredient):
        
        pass

    def addReagent(self, reagent, amount):

        pass

    def refineReagent(self):

        pass






