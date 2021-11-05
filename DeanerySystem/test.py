import unittest
from day import Day
from term import Term


class Test_TestDay(unittest.TestCase):

    def test_nth(self):
        self.assertEqual(Day.nthDayFrom(1, Day.SAT), Day.SUN)
        self.assertEqual(Day.nthDayFrom(2, Day.SAT), Day.MON)
        self.assertEqual(Day.nthDayFrom(-1, Day.TUE), Day.MON)
        self.assertEqual(Day.nthDayFrom(-2, Day.TUE), Day.SUN)

    def test_difference(self):
        self.assertEqual(Day.MON.difference(Day.TUE), 1)
        self.assertEqual(Day.MON.difference(Day.SUN), -1)
        self.assertEqual(Day.SUN.difference(Day.MON), 1)
        self.assertEqual(Day.SUN.difference(Day.SAT), -1)

    def test_term(self):
        term1 = Term(Day.TUE, 9, 45)
        print(term1)
        term2 = Term(Day.WED, 10, 15)
        print(term2)   
        self.assertEqual(term1.earlierThan(term2), True)
        self.assertEqual(term1.laterThan(term2), False)
        self.assertEqual(term1.equals(term2), False)



if __name__ == '__main__':
    unittest.main()