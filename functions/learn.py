from utils.database import tech_stack
from random import randint

length = len(tech_stack)

def get_tech()->str:
    r = randint(0,length-1)

    return tech_stack[r]
