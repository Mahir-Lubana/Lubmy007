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













