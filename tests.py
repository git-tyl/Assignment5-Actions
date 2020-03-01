import unittest
import task


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "Success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "Failure"
        self.assertNotEqual(expected, task.firstrun())

    # test for getting a circle's area from its radius
    def test_circle(self):
        expected = round(task.get_area_of_circle(4.0), 3)
        self.assertEqual(50.265, expected)


if __name__ == '__main__':
    unittest.main()
