import unittest
from utils import arrs

class TestArrs(unittest.TestCase):

    # Внутри пишем нужное количество методов (функций)
    def test_get(self):
        # Пишем нужное количество проверок
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([1, 2, 3], -2, "test"), "test")

    def test_slice(self):
        self.assertEqual(arrs.my_slice([], 1, 3), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], -4), [1, 2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], -2), [2, 3])







