
import pytest
import json
from familyTree import *



@pytest.fixture
def input_json():
    return json.dumps("test_tree.json") 

def test_get_tree(input_json):
    ft = FamilyTree(input_json)
    assert len(ft.family_tree) == 3
    

def test_calculate_age(input_json):
    date1 = "2013-01-01"
    date2 = "2020-12-31"
    date3 = "2021-01-01"

    ft = FamilyTree(input_json)
    age1 = ft.calculate_age(date1, date2)
    age2 = ft.calculate_age(date1, date3)
    assert age1 == 7
    assert age2 == 8

def test_add_child(input_json):
    """
    this needs fixing (getting data from JSON test file)
    """
    # ft = FamilyTree(input_json)
    # ft.add_child("Katie", "Wally")
    

    # node = tree["2"]["_children"][0]
    # assert node == "Wally"

       