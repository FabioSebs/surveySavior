import random
from mock.constants import CHOICES


def GetRandomChoice():
    return random.choices(list(CHOICES.keys()), weights=list(CHOICES.values()), k=1)[0]

def GetRandomEmail():
    pass