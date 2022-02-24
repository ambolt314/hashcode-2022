from reader import parse
from project import Project
from writer import Writer

filenames = ['a_an_example.in.txt',
             'b_better_start_small.in.txt',
             'c_collaboration.in.txt',
             'd_dense_schedule.in.txt',
             'e_exceptional_skills.in.txt',
             'f_find_great_mentors.in.txt']
filename = filenames[5]

output = Writer(filename)
contributors, raw_projects = parse(filename)
#print(raw_projects)
projects = sorted(raw_projects, key=lambda p : p.best_before)
#print("contributors")
#print(contributors)
#print("------------------")
#print(projects)


day=0
# Do a new day if projects aren't empty
while(len(projects) > 0):
    #print(f"Day: {day}")
    # Update availability
    for c in contributors:
        c.next_day()
    # List of only people who are available to work today
    available_contributors = [c for c in contributors if c.is_available]
    #print("All contributors: ", [p.name for p in contributors])
    #print("Available contributors: ", [p.name for p in available_contributors])
    do_later = []
    for p in projects:
        assigned = False
        p.update_score(day)
        score = p.get_project_score()
        if score <= 0:
            continue
        # Check if any contributors have the right skills
        for c in available_contributors:
            role_to_assign = p.can_assign(c)
            if role_to_assign:
                c.assign_project(p.duration)  # Assign project INTO contributor
                p.assign(c, role_to_assign)  
            if p.full():
                p.learn()
                output.do_project(p)
                break
        else: # This is a for else
            print(f"Day: {day} - On the for else loop")
            do_later.append(p)

    projects = do_later
    day += 1

output.finalise()
# PSEUDO CODE ALGORITHM

# main loop: increment day
# on each day:
#   for person in contributors:
#       person.busy_until -= 1 unless 0
#       (handled by contribtor class: if busy_until==0, is_available=True)
#   for each project in [projects to start today]
#       if project.score <=0:
#           remove project from list
#       for each role in project:
#           """Do we make a dict for each role?
#           e.g python = {name: skill_level, ....}
#               HTML = {name: skill_level, ...}
#           get the name with the lowest skill level > required skill level AND contributor.is_available
#           assign that contributor to that project
#           set contributor to is_available=False
#       if all roles assigned:
#           remove project from list
#           


#for each project:
#   if anyone has the skills:
#      assign people
#   else:
#      add project to do_later list
