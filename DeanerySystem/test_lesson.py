import unittest
from term import Term
from day import Day
from lesson import Lesson, NeitherFullNorPartError


class Test_TestIncrementDecrement(unittest.TestCase):

    def testLessonEarlierDay(self):
        lesson = Lesson(Term(Day.MON, 9, 35), "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson2 = Lesson(Term(Day.TUE, 12, 35), "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson3 = Lesson(Term(Day.SAT, 17, 10), "Programowanie skryptowe", "Stanisław Polak", 2)

        lesson.earlierDay()
        lesson2.earlierDay()
        lesson3.earlierDay()

        self.assertEqual(lesson.term._Term__termday, Day.MON)
        self.assertEqual(lesson2.term._Term__termday, Day.MON)
        self.assertEqual(lesson3.term._Term__termday, Day.FRI)
    
    def testLessonLaterDay(self):
        lesson = Lesson(Term(Day.MON, 9, 35), "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson2 = Lesson(Term(Day.THU, 8, 15), "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson3 = Lesson(Term(Day.SAT, 15, 35), "Programowanie skryptowe", "Stanisław Polak", 2)

        lesson.laterDay()
        lesson2.laterDay()
        lesson3.laterDay()

        self.assertEqual(lesson.term._Term__termday, Day.TUE)
        self.assertEqual(lesson2.term._Term__termday, Day.FRI)
        self.assertEqual(lesson3.term._Term__termday, Day.SUN)

    def testLessonEarliertime(self):
        lesson = Lesson(Term(Day.MON, 9, 35), "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson2 = Lesson(Term(Day.THU, 8, 0), "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson3 = Lesson(Term(Day.FRI, 18, 0), "Programowanie skryptowe", "Stanisław Polak", 2)

        lesson.earlierTime()
        lesson2.earlierTime()
        lesson3.earlierTime()

        self.assertEqual(lesson.term.hour, 8)
        self.assertEqual(lesson.term.minute, 5)
        self.assertEqual(lesson2.term.hour, 8)
        self.assertEqual(lesson2.term.minute, 0)
        self.assertEqual(lesson3.term.hour, 18)
        self.assertEqual(lesson3.term.minute, 0)

    def testLessonLatertime(self):
        lesson = Lesson(Term(Day.MON, 8, 35), "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson2 = Lesson(Term(Day.THU, 17, 45), "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson3 = Lesson(Term(Day.SAT, 15, 30), "Programowanie skryptowe", "Stanisław Polak", 2)

        lesson.laterTime()
        lesson2.laterTime()
        lesson3.laterTime()

        self.assertEqual(lesson.term.hour, 10)
        self.assertEqual(lesson.term.minute, 5)
        self.assertEqual(lesson2.term.hour, 19)
        self.assertEqual(lesson2.term.minute, 15)
        self.assertEqual(lesson3.term.hour, 17)
        self.assertEqual(lesson3.term.minute, 0)


if __name__ == '__main__':
    unittest.main()