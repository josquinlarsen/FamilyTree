from datetime import date
from collections import defaultdict
from pyvis.network import Network

import networkx as nx
import json

class PersonNode:
    def __init__(self, name=None):
        self._name = name
        self._birth = None
        self._death = None
        self._age = None
        self._birth_place = None
        self._death_place = None
        self._gender = None
        self._children = []
        self._mother = []
        self._father = []
        self._spouse = None

class FamilyTree:

    def __init__(self, family_tree=None):
        
        self.family_tree = family_tree
        if len(self.family_tree) == 0:
            self.id = 0
        else: 
            self.id = len(self.family_tree)
            
    def print_tree(self): 
        """
        Prints family_tree
        """
        for keys in self.family_tree.keys():
            for k in self.family_tree[keys].keys():
                if self.family_tree[keys][k]:
                    print((f"{self.family_tree[keys][k]}").strip("[").strip("]").strip("'"), end=" | ")
            print('\t')
            
    def validate_new_entry(self, name:str) -> bool:
        """
        validates that a name is not already in tree
        """
        tree = self.family_tree
        for k in tree.keys():
            if name in tree[k]["_name"]:
                print(f"{name} is already in the Tree")
                return False
        return True 

    def create_person(self) -> None:
        """
        Create person to add to tree
        """
        self.id += 1

        new_person = PersonNode()
        name = input("Enter the person's full name: ")

        while not name:
            print("Please enter a name")
            name = input("Enter the person's full name: ")
        
        check_name = self.validate_new_entry(name)

        while not check_name:
            name = input("Enter the person's full name: ")
        new_person._name = name

        gender = input("Enter their gender: (m, f, nb): ")
        if len(gender) == 0: 
            gender = None
        new_person._gender = gender

        birth = input("Enter the person's date of birth (YYYY-MM-DD). Type '?' if unknown: ")
        new_person._birth = birth
       
        death = input("Enter the person's date of death (YYYY-MM-DD)(Type '?' if unknown or hit enter if still alive): ")
        new_person._death = death

        # validate birth/death 
        if len(birth) == 0 and len(death) == 0:
            new_person._birth = None
            new_person._death = None
            new_person._age = None
            
        else:
            if len(death) == 0:
                death = str(date.today())
                new_person._age = self.calculate_age(birth, death)

            elif birth == '?' or death == '?':
                if birth == '?':
                    new_person._birth = None
                if death == '?':
                    new_person._death = '?'
                new_person._age = None
            else:
                new_person._age = self.calculate_age(birth, death)

            
        birth_place = input("Enter where the person was born (City, Country): ")
        if len(birth_place) == 0:
            birth_place = None
        new_person._birth_place = birth_place

        death_place = input("Enter where the person died (City, Country): ")
        if len(death_place) == 0:
            death_place = None
        new_person._death_place = death_place

        spouse = input("Enter their spouse's name (Name or 'n/a'): ")
        if len(spouse) == 0:
            new_person._spouse = None
        if spouse.lower() != 'n/a':
            new_person._spouse = None
        else:
            new_person._spouse = spouse

        mother = input("Enter their mother's name: ")
        if len(mother) == 0:
            mother = None
        new_person._mother.append(mother)
        
        father = input("Enter their father's name: ")
        if len(father) == 0:
            father = None
        new_person._father.append(father)

        # add person to tree
        self.family_tree[self.id] = new_person

        # write to json
        self.write_json_data('tree.json')

        return f"{name} successfully added to tree."

    def calculate_age(self, birth:str, death:str) -> int:
        """
        Returns the current age in years (if alive) or age at death of person 
        """

        def leap(year):
            """
            Calculate leap year
            """
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                return 1
            return 0
        
        def month_calc(year, month):
            """
            Calculate months
            """
            months = [31, 28 + leap(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            return months[month-1]

        def day_calc(date):
            """
            Calculate total days
            """
            year, month, day = map(int, date.split('-'))
            cnt = 0
            # range of years between 1700, 2100
            for y in range(1700, year):
                cnt += 365 + leap(y)
            for m in range(1, month):
                cnt += month_calc(year, m)

            cnt += day

            return cnt

        return int((day_calc(death) - day_calc(birth)) // 365.25)
    
    def add_person_to_tree(self, person: PersonNode):
        """
        Adds PersonNode to tree, updates relationhips (e.g. parent-child)
        """

        tree = self.family_tree

        if person not in tree:
            tree.append(person)
            
        # connect parents
        if person._mother in tree:
            pass
            
    def write_json_data(self, file_name:str):
        """
        write family tree to JSON for storage
        """
        with open(file_name, 'w') as outfile:
            write_tree = json.dumps(self.family_tree, indent=4, default=lambda o: o.__dict__,)
            outfile.write(write_tree)

    def add_child(self, parent:str, child:str):
        """
        Adds a parent's offspring to their node
        """
        tree = self.family_tree
        for key in tree.keys():
            # if parent not in tree[key]["_name"]:
            #     print(f"{parent}'s node has not been created")
            #     return
            if tree[key]["_name"] == parent:
                if child in tree[key]["_children"]:
                    print(f"{child} has already been added")
                    return 
                tree[key]["_children"].append(child)

        # update tree.json
        self.write_json_data('tree.json')

        print(f"{child} added to {parent}'s node")
        return 

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def get_names_and_ids(self, family_tree) -> list[tuple]:
        """
        Returns a list of names and their id numbers
        from FamilyTree
        """
        names_ids = []

        for entry in family_tree:
            id_num = entry
            name = family_tree[entry]["_name"]
            names_ids.append((id_num, name))

        arrays = self._split_names(names_ids)

        return arrays
    
    def _split_names(self, names_ids:list) -> list:
        """
        Returns array of id numbers in order
        """
        ids = []
        names = []

        for id, name in names_ids:
            ids.append(id)
            names.append(name)

        return ids, names


    def add_edges(self, family_tree):
        """
        adds weighted edges to graph:
        3 = child, 2 = mother, 1 = father
        """

        for entry in family_tree:
            name = family_tree[entry]["_name"]
                
            mother = family_tree[entry]["_mother"][0]
            father = family_tree[entry]["_father"][0]
            if mother and father:
                self.graph[name].append((mother, 2))
                self.graph[mother].append((name, 3))
                self.graph[name].append((father, 1))
                self.graph[father].append((name, 3))

    def print_graph(self):
        """
        prints graph
        """

        print(self.graph)

class GraphVisualizer:


    def __init__(self):
        self.net = Network()

    def add_nodes(self, arrays):
        """
        add nodes to graph visualizer
        """
        ids, names = arrays
        self.net.add_nodes(ids, label=names)

    def display_graph(self):
        """
        Displays graph
        """
        self.net.show("wally_tree.html")

if __name__ == "__main__":
    with open('tree.json', 'r') as infile:
        tree_data = json.load(infile)
    ft = FamilyTree(tree_data)
    g = Graph()
    gv = GraphVisualizer()
    net = Network(height="750px", width="100%")
    # ft.create_person()
    # ft.add_child('Mason', 'Coda')
    # ft.print_tree()
    g.add_edges(ft.family_tree)
    arrays = (g.get_names_and_ids(ft.family_tree))
    ids, names = arrays
    net.add_nodes(ids, label=names)
    net.show("wally_tree.html")



