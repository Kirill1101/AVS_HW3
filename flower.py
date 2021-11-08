from plant import *
from enum import Enum
from rnd import *

class Type(Enum):
    HOME = 1
    GARDEN = 2
    WILD = 3


def GetType(n):
    if n == '1':
        return Type.HOME
    elif n == '2':
        return Type.GARDEN
    elif n == '3':
        return Type.WILD


class Flower(Plant):

    def __init__(self):
        self.name = ""
        self.type = Type.HOME

    def ReadStrArray(self, strArray, i):
        # должно быт как минимум два непрочитанных значения в массиве
        if i >= len(strArray) - 1:
            return 0
        self.type = GetType(strArray[i])
        self.name = strArray[i + 1]
        i += 2
        return i

    def InRnd(self):
        self.type = GetType(str(GetRandomNumber(3)))
        self.name = GetRandomName()
        pass

    def Write(self, ostream):
        ostream.write("It is Flower. Type: {}. Name: {}. Quotient of division: {}".format(self.type.name,
                                                                                          self.name, self.Quotient()))
        pass

    def Quotient(self):
        vowels = 0
        for letter in self.name.lower():
            for vowel in "aeiouy":
                if vowel == letter:
                    vowels += 1
        return vowels / len(self.name)
        pass
