import copy

from .basicTerm import BasicTerm
from .day import Day
import math


class NeitherFullNorPartError(Exception):  # w dokumentacji bylo ze lepiej dziedziczyc z Exception niz BaseException
    pass


class Term(BasicTerm):

    def __init__(self, termday, hour, minute=90):
        if isinstance(termday, Day):
            self.__termday__ = termday
            self.__hour = hour
            self.__minute = minute
            self.__duration = 90
        else:  # parametry konstruktora to hour, minute, duration
            super().__init__(termday, hour, minute)

    @property
    def termday__(self):
        return self.__termday__

    @termday__.setter
    def termday__(self, val):
        self.__termday__ = val

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, val):
        self.__hour = val

    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, val):
        self.__minute = val

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, val):
        self.__duration = val

    def __str__(self):
        if hasattr(self, '__termday__'):
            return "{} {}:{} [{}]".format(self.__termday__.getName(), str(self.__hour), str(self.__minute).zfill(2),
                                          str(self.__duration))
        return "{}:{} [{}]".format(str(self.__hour), str(self.__minute).zfill(2), str(self.__duration))

    def earlierThan(self, termin):
        if (termin.__hour > self.__hour) or (termin.__hour == self.__hour and termin.__minute > self.__minute):
            return True
        return False

    def laterThan(self, termin):
        if (termin.__hour == self.__hour and termin.__minute == self.__minute) or self.earlierThan(termin):
            return False
        return True

    def equals(self, termin):
        if termin.__hour == self.__hour and termin.__minute == self.__minute and termin.__duration == self.__duration:
            return True
        return False

    def difference(self, termin):
        return Diff(self, termin)

    # overload < (less than) operator
    def __lt__(self, termin):
        return self.earlierThan(termin)

    # overload > (greater than) operator
    def __gt__(self, termin):
        return self.laterThan(termin)

    # overload <= (less than or equal to) operator
    def __le__(self, termin):
        return self.earlierThan(termin) or self.equals(termin)

    # overload >= (greater than or equal to) operator
    def __ge__(self, termin):
        return self.laterThan(termin) or self.equals(termin)

    # overload == (equal to) operator
    def __eq__(self, termin):
        return self.equals(termin)

    # overload - operator
    def __sub__(self, termin):
        minutesTerm1 = self.__hour * 60 + self.__minute + self.__duration
        minutesTerm2 = termin.__hour * 60 + termin.__minute
        return Term(termin.__hour, termin.__minute, minutesTerm1 - minutesTerm2)

    def checkIfStationary(self):
        if Day.MON.value <= self.__termday__.value <= Day.THU.value and 8 <= self.hour < 20:
            return True
        if (Day.SAT.value <= self.__termday__.value <= Day.SUN.value and 8 <= self.hour < 20) or (
                self.__termday__.value == Day.FRI.value and 17 <= self.hour < 20):
            return False
        raise NeitherFullNorPartError

    def getNextTerm_Dumb(self) -> 'Term':
        newTermTime = self.hour * 60 + self.minute + self.duration
        newTermHour = math.floor(newTermTime / 60)
        newTermMinute = (newTermTime - newTermHour * 60)
        return Term(self.termday__, newTermHour, newTermMinute)

    def getPreviousTerm_Dumb(self) -> 'Term':
        newTermTime = self.hour * 60 + self.minute - self.duration
        newTermHour = math.floor(newTermTime / 60)
        newTermMinute = (newTermTime - newTermHour * 60)
        return Term(self.termday__, newTermHour, newTermMinute)

    def getNextTerm(self) -> 'Term':
        selfCopy = copy.deepcopy(self)
        for i in range(7 * 16):
            nextT = selfCopy.getNextTerm_Dumb()
            if nextT.hour >= 20:
                nextT.termday__ = Day.nthDayFrom(1, self.termday__)
                nextT.hour = 8
                nextT.minute = 0
            try:
                if nextT.checkIfStationary() == self.checkIfStationary():
                    return nextT
            except NeitherFullNorPartError:
                pass
            selfCopy = nextT
        return None

    def getPreviousTerm(self) -> 'Term':
        selfCopy = copy.deepcopy(self)
        for i in range(7 * 16):
            nextT = selfCopy.getPreviousTerm_Dumb()
            if nextT.hour < 8:
                nextT.termday__ = Day.nthDayFrom(-1, self.termday__)
                nextT.hour = 18
                nextT.minute = 30
            try:
                if nextT.checkIfStationary() == self.checkIfStationary():
                    return nextT
            except NeitherFullNorPartError:
                pass
            selfCopy = nextT
        return None

    def hasNotClashWithAnotherTerm(self, other: 'Term'):
        if not hasattr(other, "termday__") or self.termday__ == other.termday__:
            selfMinutesStart = self.hour * 60 + self.minute
            selfMinutesStop = selfMinutesStart + self.duration
            secondMinutesStart = other.hour * 60 + other.minute
            secondMinutesStop = secondMinutesStart + other.duration
            if (selfMinutesStart <= secondMinutesStart < selfMinutesStop) or (
                    selfMinutesStart < secondMinutesStop <= selfMinutesStop):
                return False
        return True

    def __hash__(self):
        return hash((self.hour * 60 + self.minute, self.termday__.value))

    @staticmethod
    def convertTermToNumer(term: 'Term'):
        return 24*60*term.termday__.value + 60*term.hour + term.minute

    @staticmethod
    def convertNumberToTerm(numTerm: int):
        termDayValue = math.floor(numTerm/(24*60))
        termHour = math.floor((numTerm - 24*60*termDayValue)/60)
        termMinute = numTerm - termHour * 60 - termDayValue * 24 * 60
        termDay = Day(termDayValue)
        newTerm = Term(termDay, termHour, termMinute)
        return newTerm

class Diff(object):
    def __init__(self, term1, term2):
        term1Minutes = term1.hour * 60 + term1.minute
        term2Minutes = term2.hour * 60 + term2.minute
        minDiff = term2Minutes - term1Minutes
        if minDiff <= 0:
            minDiff += 60 * 24

        daysDiff = term1.termday__.difference(term2.termday__)
        minDiff += 24 * 60 * (daysDiff - 0)

        self.seconds = minDiff * 60
        self.minutes = minDiff
        self.hours = math.floor(minDiff / 60)
        self.days = daysDiff
