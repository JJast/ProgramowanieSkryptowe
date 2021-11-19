import unittest
from DeanerySystem import *
from action import Action
from bbreak import Break
from lesson import Lesson
from timetable2 import Timetable2


class Test_Timetable2(unittest.TestCase):

    breaks = [Break(BasicTerm(9, 30, 5)), Break(BasicTerm(11, 5, 10)), Break(BasicTerm(12, 45, 15)),
              Break(BasicTerm(14, 30, 5)), Break(BasicTerm(16, 5, 5)), Break(BasicTerm(17, 45, 5)), Break(BasicTerm(19, 15, 5))]


    def testValueError(self):
        #Timetable2.skipBreaks = False
        timetable2 = Timetable2(self.breaks)
        lesson = Lesson(timetable2, Term(Day.MON, 8, 00), "Polski", "Krzysztof", 2)
        with self.assertRaises(ValueError):
            timetable2.put(lesson)
        self.assertEqual(len(timetable2.lessonList), 1)


    def testBreaks(self):
        #Timetable2.skipBreaks = False
        timetable2 = Timetable2(self.breaks)
        lesson = Lesson(timetable2, Term(Day.MON, 8, 00), "Polski", "Krzysztof", 2)
        lesson2 = Lesson(timetable2, Term(Day.MON, 9, 35), "Angielski", "Miroslaw", 2)

        self.assertEqual(len(timetable2.lessonList), 2)

        ######################
        #   Standard tests   #
        ######################
    def testParse(self):
        #Timetable2.skipBreaks = True
        timetable = Timetable2(self.breaks)
        actions = timetable.parse(["d-", "d+", "t-", "t+"])
        self.assertEqual(actions, [Action.DAY_EARLIER, Action.DAY_LATER, Action.TIME_EARLIER, Action.TIME_LATER])


    def testPut(self):
        Timetable2.skipBreaks = False
        timetable = Timetable2(self.breaks)
        lesson = Lesson(timetable, Term(Day.WED, 14, 35), "Polski", "Krzysztof", 2)
        lesson1 = Lesson(timetable, Term(Day.SAT, 9, 35), "Angielski", "Miroslaw", 2)
        """with self.assertRaises(ValueError):
            timetable.put(lesson)
            timetable.put(lesson1)"""
        self.assertEqual(len(timetable.lessonList),2)


    def testPerform1(self):
        Timetable2.skipBreaks = True
        timetable = Timetable2(self.breaks)
        lesson = Lesson(timetable, Term(Day.WED, 14, 00), "Polski", "Krzysztof", 2)
        lesson1 = Lesson(timetable, Term(Day.SAT, 9, 30), "Angielski", "Miroslaw", 2)
        actions = timetable.parse(["d-", "d+", "t-", "t+"])
        timetable.perform(actions)
        self.assertEqual(lesson.term.termday__, Day.TUE)
        self.assertEqual(lesson.term.hour, 12)
        self.assertEqual(lesson.term.minute, 30)

        self.assertEqual(lesson1.term.termday__, Day.SUN)
        self.assertEqual(lesson1.term.hour, 11)
        self.assertEqual(lesson1.term.minute, 0)


    def testPerform2(self):
        Timetable2.skipBreaks = True
        timetable = Timetable2(self.breaks)
        lesson = Lesson(timetable, Term(Day.WED, 14, 00), "Polski", "Krzysztof", 2)
        lesson1 = Lesson(timetable, Term(Day.THU, 9, 30), "Angielski", "Miroslaw", 2)
        lesson3 = Lesson(timetable, Term(Day.SAT, 14, 00), "Francuski", "Miroslaw", 2)
        lesson4 = Lesson(timetable, Term(Day.SUN, 18, 30), "Wloski", "Miroslaw", 2)
        actions = timetable.parse(["d-", "d+", "t-", "t+"])
        timetable.perform(actions)

        self.assertEqual(lesson.term.termday__, Day.TUE)
        self.assertEqual(lesson.term.hour, 14)
        self.assertEqual(lesson.term.minute, 00)

        self.assertEqual(lesson1.term.termday__, Day.THU)
        self.assertEqual(lesson1.term.hour, 9)
        self.assertEqual(lesson1.term.minute, 30)

        self.assertEqual(lesson3.term.termday__, Day.SAT)
        self.assertEqual(lesson3.term.hour, 12)
        self.assertEqual(lesson3.term.minute, 30)

        self.assertEqual(lesson4.term.termday__, Day.SUN)
        self.assertEqual(lesson4.term.hour, 18)
        self.assertEqual(lesson4.term.minute, 30)


    def testShiftRight(self):
        Timetable2.skipBreaks = True
        timetable = Timetable2(self.breaks)
        lesson = Lesson(timetable, Term(Day.WED, 14, 35), "Polski", "Krzysztof", 2)
        lesson1 = Lesson(timetable, Term(Day.THU, 9, 35), "Angielski", "Miroslaw", 2)

        lesson >> 1
        self.assertEqual(lesson.term.termday__, Day.WED)
        self.assertEqual(lesson.term.hour, 16)
        self.assertEqual(lesson.term.minute, 5)
        lesson >> 3
        self.assertEqual(lesson.term.termday__, Day.THU)
        self.assertEqual(lesson.term.hour, 8)
        self.assertEqual(lesson.term.minute, 0)
        lesson >> 1
        self.assertEqual(lesson.term.termday__, Day.THU)
        self.assertEqual(lesson.term.hour, 8)
        self.assertEqual(lesson.term.minute, 0)

    def testLeftShift(self):
        Timetable2.skipBreaks = True
        timetable = Timetable2(self.breaks)
        lesson = Lesson(timetable, Term(Day.WED, 14, 35), "Polski", "Krzysztof", 2)
        lesson1 = Lesson(timetable, Term(Day.THU, 9, 35), "Angielski", "Miroslaw", 2)

        lesson1 << 1
        self.assertEqual(lesson1.term.termday__, Day.THU)
        self.assertEqual(lesson1.term.hour, 8)
        self.assertEqual(lesson1.term.minute, 5)
        lesson1 << 2
        self.assertEqual(lesson1.term.termday__, Day.WED)
        self.assertEqual(lesson1.term.hour, 15)
        self.assertEqual(lesson1.term.minute, 30)

if __name__ == '__main__':
    unittest.main()
