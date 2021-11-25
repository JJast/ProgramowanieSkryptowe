import unittest

from dekorator import Operacje


class Test_TestDekorator(unittest.TestCase):

    def testSum(self):
        op = Operacje()
        self.assertEqual(op.suma(1, 2, 3), 4)
        self.assertEqual(op.suma(1, 2), 5)
        self.assertRaises(TypeError, op.suma)

    def testDifference(self):
        op = Operacje()
        self.assertEqual(op.roznica(1, 2), 4)
        self.assertEqual(op.roznica(1), 5)
        self.assertEqual(op.roznica(), 6)
        self.assertRaises(TypeError, op.suma)

    def changeSumOperatorArgument(self):
        op = Operacje()
        op['suma'] = [1, 2]
        self.assertEqual(op.suma(1, 2, 3), 1)
        self.assertEqual(op.suma(1, 2), 2)
        self.assertRaises(TypeError, op.suma)

    def changeDifferenceOperatorArgument(self):
        op = Operacje()
        op['roznica'] = [1, 2, 3]
        self.assertEqual(op.roznica(1, 2), 1)
        self.assertEqual(op.roznica(1), 2)
        self.assertEqual(op.roznica(), 3)
        self.assertRaises(TypeError, op.suma)


if __name__ == '__main__':
    unittest.main()