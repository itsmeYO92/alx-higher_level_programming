import unittest


from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):

    def test_init(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10, 1, 1)
        r3 = Rectangle(10, 2, 0, 0, 33)
        self.assertEqual(r1.id, r2.id - 1)
        self.assertEqual(r3.id, 33)

    def test_type_validation(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, "str")

        with self.assertRaises(TypeError):
            r1 = Rectangle("10", "str")

        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 10.4)

        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 10, "str", 9)

        with self.assertRaises(ValueError):
            r1 = Rectangle(10, -2)
