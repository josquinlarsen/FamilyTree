from datetime import date
from collections import defaultdict
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
        self.id = 0
        self.family_tree = family_tree

    def print_tree(self): 
        """
        Prints family_tree
        """
        for keys in self.family_tree.keys():
            for k in self.family_tree[keys].keys():
                if self.family_tree[keys][k]:
                    print(self.family_tree[keys][k])
    
    def validate_new_entry(self, name:str) -> bool:
        """
        validates that a name is not already in tree
        """
        tree = self.family_tree
        for k in tree.keys():
            if name in tree[k]["_name"]:
                print(f"{name} is already in the Tree")
                break
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


if __name__ == "__main__":
    with open('tree.json', 'r') as infile:
        tree_data = json.load(infile)
    ft = FamilyTree(tree_data)
    ft.create_person()
    ft.write_json_data('tree.json')
    ft.print_tree()


