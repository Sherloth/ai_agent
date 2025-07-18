import unittest

class CalculatorTests(unittest.TestCase):

    def test_add(self):
        self.assertEqual(2 + 2, 4)

    def test_subtract(self):
        self.assertEqual(5 - 3, 2)

    def test_multiply(self):
        self.assertEqual(3 * 4, 12)

    def test_divide(self):
        self.assertEqual(10 / 2, 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            _ = 1 / 0

    def test_string_concat(self):
        self.assertEqual("Hello " + "World", "Hello World")

    def test_list_membership(self):
        self.assertIn(5, [3, 4, 5])

    def test_dict_access(self):
        self.assertEqual({"a": 1}["a"], 1)

    def test_boolean_logic(self):
        self.assertTrue(True and not False)

if __name__ == "__main__":
    unittest.main()
