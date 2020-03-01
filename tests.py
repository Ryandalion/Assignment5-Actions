import unittest
from datetime import date
import task as task_test


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task_test.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task_test.firstrun())

    def test_area(self):
        result = task_test.compute_area(5)
        self.assertEqual(78.5, result)

    def test_first_last(self):
        self.assertEqual((1, 10), task_test.compute_first_last([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

    def test_days(self):
        date_1 = date(2020, 4, 20)
        date_2 = date(2020, 4, 25)
        self.assertEqual(5, task_test.compute_days(date_1, date_2))


if __name__ == '__main__':
    unittest.main()
