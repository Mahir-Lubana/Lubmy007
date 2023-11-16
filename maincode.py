'''
File: maincode.py
Description: Main code file for assignment 2 
Author: Mahir Lubana
StudentID: 110408840
EmailID: Lubmy007
This is my own work as defined by the University's Academic Misconduct Policy.
'''


class Laboratory:
    """
    The Laboratory class is a facility for alchemist's potions crafting.

    Potions: will be a list to store the potion instances 
    herbs: will be a list and store herb instances 
    catalysts: will be a list to store catalysts instances

    """

    def __init__(self):
        """Initalises the  Laboratory instance with empty lists for the potions, herbs and catalysts"""
        
        self.potions = []
        self.herbs = []
        self.catalysts = []

    def addPotion(self, potion):
        """It Adds a potion to the laboratory's collection"""

        self.potions.append(potion)
    
    def addHerb(self, herb):
        """It Adds a herb to the laboratory's collection"""

        self.herbs.append(herb)

    def addCatalyst(self, catalyst):
        """It Adds a catalysts to the laboratory's collection"""

        self.catalysts.append(catalyst)

    def mixPotion(self, name, type, stat, primaryIngredient, secondaryIngredient):
        """mixing the potions in the laboratory"""
        
        pass

    def addReagent(self, reagent, amount):
        """"adding a reagent to the laboratory's collection """

        pass

    def refineReagent(self):
        """ refining the reagents in laboratory"""

        pass



class Alchemist:

    """ 
    The Alchemist class is representing an alchemist with various attributes and capabilities of its behaviour.
    __________________________________________________________________________________________________________
    attack: is an attribute which indicates that alchemist's combats prowess in physical attacks.
    strength: is an attribute and incicates alchemist's strength.
    magic: is an attribute and is alchemist's proficiency and magic abilities.
    defense: is an attribute and indicates the ability of alchemsit's to withstand attacks.
    ranged: is an attribute for alchemist's skill in ranged combat.
    laboratory: is associated with alchemist in order to provide facility for the herbs, potions and catalysts.
    necromancy: is an attribute for indicating the alchemist's proficiency in the necromantic parts.
    recipes: is a dictionary which contains recipe of potions and ingredients needed to create different types of potions.
    """

    def __init__(self, attack, strength, magic, defense, ranged, laboratory, necromancy):

        """ Initalises the Alchemist instance."""

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
        """ It will return the associated laboratory """

        return self.laboratory
    
    def getRecipes(self):
        """ it will return the recipes of potions  """

        return self.recipes 
    
    def mixpotion(self, potion_name):
        """ mixing the potions by utilising laboratory """

        if potion_name in self.recipes:
            ingredients = self.recipes[potion_name]
            primary_ingredient, secondary_ingredient = ingredients
            self.laboratory.mixPotion(potion_name, "some_type", "some_stat", primary_ingredient, secondary_ingredient)
        else:
            print(f"Error: Unknown potion recipe {potion_name} ")
    
    def drinkPotion(self, potion):
        """its a method for drinking a potion"""

        pass

    def collectReagent(self, reagent, amount):
        """it Collects reagant and adds it to laboratory """

        self.laboratory.addReagent(reagent, amount)
    
    def refineReagents(self):
        """"refining reagents in the laboratory """

        self.laboratory.refineReagents()
