# from unittest import TestCase
import unittest
from rain_terrace import find_all_terraces, gather_water

class TestFindAllTerraces(unittest.TestCase):
    """Tests Find All Terraces from rain_terrace.py"""

    def setUp(self):
            pass

    def tearDown(self):
        pass

    def test_that_function_exists(self):
        self.assertIsNotNone(find_all_terraces([]))

    def test_function_accepts_list(self):
        self.assertIsNotNone(find_all_terraces([2, 1, 2]))

    def test_function_returns_number(self):
        self.assertIsInstance(find_all_terraces([]), int)

    def test_function_does_not_return_str(self):
        self.assertNotIsInstance(find_all_terraces([]), str)

class TestGatherWater(unittest.TestCase):
    """Tests Gather Water function from rain_terrace.py"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_that_functions_exist(self):
        empty_rain_terrace = { 'total_water': 0, 'left_idx': 0, 'right_idx': 0, 'left_wall': 0, 'right_wall': 0, 'bottom_vals': [], }
        # self.assertIsNotNone(find_all_terraces([]))
        self.assertIsNotNone(gather_water(empty_rain_terrace))

    # def test_function_accepts_list(self):
    #     self.assertIsNotNone(find_all_terraces([2, 1, 2]))

    # def test_function_returns_number(self):
    #     self.assertIsInstance(find_all_terraces([]), int)

    # def test_function_does_not_return_str(self):
    #     self.assertNotIsInstance(find_all_terraces([]), str)

    



if __name__ == '__main__':
    unittest.main()
