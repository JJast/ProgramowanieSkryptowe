from day import Day
from basicTerm import BasicTerm
import math

class NeitherFullNorPartError(Exception):  # w dokumentacji bylo ze lepiej dziedziczyc z Exception niz BaseException
    pass


class Term(BasicTerm):

    def __init__(self, day, hours, minutes=90):
        if isinstance(day, Day):
            self.__termday = day
            self.hour =  hours   
            self.minute = minutes
            self.duration = 90
        else:
            super().__init__(day, hours, minutes)
    
    def earlierThan(self, termin):
        if hasattr(self, '__termday'):
            if (termin._Term__termday == self._Term__termday and termin.hour > self.hour) or (termin._Term__termday > self._Term__termday) or (termin._Term__termday == self._Term__termday and termin.hour == self.hour and termin.minute > self.minute):
                return True
            return False
        else:
            if (termin.hour > self.hour) or (termin.hour == self.hour and termin.minute > self.minute):
                return True
            return False

    def laterThan(self, termin):
        if hasattr(self, '__termday'):
            if (termin._Term__termday == self._Term__termday and termin.hour < self.hour) or (termin._Term__termday < self._Term__termday) or (termin._Term__termday == self._Term__termday and termin.hour == self.hour and termin.minute < self.minute):
                return True
            return False
        else:
            if (termin.hour < self.hour) or (termin.hour == self.hour and termin.minute < self.minute):
                return True
            return False

    def equals(self, termin):
        if hasattr(self, '__termday'):
            if (termin._Term__termday == self._Term__termday and termin.hour == self.hour and termin.minute == self.minute):
                return True
            return False
        else:
            if (termin.hour == self.hour and termin.minute == self.minute):
                return True
            return False

    def endTime(self):
        minutesTerm = self.hour * 60 + self.minute + self.duration
        endMinute = int(minutesTerm % 60)
        endHour = int((minutesTerm - self.minute)/60)

        return Term(self._Term__termday, endHour, endMinute)
    
    def setTerm(self, term, timeFromMidnight):
        cos = str(term).split()
        temp = str(cos[0]).lower()
        if temp == "poniedziałek":
            day = Day.MON
        if temp == "wtorek":
            day = Day.TUE
        if temp == "środa":
            day = Day.WED
        if temp == "czwartek":
            day = Day.THU
        if temp == "piątek":
            day = Day.FRI
        if temp == "sobota":
            day = Day.SAT
        if temp == "niedziela":
            day = Day.SUN
        
        time = cos[1].split(":")
        self.hour = int(time[0])
        self.minute = int(time[1]) 
        self.duration = int(timeFromMidnight-((self.hour*60) + self.minute))

    def __lt__(self, termin):
        return self.earlierThan(termin)
    
    def __gt__(self, termin):
        return self.laterThan(termin)
    
    def __eq__(self, termin):
        return self.equals(termin)

    def __le__(self, termin):
        return self.earlierThan(termin) or self.equals(termin)
    
    def __ge__(self, termin):
        return self.laterThan(termin) or self.equals(termin)
    
    def __sub__(self, termin):
        minutesTerm1 = self.hour * 60 + self.minute + self.duration
        minutesTerm2 = termin.hour * 60 + termin.minute
        return Term(termin.hour, termin.minute, minutesTerm1 - minutesTerm2)

    def checkIfStationary(self):
        if (Day.MON.value <= self._Term__termday.value <= Day.THU.value and 8 <= self.hour < 20) or (self._Term__termday.value == Day.FRI.value and 8 <= self.hour < 17):
            return True
        if (Day.SAT.value <= self._Term__termday.value <= Day.SUN.value and 8 <= self.hour < 20) or (self._Term__termday.value == Day.FRI.value and 17 <= self.hour < 20):
            return False
        raise NeitherFullNorPartError
    
    def __str__(self):
        if hasattr(self, 'duration')==False:
            term = "{} {}:{}".format(self._Term__termday.getName(), self.hour, str(self.minute).zfill(2))
            return term
        if hasattr(self, '__termday')==False:
            term = "{}:{} [{}]".format(self.hour, str(self.minute).zfill(2), self.duration)
            return term
        if hasattr(self, '__termday')==False and hasattr(self, 'duration')==False:
            term = "{}:{}".format(self.hour, str(self.minute).zfill(2))
            return term    
        else:
            term = "{} {}:{} [{}]".format(self._Term__termday.getName(), self.hour, str(self.minute).zfill(2), self.duration)
            return term