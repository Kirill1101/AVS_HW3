from plant import *
from enum import Enum
from rnd import *


class Month(Enum):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12


def GetMonth(n):
    if n == '1':
        return Month.JANUARY
    elif n == '2':
        return Month.FEBRUARY
    elif n == '3':
        return Month.MARCH
    elif n == '4':
        return Month.APRIL
    elif n == '5':
        return Month.MAY
    elif n == '6':
        return Month.JUNE
    elif n == '7':
        return Month.JULY
    elif n == '8':
        return Month.AUGUST
    elif n == '9':
        return Month.SEPTEMBER
    elif n == '10':
        return Month.OCTOBER
    elif n == '11':
        return Month.NOVEMBER
    elif n == '12':
        return Month.DECEMBER


class Shrub(Plant):
    def __init__(self):
        self.month = Month.JANUARY
        self.name = ""

    def ReadStrArray(self, strArray, i):
        # должно быт как минимум два непрочитанных значения в массиве
        if i >= len(strArray) - 1:
            return 0
        self.month = GetMonth(strArray[i])
        self.name = strArray[i + 1]
        i += 2
        return i

    def InRnd(self):
        self.month = GetMonth(str(GetRandomNumber(12)))
        self.name = GetRandomName()
        pass

    def Write(self, ostream):
        ostream.write("It is Shrub. Month: {}. Name: {}. Quotient of division: {}".format(self.month.name,
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
