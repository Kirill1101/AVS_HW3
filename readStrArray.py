from extender import *
from rnd import *


def InRnd(container, size):
    for i in range(size):
        key = GetRandomNumber(3)
        if key == 1:  # признак дерева
            plant = Tree()
            plant.InRnd()
        elif key == 2:  # признак кустарника
            plant = Shrub()
            plant.InRnd()
        elif key == 3:  # признак цветка
            plant = Flower()
            plant.InRnd()
        container.store.append(plant)


def ReadStrArray(container, strArray):
    arrayLen = len(strArray)
    i = 0  # Индекс, задающий текущую строку в массиве
    figNum = 0
    while i < arrayLen:
        str = strArray[i]
        key = int(str)  # преобразование в целое
        if key == 1:  # признак дерева
            i += 1
            plant = Tree()
            i = plant.ReadStrArray(strArray, i)  # чтение прямоугольника с возвратом позиции за ним
        elif key == 2:  # признак кустарника
            i += 1
            plant = Shrub()
            i = plant.ReadStrArray(strArray, i)  # чтение треугольника с возвратом позиции за ним
        elif key == 3:  # признак цветка
            i += 1
            plant = Flower()
            i = plant.ReadStrArray(strArray, i)  # чтение треугольника с возвратом позиции за ним
        else:
            # что-то пошло не так. Должен быть известный признак
            # Возврат количества прочитанных фигур
            return figNum
        # Количество пробелами фигур увеличивается на 1
        if i == 0:
            return figNum
        figNum += 1
        container.store.append(plant)
