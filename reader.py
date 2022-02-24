from contributors import Contributor
from project import Project

def parse(filename):
    """
    Parse filename into a problem

    Args:
       a filename

    Returns:
      list of people
      list of projects   # note these could be dict
    """
    people: "list[Contributor]" = []
    projects: "list[Project]" = []
    with open(f'data/{filename}') as f:
        tokens = f.readline().split()
        num_people = int(tokens[0])
        num_projects = int(tokens[1])
        for _ in range(num_people):
            tokens = f.readline().split()
            name = tokens[0]
            num_skills = int(tokens[1])
            skills = {}
            for _ in range(num_skills):
                tokens = f.readline().split()
                skill = tokens[0]
                score = int(tokens[1])
                skills[skill] = score
            person = Contributor(name, skills)
            people.append(person)
        
        for _ in range(num_projects):
            tokens = f.readline().split()
            name = tokens[0]
            days = int(tokens[1])
            score = int(tokens[2])
            best_before = int(tokens[3])
            num_roles = int(tokens[4])
            roles = {}
            for _ in range(num_roles):
                tokens = f.readline().split()
                role_name = tokens[0]
                role_score = int(tokens[1])
                while role_name in roles:
                    role_name += ' '
                roles[role_name] = role_score
            project = Project(name=name,
                              completion_score=score,
                              best_before=best_before,
                              duration=days,
                              roles=roles)
            projects.append(project)
    return people, projects
