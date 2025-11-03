from _pytest import unittest


def add(a,b):
    return a+b


class TestAddNumbers(unittest.Testcase):
    def test_positive_numbers(self):
        result=add(2,3)
        self.assertEqual(result,5)

    def test_negative_Numbers(self):
        self.assertEqual(add(1,2), 3)
