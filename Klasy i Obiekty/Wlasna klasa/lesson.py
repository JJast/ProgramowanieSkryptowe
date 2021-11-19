import copy

from DeanerySystem import *
import math
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from timetable1 import Timetable1


class Lesson:
    def __init__(self, timetable, term: Term, name: str, teacherName: str, year: int = 1):
        from timetable1 import Timetable1
        if not isinstance(timetable, Term):
            self.__term = term
            self.__name = name
            self.__teacherName = teacherName
            self.__year = year
            self.__full_time = self.term.checkIfStationary()

            self.__timetable = timetable
            # self.__timetable.lessonList.append(self)
            try:
                self.__timetable.put(self)
            except ValueError:
                exit(1)
        else:
            self.__term = timetable
            self.__name = term
            self.__teacherName = name
            self.__year = teacherName
            self.__full_time = self.term.checkIfStationary()

            self.__timetable = Timetable1()
            # self.__timetable.lessonList.append(self)
            try:
                self.__timetable.put(self)
            except ValueError:
                exit(1)

    @property
    def term(self):
        return self.__term

    @term.setter
    def term(self, val):
        self.__term = val

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        self.__name = val

    @property
    def teacherName(self):
        return self.__teacherName

    @teacherName.setter
    def teacherName(self, val):
        self.__teacherName = val

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, val):
        self.__year = val

    @property
    def full_time(self):
        return self.__full_time

    @full_time.setter
    def full_time(self, val):
        self.__full_time = val

    @property
    def timetable(self):
        return self.__timetable

    @timetable.setter
    def timetable(self, val):
        self.__timetable = val

    def earlierDay(self):
        from timetable1 import Timetable1
        newDay = Day.nthDayFrom(-1, self.__term.__termday__)
        newTerm = Term(newDay, self.term.hour, self.term.minute)
        if self.timetable.can_be_transferred_to(newTerm, self.full_time):
            self.term.termday__ = newDay

        # tempTerm = self.__term.__termday__
        # try:
        #     self.__term.__termday__ = day.nthDayFrom(-1, self.__term.__termday__)
        #     if self.term.checkIfStationary() != self.__full_time:
        #         raise NeitherFullNorPartError()
        # except NeitherFullNorPartError as e:
        #     print("Cannot shift!\n")
        #     self.__term.__termday__ = tempTerm

    def laterDay(self):
        from timetable1 import Timetable1
        newDay = Day.nthDayFrom(1, self.__term.__termday__)
        newTerm = Term(newDay, self.term.hour, self.term.minute)
        if self.timetable.can_be_transferred_to(newTerm, self.full_time):
            self.term.termday__ = newDay

        # tempTerm = self.__term.__termday__
        # try:
        #     self.__term.__termday__ = day.nthDayFrom(1, self.__term.__termday__)
        #     if self.term.checkIfStationary() != self.__full_time:
        #         raise NeitherFullNorPartError()
        # except NeitherFullNorPartError as e:
        #     print("Cannot shift!\n")
        #     self.__term.__termday__ = tempTerm

    def earlierTime(self):
        from timetable1 import Timetable1
        currentMinutesTime = self.term.hour * 60 + self.term.minute - self.term.duration
        newhour = math.floor(currentMinutesTime / 60)
        newminute = currentMinutesTime % 60
        newTerm = Term(self.term.termday__, newhour, newminute)
        if self.timetable.can_be_transferred_to(newTerm, self.full_time):
            self.term = newTerm

        # tempHour = self.__term.hour
        # tempMinute = self.__term.minute
        # try:
        #     currentMinutesTime = self.__term.hour * 60 + self.__term.minute
        #     currentMinutesTime -= self.__term.duration
        #     if currentMinutesTime < 0:
        #         raise NeitherFullNorPartError()
        #     self.__term.hour = math.floor(currentMinutesTime / 60)
        #     self.__term.minute = currentMinutesTime % 60
        #     if self.term.checkIfStationary() != self.__full_time:
        #         raise NeitherFullNorPartError()
        # except NeitherFullNorPartError:
        #     print("Cannot shift!\n")
        #     self.__term.hour = tempHour
        #     self.__term.minute = tempMinute

    def laterTime(self):
        from timetable1 import Timetable1
        currentMinutesTime = self.term.hour * 60 + self.term.minute + self.term.duration
        newhour = math.floor(currentMinutesTime / 60)
        newminute = currentMinutesTime % 60
        newTerm = Term(self.term.termday__, newhour, newminute)
        if self.timetable.can_be_transferred_to(newTerm, self.full_time):
            self.term = newTerm

        # tempHour = self.__term.hour
        # tempMinute = self.__term.minute
        # try:
        #     currentMinutesTime = self.__term.hour * 60 + self.__term.minute
        #     currentMinutesTime += self.__term.duration
        #     if currentMinutesTime < 0:
        #         raise NeitherFullNorPartError()
        #     self.__term.hour = math.floor(currentMinutesTime / 60)
        #     self.__term.minute = currentMinutesTime % 60
        #     if self.term.checkIfStationary() != self.__full_time:
        #         raise NeitherFullNorPartError()
        # except NeitherFullNorPartError as e:
        #     print("Cannot shift!\n")
        #     self.__term.hour = tempHour
        #     self.__term.minute = tempMinute

    def __str__(self):
        if self.full_time:
            full_time_text = "stacjonarnych"
        else:
            full_time_text = "niestacjonarnych"

        if self.year == 1:
            year_text = "Pierwszy"
        elif self.year == 2:
            year_text = "Drugi"
        elif self.year == 3:
            year_text = "Trzeci"
        else:
            year_text = "???"

        currentMinutesTime = self.term.hour * 60 + self.term.minute
        currentMinutesTime += self.term.duration
        finishHour = math.floor(currentMinutesTime / 60)
        finishMinute = str(currentMinutesTime % 60).zfill(2)
        dateStr = "{} {}:{}-{}:{}".format(self.term.termday__.getName(), self.term.hour, str(self.term.minute).zfill(2), finishHour,
                                          finishMinute)
        return "{} ({})\n                  {} rok studiów {}\n                  Prowadzący: {}\n".format(self.name,
                                                                                                         dateStr,
                                                                                                         year_text,
                                                                                                         full_time_text,
                                                                                                         self.teacherName)




    def getCurrentLessonIndex(self):    #nie przetestowane!
        for i in range(len(self.timetable.lessonList)):
            if self.timetable.lessonList.term == self.term:
                return i
        return -1




    def __rshift__(self, other: int):
        newTerm = copy.deepcopy(self.term)
        for i in range(other):
            newTerm = newTerm.getNextTerm()
        if self.timetable.can_be_transferred_to(newTerm, self.full_time):
            self.term = newTerm
        else:
            print("Can not shift this term!")


    def __lshift__(self, other: int):
        newTerm = copy.deepcopy(self.term)
        for i in range(other):
            newTerm = newTerm.getPreviousTerm()
        if self.timetable.can_be_transferred_to(newTerm, self.full_time):
            self.term = newTerm
        else:
            print("Can not shift this term!")


if __name__ == "__main__":
    lesson = Lesson(Term(Day.TUE, 9, 35), "Programowanie skryptowe", "Stanisław Polak", 2)
    print(lesson)
    """Programowanie skryptowe (Wtorek 9:35-11:05)
                  Drugi rok studiów stacjonarnych
                  Prowadzący: Stanisław Polak"""
