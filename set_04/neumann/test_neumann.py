import unittest
from set_04.neumann.neumann import neumann, neumann_recursive


class TestNeumann(unittest.TestCase):
    def test_n0(self):
        result = neumann_recursive(0)
        self.assertEqual(result, "{}")

    def test_n1(self):
        result = neumann_recursive(1)
        self.assertEqual(result, "{{}}")

    def test_n2(self):
        result = neumann_recursive(2)
        self.assertEqual(result, "{{},{{}}}")

    def test_n3(self):
        result = neumann_recursive(3)
        self.assertEqual(result, "{{},{{}},{{},{{}}}}")


if __name__ == "__main__":
    unittest.main()
