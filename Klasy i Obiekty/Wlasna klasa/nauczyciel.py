from __future__ import annotations

import math
from abc import ABC, abstractmethod

from DeanerySystem import Term, Day, BasicTerm
from basicTimetable import BasicTimetable
from bbreak import Break
from lesson import Lesson
from timetable1 import Timetable1
from timetable2 import Timetable2


class Nauczyciel(ABC):
    @abstractmethod
    def show_day_timetable(self, day: Day, timetable: Timetable2) -> None:
        pass


class Kowalski(Nauczyciel):
    teacherName = "Kowalski"

    def show_day_timetable(self, day: Day, timetable: Timetable2) -> None:
        print(self.teacherName + "\n\n" + day.getName())
        dayLessonList = timetable.getDayLesson(day)
        startMinutesTime = 1700  # 24*60
        stopMinutesTime = 0
        workMinutesTime = 0
        for lesson in dayLessonList:
            if lesson.teacherName == self.teacherName:
                print(" {} '{}'".format(lesson.term.printTimeRange(), lesson.name))
                lessonMinuteTime = lesson.term.hour * 60 + lesson.term.minute
                if lessonMinuteTime < startMinutesTime:
                    startMinutesTime = lessonMinuteTime
                if lessonMinuteTime + lesson.term.duration > stopMinutesTime:
                    stopMinutesTime = lessonMinuteTime +lesson.term.duration
                workMinutesTime += lesson.term.duration
        restHours = math.floor((stopMinutesTime - startMinutesTime - workMinutesTime) / 60)
        restMinutes = stopMinutesTime - startMinutesTime - workMinutesTime - restHours * 60
        print(" Czas bezczynności: {}:{}".format(str(restHours), str(restMinutes).zfill(2)))


# class Nowak(Nauczyciel):
#     teacherName = "Nowak"
#
#     def show_day_timetable(self, day: Day, timetable: Timetable2) -> None:
#         print(self.teacherName + "\n\n" + day.getName())
#         dayLessonList = timetable.getDayLesson(day)
#         startMinutesTime = 1700  # 24*60
#         stopMinutesTime = 0
#         workMinutesTime = 0
#         for lesson in dayLessonList:
#             if lesson.teacherName == self.teacherName:
#                 print(" {} '{}'".format(lesson.term.printTimeRange(), lesson.name))
#                 lessonMinuteTime = lesson.term.hour * 60 + lesson.term.minute
#                 if lessonMinuteTime < startMinutesTime:
#                     startMinutesTime = lessonMinuteTime
#                 if lessonMinuteTime + lesson.term.duration > stopMinutesTime:
#                     stopMinutesTime = lessonMinuteTime +lesson.term.duration
#                 workMinutesTime += lesson.term.duration
#         restHours = math.floor((stopMinutesTime - startMinutesTime - workMinutesTime) / 60)
#         restMinutes = stopMinutesTime - startMinutesTime - workMinutesTime - restHours * 60
#         print(" Czas bezczynności: {}:{}".format(str(restHours), str(restMinutes).zfill(2)))


if __name__ == '__main__':
    breaks = [Break(BasicTerm(9, 30, 5)), Break(BasicTerm(11, 5, 10)), Break(BasicTerm(12, 45, 15)),
              Break(BasicTerm(14, 30, 5)), Break(BasicTerm(16, 5, 5)), Break(BasicTerm(17, 45, 5)),
              Break(BasicTerm(19, 20, 5))]
    Timetable2.skipBreaks = False
    timetable = Timetable2(breaks)
    lesson1 = Lesson(timetable, Term(Day.MON, 8, 00), "Niemiecki", "Kowalski", 2)
    lesson = Lesson(timetable, Term(Day.MON, 13, 00), "Polski", "Kowalski", 2)
    lesson2 = Lesson(timetable, Term(Day.MON, 9, 35), "Angielski", "Nowak", 2)
    lesson3 = Lesson(timetable, Term(Day.MON, 14, 35), "Angielski2", "Nowak", 2)
    lesson4 = Lesson(timetable, Term(Day.MON, 17, 50), "Polski2", "Kowalski", 2)

    kowalski = Kowalski()
    kowalski.show_day_timetable(Day.MON, timetable)
