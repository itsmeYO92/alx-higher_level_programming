import unittest


from models.base import Base


class TestBase(unittest.TestCase):

    def test_init(self):
        a = Base()
        b = Base(4)
        c = Base()
        self.assertEqual(a.id, c.id - 1)
        self.assertEqual(c.id, a.id + 1)
        self.assertEqual(b.id, 4)

