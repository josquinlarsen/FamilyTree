class PersonNode:
    def __init__(self, name=None):
        self._name = name
        self._birth = None
        self._death = None
        self._age_at_death = None
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
        new_person._birth = input("Enter the person's date of birth (YYYY-MM-DD)")
        new_person._birth_place = input("Enter where the person was born (City, Country: ")
        new_person._death = input("Enter the person's date of death (YYYY-MM-DD)")

        # validate birth/death 
        new_person._death_place = input("Enter where the person died (City, Country: ")

        spouse = input("Enter their spouse's name (Name or 'n/a'): ")
        if spouse.lower() != 'n/a':
            new_person._spouse = spouse

        mother = input("Enter their mother's name: ")
        new_person._mother.append(PersonNode(mother))
        
        father = input("Enter their father's name: ")
        new_person._father.append(PersonNode(father))

        self.family_tree.append(new_person)

if __name__ == "__main__":
    p = PersonNode()
    ft = FamilyTree()
    ft.create_person()
    print(ft.family_tree[0]._name)

