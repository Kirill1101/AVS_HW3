from random import randint
import random
import string


def GetRandomName():
    length = random.randint(1, 20)
    letters = string.ascii_lowercase
    name = ""
    for i in range(length):
        name += random.choice(letters)
    return name


def GetRandomNumber(range):
    return randint(1, range)
