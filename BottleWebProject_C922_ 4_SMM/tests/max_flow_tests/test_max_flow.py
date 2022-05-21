import unittest
import max_flow

class MaxFlowTest(unittest.TestCase):

    def test_maxFlow_Correct(self):
        self.assertAlmostEqual(max_flow.solve_max_flow([[0, 4, 5, 0], [0, 0, 0, 5], [0, 3, 0, 4], [0, 0, 0, 0]], 0, 3), 9.0)
        self.assertAlmostEqual(max_flow.solve_max_flow([[0, 4, 3, 5, 0], [0, 0, 2, 4, 5], [0, 3, 0, 0, 4], [0, 0, 0, 5, 10], [0,0,0,0,0]], 0, 4), 12.0)
        self.assertAlmostEqual(max_flow.solve_max_flow([[0, 1, 0], [0, 0, 1], [0, 0, 0]], 0, 2), 1.0)
        self.assertAlmostEqual(max_flow.solve_max_flow([[0, 1000, 1000, 0], [0, 0, 1000, 0], [0, 0, 0, 0], [0, 0, 0, 0]], 0, 3), "Нет потока!")
        self.assertAlmostEqual(max_flow.solve_max_flow([[0, 1000000, 0, 1000000], [0, 0, 0, 1], [0, 1000000, 0, 1000000], [0, 0, 0, 0]], 0, 3), 1000001.0)
    
    def test_maxFlow_Incorrect(self):
        self.assertAlmostEqual(max_flow.solve_max_flow([[0, 4, 5, 0], [0, 0, 0, 5], [0, 3, 0, 4], [0, 0, 0, 0]], 0, 0), "Некорректный ввод! Источник и сток одинаковы!")
        self.assertAlmostEqual(max_flow.solve_max_flow([[0, 4, 3, 5, 0], [0, 0, 2, 4, 5], [0, 3, 0, 0, 4], [0, 0, 0, 5, 10], [0,0,0,0,0]], 4, 4), "Некорректный ввод! Источник и сток одинаковы!")
        self.assertAlmostEqual(max_flow.solve_max_flow([[0, 1, 0], [0, 0, 1], [0, 0, 0]], 2, 2), "Некорректный ввод! Источник и сток одинаковы!")
        self.assertAlmostEqual(max_flow.solve_max_flow([[0, 1000, 1000, 0], [0, 0, 1000, 0], [0, 0, 0, 0], [0, 0, 0, 0]], 3, 3), "Некорректный ввод! Источник и сток одинаковы!")
        self.assertAlmostEqual(max_flow.solve_max_flow([[0, 1000000, 0, 1000000], [0, 0, 0, 1], [0, 1000000, 0, 1000000], [0, 0, 0, 0]], 0, 0), "Некорректный ввод! Источник и сток одинаковы!")
