import unittest

from relation_handler import Features, BinaryRelation

class TestRelationHandler1(unittest.TestCase):

    # В данном методе проверяется корректность определения свойств бинарных отношений
    def testFeaturesCheck(self):

        # В списки заносятся тестовые случаи, и ожидаемые результаты
        inputTests = []
        expectedResults = []

        inputTests.append([
            [1, 0],
            [1, 1]
        ])
        expectedResults.append([Features.REFLECTIVE])

        inputTests.append([
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]
        ])
        expectedResults.append([
            Features.REFLECTIVE,
            Features.SYMMETRIC,
            Features.TRANSITIVE
        ])
        
        inputTests.append([
            [1, 0, 0, 1],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ])
        expectedResults.append([
            Features.REFLECTIVE,
        ])

        inputTests.append([
            [1, 0, 1, 1],
            [0, 1, 0, 0],
            [0, 0, 1, 1],
            [0, 0, 0, 1]
        ])
        expectedResults.append([
            Features.REFLECTIVE,
            Features.TRANSITIVE
        ])

        inputTests.append([
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [1, 1, 1, 0, 0],
        ])
        expectedResults.append([
            Features.TRANSITIVE,
            Features.ASYMMETRIC
        ])

        inputTests.append([
            [1, 0, 0, 1],
            [0, 0, 1, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 1],
        ])
        expectedResults.append([])

        # Цикл для последовательной проверки всех тестовых случаев
        for i in range(0, len(inputTests)):
            realResults = BinaryRelation(inputTests[i]).checkForFeatures()
            self.assertCountEqual(realResults, expectedResults[i])
            

    # В данном методе проверяется корректность расчета дополнительного бинарного отнощения к данному
    def testAdditionalRelation(self):
        inputTests = []
        expextedResults = []

        # В списки заносятся тестовые случаи, и ожидаемые результаты
        inputTests.append(
            [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ]
        )
        expextedResults.append(
            [
                [1, 1, 1, 1],
                [1, 1, 1, 1],
                [1, 1, 1, 1],
                [1, 1, 1, 1]
            ]
        )
        inputTests.append(
            [
                [1, 1, 1, 1],
                [1, 1, 1, 1],
                [1, 1, 1, 1],
                [1, 1, 1, 1]
            ]
        )
        expextedResults.append(
            [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ]
        )

        inputTests.append(
            [
                [1, 0, 1, 0],
                [1, 0, 1, 0],
                [1, 0, 1, 0],
                [1, 0, 1, 0]
            ]
        )
        expextedResults.append(
            [
                [0, 1, 0, 1],
                [0, 1, 0, 1],
                [0, 1, 0, 1],
                [0, 1, 0, 1]
            ]
        )

        inputTests.append(
            [
                [1, 0, 1, 0],
                [0, 1, 0, 1],
                [1, 0, 1, 0],
                [0, 1, 0, 1]
            ]
        )
        expextedResults.append(
            [
                [0, 1, 0, 1],
                [1, 0, 1, 0],
                [0, 1, 0, 1],
                [1, 0, 1, 0]
            ]
        )

        inputTests.append(
            [
                [1, 0],
                [0, 1]
            ]
        )
        expextedResults.append(
            [
                [0, 1],
                [1, 0],
            ]
        )

        # Цикл для последовательной проверки всех тестовых случаев
        for i in range(0, len(inputTests)):
            realResults = BinaryRelation(inputTests[i]).getAdditionalRelation()
            self.assertCountEqual(realResults, expextedResults[i])


