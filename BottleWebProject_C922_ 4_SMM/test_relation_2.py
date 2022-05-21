import unittest

from relation_handler import Features, BinaryRelation

class TestRelationHandler2(unittest.TestCase):

    def testFeaturesCheck(self):
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

        
        for i in range(0, len(inputTests)):
            realResults = BinaryRelation(inputTests[i]).checkForFeatures()
            self.assertCountEqual(realResults, expectedResults[i])


    def testInversedRelation(self):
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

        for i in range(0, len(inputTests)):
            realResults = BinaryRelation(inputTests[i]).getInversedRelation()
            self.assertCountEqual(realResults, expectedResults[i])

