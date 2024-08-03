import unittest
import pytest
import json
from familyTree import *


class TestFamilyTree(unittest.TestCase):

    @pytest.fixture
    def input_json():
        return json.dumps("test_tree.py") 
        

    def test_calculate_age(self):
        date1 = "2013-01-01"
        date2 = "2020-12-31"
        date3 = "2021-01-01"
        ft = FamilyTree
        age1 = ft.calculate_age(self, date1, date2)
        age2 = ft.calculate_age(self, date1, date3)
        self.assertEqual(age1, 7)
        self.assertEqual(age2, 8)

    # def test_add_child(self, input_json):
    #     """
    #     this needs fixing (getting data from JSON test file)
    #     """
    #     ft = FamilyTree(input_json)
    #     tree = ft.family_tree
    #     ft.add_child("Katie", "Wally")
    #     node = tree["2"]["_children"][0]
    #     self.assertEqual(node, "Wally")

    

    



if __name__ == "__main__":
    unittest.main()
        