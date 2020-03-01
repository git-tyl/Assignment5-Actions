import unittest
import task


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "Success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "Failure"
        self.assertNotEqual(expected, task.firstrun())


if __name__ == '__main__':
    unittest.main()
