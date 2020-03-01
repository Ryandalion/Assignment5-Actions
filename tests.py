import unittest
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
        self.assertEqual([1, 10], task_test.compute_first_last([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

if __name__ == '__main__':
    unittest.main()
