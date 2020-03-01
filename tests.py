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
        result = task_test.compute_area(5);
        self.assertEqual(78.5, result);


if __name__ == '__main__':
    unittest.main()