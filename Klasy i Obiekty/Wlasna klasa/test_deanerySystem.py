import unittest
from DeanerySystem import *


class Test_TestIncrementDecrement(unittest.TestCase):

    def testTermLater(self):
        term1 = Term(Day.MON, 10, 00)
        term2 = Term(Day.SAT, 9, 45)
        self.assertEqual(term1.earlierThan(term2), False)
        self.assertEqual(term1.laterThan(term2), True)
        self.assertEqual(term1.equals(term2), False)

    def testTermEarlier(self):
        term1 = Term(Day.TUE, 8, 45)
        term2 = Term(Day.TUE, 9, 45)
        self.assertEqual(term1.earlierThan(term2), True)
        self.assertEqual(term1.laterThan(term2), False)
        self.assertEqual(term1.equals(term2), False)

    def testTermEqual(self):
        term1 = Term(Day.TUE, 9, 45)
        term2 = Term(Day.TUE, 9, 45)
        self.assertEqual(term1.earlierThan(term2), False)
        self.assertEqual(term1.laterThan(term2), False)
        self.assertEqual(term1.equals(term2), True)

    def testPrint(self):
        term = Term(Day.TUE, 9, 45)
        self.assertEqual(term.__str__(), "Wtorek 9:45 [90]")

    def setUp(self):
        self.term1 = Term(Day.TUE, 9, 45)
        self.term2 = Term(Day.WED, 10, 15)

    def test_difference(self):
        diff = self.term1.difference(self.term2)
        self.assertIsInstance(diff, Diff)
        self.assertEqual(diff.seconds, 88_200)
        self.assertEqual(diff.minutes, 1_470)
        self.assertEqual(diff.hours, 24) # wartość zaokrąglona w dół
        self.assertEqual(diff.days, 1)

if __name__ == '__main__':
    unittest.main()