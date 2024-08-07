
import pytest
import json
from familyTree import *



@pytest.fixture
def input_json(scope="session"):
    return json.dumps("test_tree.json") 

@pytest.fixture
def json_file(scope="session"):
    return "test_tree.json"

@pytest.fixture
def family_tree(scope="session"):
    tree = {"1": {
        "_name": "Wally",
        "_birth": "2021-08-17",
        "_death": "",
        "_age": 2,
        "_birth_place": "USA",
        "_death_place": None,
        "_gender": "m",
        "_children": [],
        "_mother": [
            "Katie"
        ],
        "_father": [
            "Calvin"
        ],
        "_spouse": None
    },
    "2": {
        "_name": "Katie",
        "_birth": "2018-01-01",
        "_death": "",
        "_age": 6,
        "_birth_place": None,
        "_death_place": None,
        "_gender": "f",
        "_children": [
        ],
        "_mother": [
            "Evie"
        ],
        "_father": [
            "Oscar"
        ],
        "_spouse": None
    },   
    "3": {
        "_name": "Calvin",
        "_birth": "2019-01-01",
        "_death": "",
        "_age": 5,
        "_birth_place": None,
        "_death_place": None,
        "_gender": "m",
        "_children": [
            "Wally"
        ],
        "_mother": [
        
        ],
        "_father": [
        ],
        "_spouse": None
    }
    } 
    return tree

def test_get_tree(family_tree):
    ft = FamilyTree(family_tree)
    assert ft.family_tree
    assert len(family_tree) == 3
    
def test_validate_entry(family_tree):
    ft = FamilyTree(family_tree)
    test01 = ft.validate_new_entry('Wally')
    test02 = ft.validate_new_entry('Coda')
    assert not test01
    assert test02

def test_calculate_age(family_tree):
    date1 = "2013-01-01"
    date2 = "2020-12-31"
    date3 = "2021-01-01"

    ft = FamilyTree(family_tree)
    age1 = ft.calculate_age(date1, date2)
    age2 = ft.calculate_age(date1, date3)
    assert age1 == 7
    assert age2 == 8

def test_add_child(family_tree):
    ft = FamilyTree(family_tree)
    ft.add_child("Katie", "Wally")
    tree = ft.family_tree

    node = tree["2"]["_children"]
    assert node[0] == "Wally"

    ft.add_child("Katie", "Rocket")
    assert len(node) == 2

def test_write_to_json(json_file, family_tree):
    ft = FamilyTree(family_tree)
    result = ft.write_json_data(json_file)
    assert result == f"{json_file} has been successfully updated."
    assert len(json_file) > 0

def test_graph_get_names(family_tree):
    g = Graph()
    result = g.get_names(family_tree)
    assert len(result) == 3
    assert "Wally" in result

       