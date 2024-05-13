import random
from mock.constants import CHOICES


def GetRandomChoice():
    return random.choices(list(CHOICES.keys()), weights=list(CHOICES.values()), k=1)[0]

def GetRandomEmail():
    pass

def GetRandomPersonalChoices(idx : int):
    if idx < 2 or idx > 7:
        return 2
    
    choices = {
        2 : random.randint(1,4),
        3 : random.randint(1,2),
        4 : random.randint(1,3),
        5 : random.randint(1,2),
        6 : random.randint(1,3),
        7 : random.randint(1,3),
    }

    return choices[idx]