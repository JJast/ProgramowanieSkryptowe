import unittest
from DeanerySystem import *
from lesson import Lesson, NeitherFullNorPartError


class Test_TestIncrementDecrement(unittest.TestCase):

    def testLessonPrint(self):
        lesson = Lesson(Term(Day.TUE, 9, 35), "Programowanie skryptowe", "Stanisław Polak", 2)
        lessonStr = """Programowanie skryptowe (Wtorek 9:35-11:05)
                  Drugi rok studiów stacjonarnych
                  Prowadzący: Stanisław Polak
"""
        self.assertEqual(lesson.__str__(), lessonStr)

    def testFulltime(self):
        lesson = Lesson(Term(Day.MON, 8, 00), "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson2 = Lesson(Term(Day.SUN, 17, 35), "Programowanie skryptowe", "Stanisław Polak", 2)
        self.assertEqual(lesson.full_time, True)
        self.assertEqual(lesson2.full_time, False)
        self.assertRaises(NeitherFullNorPartError, Lesson, Term(Day.TUE, 20, 35), "Programowanie skryptowe", "Stanisław Polak", 2)

        lesson = Lesson(Term(Day.MON, 10, 00), "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson2 = Lesson(Term(Day.SUN, 17, 35), "Programowanie skryptowe", "Stanisław Polak", 2)
        self.assertEqual(lesson.full_time, True)
        self.assertEqual(lesson2.full_time, False)
        self.assertRaises(NeitherFullNorPartError, Lesson, Term(Day.FRI, 20, 35), "Programowanie skryptowe", "Stanisław Polak", 2)

    def testLessonEarlierDay(self):
        lesson = Lesson(Term(Day.MON, 9, 35), "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson2 = Lesson(Term(Day.TUE, 12, 35), "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson3 = Lesson(Term(Day.SAT, 17, 35), "Programowanie skryptowe", "Stanisław Polak", 2)

        lesson.earlierDay()
        lesson2.earlierDay()
        lesson3.earlierDay()

        self.assertEqual(lesson.term.termday__, Day.MON)
        self.assertEqual(lesson2.term.termday__, Day.MON)
        self.assertEqual(lesson3.term.termday__, Day.FRI)

    def testLessonLaterDay(self):
        lesson = Lesson(Term(Day.MON, 9, 35), "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson2 = Lesson(Term(Day.THU, 12, 35), "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson3 = Lesson(Term(Day.SAT, 15, 35), "Programowanie skryptowe", "Stanisław Polak", 2)

        lesson.laterDay()
        lesson2.laterDay()
        lesson3.laterDay()

        self.assertEqual(lesson.term.termday__, Day.TUE)
        self.assertEqual(lesson2.term.termday__, Day.THU)
        self.assertEqual(lesson3.term.termday__, Day.SUN)

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
        lesson2 = Lesson(Term(Day.THU, 18, 35), "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson3 = Lesson(Term(Day.SAT, 15, 30), "Programowanie skryptowe", "Stanisław Polak", 2)

        lesson.laterTime()
        lesson2.laterTime()
        lesson3.laterTime()

        self.assertEqual(lesson.term.hour, 10)
        self.assertEqual(lesson.term.minute, 5)
        self.assertEqual(lesson2.term.hour, 18)
        self.assertEqual(lesson2.term.minute, 35)
        self.assertEqual(lesson3.term.hour, 17)
        self.assertEqual(lesson3.term.minute, 0)


if __name__ == '__main__':
    unittest.main()
