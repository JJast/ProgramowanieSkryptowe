import math


class BasicTerm(object):

    def __init__(self, hour, minute, duration=90):
        self.__hour = hour
        self.__minute = minute
        self.__duration = duration

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

    def hasNotClashWithAnotherTerm(self, other: 'BasicTerm'):
        selfMinutesStart = self.hour * 60 + self.minute
        selfMinutesStop = selfMinutesStart + self.duration
        secondMinutesStart = other.hour * 60 + other.minute
        secondMinutesStop = secondMinutesStart + other.duration
        if (selfMinutesStart <= secondMinutesStart < selfMinutesStop) or (
                selfMinutesStart < secondMinutesStop <= selfMinutesStop):
            return False
        return True


    def printTimeRange(self):
        currentMinutesTime = self.hour * 60 + self.minute
        currentMinutesTime += self.duration
        finishHour = math.floor(currentMinutesTime / 60)
        finishMinute = str(currentMinutesTime % 60).zfill(2)
        return "{}:{}-{}:{}".format(self.hour, str(self.minute).zfill(2), finishHour, finishMinute)