from project import Project
import os

class Writer:

    def __init__(self, filename):
        """
        Args:
            filename -- the input data file
        """
        self.projects = 0
        self.filename = f'output/{filename}'
        self.tempfile = f'output/{filename}-working'
        if os.path.exists(self.tempfile):
            os.remove(self.tempfile)
        self.f = open(self.tempfile, 'w')

    def do_project(self, project: Project):
        self.projects += 1
        self.f.write(project.name+'\n')
        names = [project.assignees[role].name for role in project.roles]
        
        self.f.write(' '.join(names)+'\n')
    
    def finalise(self):
        self.f.flush()
        self.f.close()
        with open(self.tempfile) as f:
            lines = f.readlines()
        os.remove(self.tempfile)
        with open(self.filename, 'w') as f:
            f.write(str(self.projects)+'\n')
            f.writelines(lines)
