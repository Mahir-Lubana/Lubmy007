"""
File: testcode.py
Description: Test code file for assignment 2 
Author: Mahir Lubana
StudentID: 110408840
EmailID: Lubmy007
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import pytest
from maincode import Laboratory, Herb, Catalyst, Potion

@pytest.fixture
def lab():
    return Laboratory()

@pytest.fixture
def herb():
    return Herb(name="Testing Herb", potency=2.0)

@pytest.fixture
def catalyst():
    return Catalyst(name="Testing Catalyst", potency=3.0, quality=1.5)

@pytest.fixture
def potion():
    return Potion(name="Testing Potion", stat="Testing Stat", boost=5.0)

def testing_add_potion(lab, potion):
    lab.addPotion(potion)
    assert lab.potions == [potion]

def testing_add_herb(lab, herb):
    lab.addHerb(herb)
    assert lab.herbs ==[herb]

def testing_add_catalyst(lab, catalyst):
    lab.addCatalyst(catalyst)
    assert lab.catalyst == [catalyst]

def testing_mix_potion(lab, herb,catalyst):
    lab.addHerb(herb)
    lab.addCatalysts(catalyst)
    lab.mixPotion(name= "Testing Potion", type= "Super", stat="Testing Stat", primaryIngredient= "Testing Herb", secondaryIngredient="Testing Catalyst")
    assert len(lab.potions) == 1
    assert lab.potions[0].getName() == "Testing Potion"

def testing_add_reagent(lab,herb, catalyst):
    lab.addReagent(herb, amount=1)
    lab.addReagent(catalyst, amount=1)
    assert lab.herbs == [herb]
    assert lab.catalysts == [catalyst]

def testing_refine_reagents(lab, herb, catalyst):
    lab.addHerb(herb)
    lab.addCatalyst(catalyst)
    lab.refineReagents()
    assert not lab.herbs[0].isGrimy()
    assert lab.herbs[0].getPotency() == 5.0
    assert catalyst.getQuality() == 2.6
    
