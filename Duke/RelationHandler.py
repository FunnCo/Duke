from enum import Enum


class Features(Enum):
    REFLECTIVE = 1
    SYMMETRIC = 2
    TRANSITIVE = 3
    ASYMMETRIC = 4
    ANTI_TRANSITIVE = 5


class BinaryRelation:

    graph = None

    def __init__(self, graph):
        self.graph = graph

    def checkTransitive(self):
        isTransitive = False

        # Проверка на транзитивность
        for rowIndex in range(0, len(self.graph)):
            for columnIndex in range(0, len(self.graph)):
                currentValue = self.graph[rowIndex][columnIndex]
                if(currentValue == 1 and rowIndex != columnIndex):
                    for secondIndex in range(0, len(self.graph)):
                        secondValue = self.graph[columnIndex][secondIndex]
                        if(secondValue == 1 and secondIndex != columnIndex):
                            if(self.graph[rowIndex][secondIndex] == 1):
                                isTransitive = True
                            elif(isTransitive):
                                return False

        return isTransitive

    def checkAntiTransitive(self):
        isAntiTransitive = False

        # Проверка на антитранзитивность
        for rowIndex in range(0, len(self.graph)):
            for columnIndex in range(0, len(self.graph)):
                currentValue = self.graph[rowIndex][columnIndex]
                if(currentValue == 0):
                    for secondIndex in range(0, len(self.graph)):
                        secondValue = self.graph[columnIndex][secondIndex]
                        if(secondValue == 0 and secondIndex != columnIndex):
                            if(self.graph[rowIndex][secondIndex] == 0):
                                isAntiTransitive = True
                            elif(isAntiTransitive):
                                return False
        return isAntiTransitive

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

    def getAdditionalRelation(self):
        additionalRelation = []

        for rowIndex in range(0, len(self.graph)):
            additionalRelation.append([])
            for columnIndex in range(0, len(self.graph)):
                additionalRelation[rowIndex].append(
                    abs(self.graph[rowIndex][columnIndex]-1))

        return additionalRelation

    def getInversedRelation(self):
        inversedRelation = []

        for rowIndex in range(0, len(self.graph)):
            inversedRelation.append([])
            for columnIndex in range(0, len(self.graph)):
                inversedRelation[rowIndex].append(
                    self.graph[columnIndex][rowIndex])

        return inversedRelation
