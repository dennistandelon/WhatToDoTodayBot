from utils.database import projects
from random import randint

length = len(projects)

def get_project()->str:
    r = randint(0,length-1)

    return projects[r]
