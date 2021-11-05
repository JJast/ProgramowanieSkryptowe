import math
from term import Term
from day import Day
from basicTimetable import BasicTimetable
from lesson import Lesson, NeitherFullNorPartError


class Timetable1(BasicTimetable):
    """ Class containing a set of operations to manage the timetable """

    def __init__(self):
        super().__init__()

    ##########################################################
    def can_be_transferred_to(self, term: Term, full_time: bool) -> bool:
        try:
            if full_time != term.checkIfStationary():
                return False
        except NeitherFullNorPartError as e:
            return False

        for lessonTerm, lesson in self.lessonList.items():
            if lesson.term.termday__ == term.termday__:
                lessonMinutesStart = lesson.term.hour * 60 + lesson.term.minute
                lessonMinutesStop = lessonMinutesStart + lesson.term.duration
                termMinutesStart = term.hour * 60 + term.minute
                termMinutesStop = termMinutesStart + term.duration
                if (lessonMinutesStart <= termMinutesStart < lessonMinutesStop) or (
                        lessonMinutesStart < termMinutesStop <= lessonMinutesStop):
                    return False
        return True

    ##########################################################

    def busy(self, term: Term) -> bool:
        for lesson in self.lessonList.values():
            if lesson.term == term:
                return True
        return False

    ##########################################################

    def __str__(self):
        maxLen = 12
        for lesson in self.lessonList.values():
            if len(lesson.name) > maxLen:
                maxLen = len(lesson.name)
        print(" " * 12, "*Poniedziałek*Wtorek      *Środa       *Czwartek    *Piątek      *Sobota      *Niedziela")
        print(" " * 12, "*" * 90)

        currHour = 8
        currMinute = 0
        for i in range(8):
            self.printTime(i)
            for currDay in Day:  # przechodz po dniach tygodnia
                currentTerm = Term(currDay, currHour, currMinute)
                lesson = self.get(currentTerm)
                if lesson is not None:
                    print("*", lesson.name.ljust(11), end="")
                    continue
                print("*"," " * 11, end="")
            print("\n"," " * 11, "*" * 90)
            currHour += 1
            currMinute += 30
            if currMinute == 60:
                currHour += 1
                currMinute = 0
        return ""

    @staticmethod
    def printTime(i: int):
        currentMinutesTime = 8 * 60 + 90 * i
        startHour = math.floor(currentMinutesTime / 60)
        startMinute = str(currentMinutesTime % 60).zfill(2)
        finishMinutesTime = currentMinutesTime + 90
        finishHour = math.floor(finishMinutesTime / 60)
        finishMinute = str(finishMinutesTime % 60).zfill(2)
        dateStr = "{}:{}-{}:{}".format(startHour, startMinute, finishHour, finishMinute)
        print(dateStr.ljust(13), end="")



if __name__ == '__main__':
    # lesson = Lesson(Term(Day.WED, 14, 00), "Polski", "Krzysztof", 2)
    # lesson1 = Lesson(Term(Day.SAT, 9, 30), "Angielski", "Krzysztof", 2)
    # timetable = Timetable1()
    # try:
    #     timetable.put(lesson)
    #     timetable.put(lesson1)
    # except ValueError:
    #     exit(1)
    # print(timetable)
    #
    # actions = timetable.parse(["d-", "d+", "t-", "t+"])
    # timetable.perform(actions)
    # print(timetable


    timetable = Timetable1()
    lesson = Lesson(timetable, Term(Day.WED, 14, 00), "Polski", "Krzysztof", 2)
    lesson1 = Lesson(timetable, Term(Day.SAT, 9, 30), "Angielski", "Krzysztof", 2)

    actions = timetable.parse(["d-", "d+", "t-", "t+"])
    timetable.perform(actions)
    print(timetable)