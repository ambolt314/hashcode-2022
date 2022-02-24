from contributors import Contributor
from project import Project
from reader import parse
from writer import Writer

(contributors, raw_projects) = parse("a_an_example.in.txt")
(contributors, raw_projects) = parse("d_dense_schedule.in.txt")
(contributors, raw_projects) = parse("d_dense_schedule.in.txt")
(contributors, raw_projects) = parse("e_exceptional_skills.in.txt")
(contributors, raw_projects) = parse("f_find_great_mentors.in.txt")

projects = sorted(raw_projects, key=lambda p : p.best_before)

assigned_projects: "list[Project]" = []

for project in projects:
  #print(project.name, len(project.roles))
  assignees = {}
  for role_name, role_value in project.roles.items():
    role_name = role_name.strip()
    #print(role_name, str(role_value))
    for contributor in contributors:
      #print(contributor.skills)
      to_do = len(assignees) < len(project.roles)
      has_role = role_name in contributor.skills
      if (has_role):
        has_skill = contributor.skills[role_name] >= role_value
        #if has_skill:
          #print(str(to_do) + str(has_role) + str(has_skill) + role_name)
      if (to_do and has_role and has_skill):
        assignees[role_name] = contributor
        break
    
    #print(len(assignees))
    if len(assignees) == len(project.roles):
      project.assignees = assignees
      assigned_projects.append(project)

#print(assigned_projects)

writer = Writer("crape.txt")
for project in assigned_projects:
  writer.do_project(project)
writer.finalise()
