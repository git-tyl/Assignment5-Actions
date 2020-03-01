import unittest
import task


class TestCase(unittest.TestCase):

    # example test 1
    def test1(self):
        #example test 1
        expected = "Success"
        self.assertEqual(expected, task.firstrun())

    # example test 2
    def test2(self):
        # example test 2
        expected = "Failure"
        self.assertNotEqual(expected, task.firstrun())

    # test for getting a circle's area from its radius
    def test_circle(self):
        # get the area of a cicle and also round the answer to 3 decimal places
        expected = round(task.get_area_of_circle(4.0), 3)
        #assert and check if they are equal
        self.assertEqual(50.265, expected)


if __name__ == '__main__':
    unittest.main()
