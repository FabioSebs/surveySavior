import random
from mock.constants import CHOICES, LEGIT_RESPONSE


def GetRandomChoice(i : int):
    choice = 0
    try:
        choice = LEGIT_RESPONSE[i]
    except:
        choice = random.randint(1,5)

    # add some spice
    if random.randint(1,5) > 3 and choice > 3 and choice != 5:
        choice+=1
    
    if random.randint(1,5) < 3 and choice < 3 and choice != 1:
        choice-=1
    
    return choice
    # return random.choices(list(CHOICES.keys()), weights=list(CHOICES.values()), k=1)[0]

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