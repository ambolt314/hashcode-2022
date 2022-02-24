class Contributor:

    # DICT INPUT
    def __init__(self, name, skills):
        """
        dict: skills
        """
        self.name: str = name
        self.skills = skills
        self.is_available = True
        self.busy_until = 0
        self.skill_names = skills.keys()
        self.skill_levels = skills.values()
    
    def assign_project(self, duration: int):
        self.is_available = False
        self.busy_until = duration
    
    def __str__(self):
        return str(self.__dict__)
    
    def next_day(self):
        self.busy_until -= 1
        if self.busy_until <= 0:
            self.busy_until = 0
            self.is_available = True
    
    def unassign(self):
        self.is_available = True
        self.busy_until = 0

    def can_retire(self):
        return True if len(self.skills) > 100 else False

def main():
    name = "Everard"
    skills = {"a": 1, "b": 2, "c": 3}
    person = Contributor(name, skills)
    person.busy_until = 5
    print(person)
    person.next_day()
    person.next_day()
    print(person)


if __name__ == "__main__":
    main()