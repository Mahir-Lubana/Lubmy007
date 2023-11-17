"""
File: maincode.py
Description: Main code file for assignment 2 
Author: Mahir Lubana
StudentID: 110408840
EmailID: Lubmy007
This is my own work as defined by the University's Academic Misconduct Policy.
"""



class Laboratory:
    """
    The Laboratory class is a facility for alchemist's potions crafting.

    Potions: will be a list to store the potion instances 
    herbs: will be a list and store herb instances 
    catalysts: will be a list to store catalysts instances

    """

    def __init__(self):

        self.potions = []
        self.herbs = [
            Herb(name="Arbuck", potency=2.6),
            Herb(name="Avantoe", potency=3.0),
            Herb(name="Cadantine", potency=1.5),
            Herb(name="Dwarf Weed", potency=2.5),
            Herb(name="Irit", potency=1.0),
            Herb(name="Kwuarm", potency=1.2),
            Herb(name="Lantadyme", potency=2.0),
            Herb(name="Torstol", potency=4.5)
        ]

        self.catalysts = [
            Catalyst(name="Eye of Newt", potency=4.3, quality=1.0),
            Catalyst(name="Limpwurt Root", potency=3.6, quality=1.7),
            Catalyst(name="White Berries", potency=1.2, quality=2.0),
            Catalyst(name="Potato Cactus", potency=7.3, quality=0.1),
            Catalyst(name="Wine of Zamorak", potency=1.7, quality=5.0),
            Catalyst(name="Blood of Orcus", potency=4.5, quality=2.2),
            Catalyst(name="Ground Mud Rune", potency=2.1, quality=6.7),
            Catalyst(name="Grenwall Spike", potency=6.3, quality=4.9),
            Catalyst(name="Ground Miasma Rune", potency=3.3, quality=5.2)
        ]

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

        primary= next((herb for herb in self.herbs if herb.getName()== primaryIngredient), None)
        secondary= next((catalyst for catalyst in self.catalysts if catalyst.getName()== secondaryIngredient), None)

        if primary and secondary:

            if type == "Super":
                
                boost = primary.getPotency() + (secondary.getPotency() * secondary.getQuality()) * 1.5
                boost = round(boost, 2)


            elif type == "Extreme":
                
                boost = (primary.getPotency() * secondary.getBoost()) * 3.0
                boost = round(boost, 2)
            
            else:
                boost =1.0

            
            potion = Potion(name=name, stat=stat, boost=boost)
            self.addPotion(potion)

        else:
            print(f"Error: Unknown ingredients for potion {name}.")


    
    def addReagent(self, reagent, amount):
        """"adding a reagent to the laboratory's collection """


        if isinstance(reagent, Herb):
            self.herbs.append(reagent)

        elif isinstance(reagent, Catalyst):
            self.catalysts.append(reagent)

        

    def refineReagents(self):
        """ refining the reagents in laboratory"""

        for herb in self.herbs:
            herb.refine()

        for catalyst in self.catalysts:
            catalyst.refine()




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



class Reagent:
    """Reagent class is a basic ingredient with name and potency.
     
      it follows potency value of the reagent and name of reagent.
      -potency(float)
      -name(string)"""



    def __init__(self, potency, name):

        self.potency = potency
        self.name = name

    def getName(self):
        return self.name
    
    def getPotency(self):
        return self.potency
    
    
class Herb(Reagent):
    """Herb class is representing reagent which is used in potion making and is a sub-class of Reagent.

      -grimy: is an attribute and it indicates that if the herb is in a grimy or refined state.
      -potency: is an attribute and it for determining the effectiveness in potion making.   
    
    
    """



    def __init__(self, *args, **kwargs):


        super().__init__(*args, **kwargs)
        self.grimy = True


    def refine(self):
        """refining the herb and multiplying its potency by value of 2.5"""

        self.grimy = False
        self.potency *= 2.5
        print(f"{self.name} has been refined. Potency is now {self.potency:.2f}.")

    def isGrimy(self):
        """checks if the herb is grimy and if it is grimy then 
        it will return true else false """

        return self.grimy
    
    
class Catalyst(Reagent):
    """The Catalysts is part of reagent which is used in potion making and is a sub-class of Reagent.

    -quality: is an attribute for catalysts and its effectiveness in potion making.
    
    """
    


    def __init__(self, quality, *args, **kwargs):


        super().__init__(*args, **kwargs)
        self.quality = quality

    
    def refine(self):
        """Refining the catalyst, increasing its quality by 1.1 and up to a maximum 10"""

        if self.quality < 8.9:
            self.quality += 1.1
            print(f"{self.name} has been refined. Quality is now {self.quality:.2f}.")

        else:
            self.quality = 10
            print(f"{self.name} cannot be refined any further. Quality is now 10.")

    def getQuality(self):

        return self.quality    





class Potion:
    """The potion class is a generic potion in potion making
    
    stat: is an attribute and is affected by the (attack, defense and etc).
    name: is an attribute for potion name 
    boost: is an attribute and boost provided by the potion
    
    
    
    """

    def __init__(self, stat, name, boost):


        self.name = name
        self.stat = stat
        self.boost = boost

    def calculateBoost(self):
        """calculating and then return the boost provided by potion"""

        return self.boost
    

    def getName(self):

        return self.name
    
    def getStat(self):

        return self.stat
    
    def getBoost(self):

        return self.boost
    
    def setBoost(self, boost):

        self.boost = boost


class SuperPotion(Potion):
    """The Superpotion class is a sub-class of Potion  but has more enhanced properties.
    
    Attributes used:
    -herb
    -catalyst
    -stat
    -name
    -boost
    """

    def __init__(self, herb, catalyst, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.herb = herb
        self.catalyst = catalyst

    def calculateBoost(self):
        """it calculates and retun the boost prvoided to the super potion 
        and it also Overrides the method in Potion in order to provide a boost calculation."""

        return self.herb.getPotency() + (self.catalyst.getPotency()* self.catalyst.getQuality()) * 1.5
    
    def getHerb(self):

        return self.herb
    
    def getCatalyst(self):

        return self.catalyst
    

class ExtremePotion(Potion):
    """The class of ExtremePotion is a different type of potion with other properties
    
    Attributes:
    -reagent:
    -potion:
    -stat
    -name
    -boost
    
    """


    def __init__(self, reagent, potion, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.reagent= reagent
        self.potion= potion

    def calculateBoost(self):

        return (self.reagent.getPotency() * self.potion.getBoost()) *3.0
    
    
    def getPotion(self):

        return self.potion
    
    def getReagent(self):

        return self.reagent
    


lab= Laboratory()

alchemist = Alchemist(attack=85, strength=70, magic=90, defense=75, ranged=65, necromancy=60, laboratory=lab)

alchemist.mixpotion("Super Attack")

herb= Herb(name= "New Herb", potency=2.0)
alchemist.collectReagent(herb, amount=1)
alchemist.refineReagents()


print("\n State of the Laboratory")
print("Herbs:", [herb.getName() for herb in lab.herbs])
print("Catalysts:", [catalyst.getName() for catalyst in lab.catalysts])
print("Potion:", [potion.getName() for potion in lab.potions])
    






