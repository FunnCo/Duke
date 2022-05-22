import unittest

from relation_handler import Features, BinaryRelation

class TestRelationHandler2(unittest.TestCase):

    # ¬ данном методе провер€етс€ корректность определени€ свойств бинарных отношений
    def testFeaturesCheck(self):
        # ¬ списки занос€тс€ тестовые случаи, и ожидаемые результаты
        inputTests = []
        expectedResults = []

        inputTests.append([
            [0, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ])
        expectedResults.append([
            Features.ANTI_TRANSITIVE,
            Features.ASYMMETRIC
        ])

        inputTests.append([
            [0, 0, 0, 1],
            [0, 0, 0, 1],
            [0, 0, 0, 1],
            [0, 0, 0, 1],
        ])
        expectedResults.append([
            Features.ANTI_TRANSITIVE
        ])

        inputTests.append([
            [0, 0, 1, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ])
        expectedResults.append([
            Features.ASYMMETRIC
        ])

        inputTests.append([
            [0, 0, 1, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ])
        expectedResults.append([
            Features.ASYMMETRIC
        ])

        inputTests.append([
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ])
        expectedResults.append([])

        # ÷икл дл€ последовательной проверки всех тестовых случаев
        for i in range(0, len(inputTests)):
            realResults = BinaryRelation(inputTests[i]).checkForFeatures()
            self.assertCountEqual(realResults, expectedResults[i])

    # ¬ данном методе провер€етс€ корректность нахождени€ обратного отношени€ к данному
    def testInversedRelation(self):
        # ¬ списки занос€тс€ тестовые случаи, и ожидаемые результаты
        inputTests = []
        expectedResults = []

        inputTests.append(
            [
                [0, 0],
                [1, 1],
            ]
        )
        expectedResults.append(
            [
                [0, 1],
                [0, 1],
            ]
        )


        inputTests.append(
            [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ]
        )
        expectedResults.append(
            [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ]
        )

        inputTests.append(
            [
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
            ]
        )
        expectedResults.append(
            [
                [0, 0, 0, 1],
                [0, 0, 1, 0],
                [0, 1, 0, 0],
                [1, 0, 0, 0]
            ]
        )

        inputTests.append(
            [
                [1, 1, 1, 1],
                [1, 0, 0, 0],
                [1, 0, 1, 0],
                [1, 0, 0, 1]
            ]
        )
        expectedResults.append(
            [
                [1, 1, 1, 1],
                [1, 0, 0, 0],
                [1, 0, 1, 0],
                [1, 0, 0, 1]
            ]
        )

        inputTests.append([
            [0, 0, 0, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0]    
        ])

        expectedResults.append(
            [
                [0, 0, 0, 1, 1],
                [0, 0, 1, 0, 0],
                [0, 1, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
            ]
        )

        # ÷икл дл€ последовательной проверки всех тестовых случаев
        for i in range(0, len(inputTests)):
            realResults = BinaryRelation(inputTests[i]).getInversedRelation()
            self.assertCountEqual(realResults, expectedResults[i])

