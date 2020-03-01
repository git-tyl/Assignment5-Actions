import unittest
import task
from datetime import date


class TestCase(unittest.TestCase):

    # example test 1
    def test1(self):
        # example test 1
        expected = "Success"

        self.assertEqual(expected, task.firstrun())

    # example test 2
    def test2(self):
        # example test 2
        expected = "Failure"
        self.assertNotEqual(expected, task.firstrun())

    # test for getting a circle's area from its radius
    def test_circle(self):
        # get the area of a circle and also round the answer to 3 decimal places
        expected = round(task.get_area_of_circle(4.0), 3)
        # assert and check if they are equal
        self.assertEqual(50.265, expected)

    # test for getting first and last element in an array
    def test_array(self):

        # create a new array
        array = [1, 2, 3]

        # get the result of the array
        expected = task.get_first_and_last_elements(array)

        # assert and check if they are equal
        self.assertEqual(1, expected[0])
        self.assertEqual(3, expected[1])

    # test for days between dates
    def test_dates(self):
        # create a 2 different dates
        date1 = date(2014, 7, 2)
        date2 = date(2014, 7, 5)

        # get the result of the array
        expected = task.get_days_between_dates(date1, date2)

        # assert and check if the days are correct
        self.assertEqual(3, expected)


if __name__ == '__main__':
    unittest.main()
