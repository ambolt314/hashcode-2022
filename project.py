from contributors import Contributor

class Project:
    name = ""
    completion_score = 0
    

    # given in days
    best_before = 0 
    duration = 0
    start_date = 0

    roles = {} # Can this be a dict?
    person_to_role = {} # I'm thinking this should be {'person' : 'role'}

    assignees = {}

    def __init__(self, name, completion_score, best_before, duration, roles):
        self.name = name
        self.completion_score = completion_score
        self.best_before = best_before
        self.duration = duration
        self.roles = roles
        self.start_date = best_before - duration
        self.assignees = dict()

    def update_score(self, cur_day):
        if self.completion_score != 0:
            if cur_day > self.start_date:
                self.completion_score -= 1

    def get_project_score(self):
        return max(self.completion_score, 0)
            
    def __str__(self):
        return str(self.__dict__)

    def can_assign(self, person: Contributor):
        """
        return: str: role to assign to person
        """
        possible_roles = list(set(person.skill_names).intersection(set([r.strip() for r in self.roles])))
        for role in possible_roles:
            if person.skills[role] == self.roles[role]:
                return role
            if person.skills[role] > self.roles[role]:
                return role
        return False
    
    def assign(self, assignee: Contributor, role):
        """
        return: Dict[str role: Contributor: assignee]
        """
        self.assignees[role] = assignee


    def full(self):
        if len(self.roles) == len(self.assignees.keys()):
            #print(self.roles, self.assignees.keys())
            return True
        return False


    def unassign(self):
        """
        Unassign all assignees and reset status
        """
        for c in self.assignees.values():
            c.unassign()
        self.assignees = {}

    def learn(self):
        for skill, c in self.assignees.items():
            level = c.skills[skill] 
            if level <= self.roles[skill]:
                if level < 10:
                    c.skills[skill] += 1