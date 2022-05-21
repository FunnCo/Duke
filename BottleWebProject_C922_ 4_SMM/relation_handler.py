from enum import Enum


# Перечисление для пердставления всех свойств графа
class Features(str, Enum):
    REFLECTIVE = "рефлективность"
    SYMMETRIC = "симметричность"
    TRANSITIVE = "транзитивность"
    ASYMMETRIC = "асимметричность"
    ANTI_TRANSITIVE = "антитранзитивность"
    
# Класс для работы с бинарными отношениями
class BinaryRelation:

    # Матрица смежности графа
    graph = None

    # Конструктор класса
    def __init__(self, graph):
        self.graph = graph

    # Метод проверки графа на транзитивность
    def checkTransitive(self):
        isTransitive = False

        # Внешний цикл, перебирающий все строки (i индекс,
        # если смотреть на формальное представление транзитивности)
        for rowIndex in range(0, len(self.graph)):
            
            # Цикл, перебирающий все значения в строке (l элемент)
            # если смотреть на формальное представление транзитивности)
            for columnIndex in range(0, len(self.graph)):
                currentValue = self.graph[rowIndex][columnIndex]

                # Пропуск петель в графе
                if(currentValue == 1 and rowIndex != columnIndex):

                    # Цикл, перебирающий j значения
                    for secondIndex in range(0, len(self.graph)):
                        secondValue = self.graph[columnIndex][secondIndex]
                        if(secondValue == 1 and secondIndex != columnIndex):
                            if(self.graph[rowIndex][secondIndex] == 1):
                                isTransitive = True
                            elif(isTransitive):
                                return False

        return isTransitive
    
    # Метод проверки графа на транзитивность
    def checkAntiTransitive(self):
        isAntiTransitive = False
        
        # Цикл, перебирающий все значения в строке (j элемент)
        # если смотреть на формальное представление антитранзитивности)
        for rowIndex in range(0, len(self.graph)):

            # Цикл, перебирающий все значения в строке (j элемент)
            # если смотреть на формальное представление антитранзитивности)
            for columnIndex in range(0, len(self.graph)):
                currentValue = self.graph[rowIndex][columnIndex]
                if(currentValue == 0):

                    # Цикл, перебирающий k значения
                    for secondIndex in range(0, len(self.graph)):
                        secondValue = self.graph[columnIndex][secondIndex]
                        if(secondValue == 0 and secondIndex != columnIndex):
                            if(self.graph[rowIndex][secondIndex] == 0):
                                isAntiTransitive = True
                            elif(isAntiTransitive):
                                return False
        return isAntiTransitive

    # Метод получения списка свойств из представленных в представлении Features
    # которыми обладает данный граф 
    def checkForFeatures(self):
        result = []

        # Проверка на рефлексивность
        isReflective = True
        for row in range(0, len(self.graph)):
            if(self.graph[row][row] == 0):
                isReflective = False
                break

        if(isReflective):
            result.append(Features.REFLECTIVE)

        # Проверка на симметрию и ассиметрию
        isSymmetric = True
        isAsymmetric = True
        for rowIndex in range(0, len(self.graph)):
            for columnIndex in range(0, rowIndex + 1):
                currentValue = self.graph[rowIndex][columnIndex]
                mirroredValue = self.graph[columnIndex][rowIndex]
                if(currentValue + mirroredValue != 0):
                    if(currentValue + mirroredValue == 2):
                        isAsymmetric = False
                    else:
                        isSymmetric = False

        if(isSymmetric):
            result.append(Features.SYMMETRIC)
        elif(isAsymmetric):
            result.append(Features.ASYMMETRIC)

        if(self.checkTransitive() == True):
            result.append(Features.TRANSITIVE)
        elif(self.checkAntiTransitive() == True):
            result.append(Features.ANTI_TRANSITIVE)

        return result

    # Метод получения дополнительного отношения к представляемому этим классом. 
    # Метод возвращает матрицу смежности необходимого отношения
    def getAdditionalRelation(self):
        additionalRelation = []

        for rowIndex in range(0, len(self.graph)):
            additionalRelation.append([])
            for columnIndex in range(0, len(self.graph)):
                additionalRelation[rowIndex].append(
                    abs(self.graph[rowIndex][columnIndex]-1))

        return additionalRelation

    # Метод получения обратного отношения к представляемому этим классом. 
    # Метод возвращает матрицу смежности необходимого отношения
    def getInversedRelation(self):
        inversedRelation = []

        for rowIndex in range(0, len(self.graph)):
            inversedRelation.append([])
            for columnIndex in range(0, len(self.graph)):
                inversedRelation[rowIndex].append(
                    self.graph[columnIndex][rowIndex])

        return inversedRelation
