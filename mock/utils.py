import random
from mock.constants import CHOICES, LEGIT_RESPONSE, LEGIT_RESPONSES


def GetRandomChoice(i : int):
    listNo = random.randint(0,4)
    choice = 0
    try:
        choice = LEGIT_RESPONSES[listNo][i-1]
    except:
        choice = random.randint(1,5)

    print(choice)
    return choice
    # return random.choices(list(CHOICES.keys()), weights=list(CHOICES.values()), k=1)[0]

def GetRandomEmail():

    pass

def GetRandomPersonalChoices(idx : int):
    if idx < 2 or idx > 7:
        return 2
    
    choices = {
        2 : 1,
        3 : 2,
        4 : 1,
        5 : 2,
        6 : 3,
        7 : 3,
    }

    return choices[idx]