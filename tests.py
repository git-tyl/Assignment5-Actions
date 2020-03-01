import unittest
import task


class TestCase(unittest.TestCase):

    # test for getting a circle's area from its radius
    def test_circle(self):
        # get the area of a circle and also round the answer to 3 decimal places
        expected = round(task.get_area_of_circle(4.0), 3)
        # assert and check if they are equal
        self.assertEqual(50.265, expected)


if __name__ == '__main__':
    unittest.main()
