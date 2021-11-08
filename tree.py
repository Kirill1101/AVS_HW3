from plant import *
from rnd import *


class Tree(Plant):
    def __init__(self):
        self.name = ""
        self.age = 0

    def ReadStrArray(self, strArray, i):
        # должно быт как минимум два непрочитанных значения в массиве
        if i >= len(strArray) - 1:
            return 0
        self.age = int(strArray[i])
        self.name = strArray[i + 1]
        i += 2
        return i

    def InRnd(self):
        self.age = GetRandomNumber(1000)
        self.name = GetRandomName()
        pass

    def Write(self, ostream):
        ostream.write("It is Tree. Age: {}. Name: {}. Quotient of division: {}".format(self.age,
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

