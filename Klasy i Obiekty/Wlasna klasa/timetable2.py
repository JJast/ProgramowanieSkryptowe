import math

from DeanerySystem import Term, Day
from basicTimetable import BasicTimetable
from lesson import Lesson, NeitherFullNorPartError
from bbreak import Break, BasicTerm


class Timetable2(BasicTimetable):
    """ Class containing a set of operations to manage the timetable """
    skipBreaks = False

    def __init__(self, breaks):
        super().__init__()
        self.breaks = breaks

    ##########################################################
    def can_be_transferred_to(self, term: Term, full_time: bool) -> bool:
        if not Timetable2.skipBreaks:
            for b in self.breaks:
                if not term.hasNotClashWithAnotherTerm(b.term):
                    return False

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
                if (lessonMinutesStart <= termMinutesStart < lessonMinutesStop):
                    return False
                elif (lessonMinutesStart < termMinutesStop <= lessonMinutesStop):
                    return False
        return True

    ##########################################################

    def busy(self, term: Term) -> bool:
        for lesson in self.lessonList.values():
            if lesson.term == term or lesson.term.hasNotClashWithAnotherTerm(term):
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
            self.printTime(currHour, currMinute)
            for currDay in Day:  # przechodz po dniach tygodnia
                currentTerm = Term(currDay, currHour, currMinute)
                lesson = self.get(currentTerm)
                if lesson is not None:
                    print("*", lesson.name.ljust(11), end="")
                    continue
                print("*"," " * 11, end="")
            currHour += 1
            currMinute += 30
            if currMinute >= 60:
                currHour += 1
                currMinute = currMinute % 60
            if self.skipBreaks:
                print("\n", " " * 11, "*" * 90)
            else:
                print()
                if i < len(self.breaks):
                    self.printTime(currHour, currMinute, self.breaks[i].term.duration)
                    print('-' * 90)
                    currMinute += self.breaks[i].term.duration
                    if currMinute >= 60:
                        currHour += 1
                        currMinute = currMinute % 60
        return ""



    @staticmethod
    def printTime(currHour, currMinute, duration = 90):
        currentMinutesTime = currHour * 60 + currMinute
        finishMinutesTime = currentMinutesTime + duration
        finishHour = math.floor(finishMinutesTime / 60)
        finishMinute = str(finishMinutesTime % 60).zfill(2)
        dateStr = "{}:{}-{}:{}".format(str(currHour).zfill(2), str(currMinute).zfill(2)
                                       , finishHour, finishMinute)
        print(dateStr.ljust(13), end="")



if __name__ == '__main__':
    Timetable2.skipBreaks = True
    breaks = [Break(BasicTerm(9, 30, 5)), Break(BasicTerm(11, 5, 10)), Break(BasicTerm(12, 45, 15)),
              Break(BasicTerm(14, 30, 5)), Break(BasicTerm(16, 5, 5)), Break(BasicTerm(17, 45, 5)), Break(BasicTerm(19, 15, 5))]
    lesson = Lesson(Term(Day.WED, 8, 0), "Polski", "Krzysztof", 2)
    lesson1 = Lesson(Term(Day.SAT, 9, 30), "Angielski", "Krzysztof", 2)
    lesson2 = Lesson(Term(Day.SAT, 9, 35), "Angielski", "Krzysztof", 2)
    timetable = Timetable2(breaks)
    try:
        timetable.put(lesson)
        #timetable.put(lesson1)
        timetable.put(lesson2)
    except ValueError:
        exit(0)
    print(timetable)

