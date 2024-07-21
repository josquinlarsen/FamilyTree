from datetime import date
from collections import defaultdict

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
    def __init__(self):

        self.family_tree = []

    def create_person(self) -> None:
        """
        Create person to add to tree
        """
        new_person = PersonNode()
        name = input("Enter the person's full name: ")

        while not name:
            print("Please enter a name")
            name = input("Enter the person's full name: ")
            
        new_person._name = name

        new_person._gender = input("Enter their gender: (m, f, nb): ")
        birth = input("Enter the person's date of birth (YYYY-MM-DD). Type '?' if unknown: ")
        new_person._birth = birth
       
        death = input("Enter the person's date of death (YYYY-MM-DD)(Type '?' if unknown or hit enter if still alive): ")

        if death is None:
            death = str(date.today())

        new_person._death = death
        if birth == '?' or death == '?':
            new_person._age = None
        else:
            new_person._age = self.calculate_age(birth, death)

        # validate birth/death 
        new_person._birth_place = input("Enter where the person was born (City, Country): ")
        new_person._death_place = input("Enter where the person died (City, Country): ")

        spouse = input("Enter their spouse's name (Name or 'n/a'): ")
        if spouse.lower() != 'n/a':
            new_person._spouse = spouse

        mother = input("Enter their mother's name: ")
        new_person._mother.append(PersonNode(mother))
        
        father = input("Enter their father's name: ")
        new_person._father.append(PersonNode(father))

        # add person to tree
        self.family_tree.append(new_person)

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
            





if __name__ == "__main__":
    
    ft = FamilyTree()
    ft.create_person()
    print(ft.family_tree[0]._name, ft.family_tree[0]._age)

