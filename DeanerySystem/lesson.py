from term import Term
from day import Day
import math

class NeitherFullNorPartError(Exception):  # w dokumentacji bylo ze lepiej dziedziczyc z Exception niz BaseException
    pass

class Lesson():

    def __init__(self, term: Term, name: str, teacherName: str, year: int=1):
            self.term = term
            self.name = name
            self.teacherName = teacherName
            self.year = year
            self.full_time = self.term.checkIfStationary()
            

    def __str__(self):
        if self.full_time == True:
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
        dateStr = "{} {}:{}-{}:{}".format(self.term._Term__termday.getName(), self.term.hour, str(self.term.minute).zfill(2), finishHour,finishMinute)
        return "{} ({})\n{} rok studiów {}\nProwadzący: {}\n".format(self.name, dateStr, year_text, full_time_text, self.teacherName)
    
    def earlierDay(self):
        newDay = Day.nthDayFrom(-1, self.term._Term__termday)
        if self.full_time:
            if self.term._Term__termday == Day.MON:
                print("Nie da się przesunąć")
            else:
                self.term._Term__termday = newDay
                return Lesson(Term(newDay, self.term.hour, self.term.minute), self.name, self.teacherName, self.year)
        else:
            if self.term._Term__termday == Day.FRI or (self.term._Term__termday == Day.SAT and self.term.hour > 15 and self.term.minute > 30):
                print("Nie da się przesunąć")
                
            else:
                self.term._Term__termday = newDay
                return Lesson(Term(newDay, self.term.hour, self.term.minute), self.name, self.teacherName, self.year)
            
    def laterDay(self):
        newDay = Day.nthDayFrom(1, self.term._Term__termday)
        if self.full_time:
            if self.term._Term__termday == Day.FRI or (self.term._Term__termday == Day.THU and self.term.hour > 15 and self.term.minute > 30):
                print("Nie da się przesunąć")
            else:
                self.term._Term__termday = newDay
                return Lesson(Term(newDay, self.term.hour, self.term.minute), self.name, self.teacherName, self.year)
        else:
            if (self.term._Term__termday == Day.SUN):
                print("Nie da się przesunąć")
            else:
                self.term._Term__termday = newDay
                return Lesson(Term(newDay, self.term.hour, self.term.minute), self.name, self.teacherName, self.year)

    def earlierTime(self):
        if self.full_time:
            if self.term.hour > 9 or (self.term.hour==9 and self.term.minute > 30):
                currentMinutesTime = self.term.hour * 60 + self.term.minute - self.term.duration
                newminute = int(currentMinutesTime % 60)
                newhour = int((currentMinutesTime - newminute)/60)
                self.term.hour = newhour
                self.term.minute = newminute
        else:
            if self.term.hour < 9 or (self.term.hour==9 and self.term.minute < 30) or (self.term._Term__termday==Day.FRI and self.term.hour < 19)  == False:
                currentMinutesTime = self.term.hour * 60 + self.term.minute - self.term.duration
                newminute = int(currentMinutesTime % 60)
                newhour = int((currentMinutesTime - newminute)/60)
                self.term.hour = newhour
                self.term.minute = newminute
    
    def laterTime(self):
        if self.full_time:
            if self.term.hour > 18 or (self.term.hour==18 and self.term.minute > 30) or (self.term._Term__termday == Day.FRI and self.term.hour > 15) == False:
                currentMinutesTime = self.term.hour * 60 + self.term.minute + self.term.duration
                newminute = int(currentMinutesTime % 60)
                newhour = int((currentMinutesTime - newminute)/60)
                self.term.hour = newhour
                self.term.minute = newminute
        else:
            if self.term.hour < 18 or (self.term.hour==18 and self.term.minute < 30):
                currentMinutesTime = self.term.hour * 60 + self.term.minute + self.term.duration
                newminute = int(currentMinutesTime % 60)
                newhour = int((currentMinutesTime - newminute)/60)
                self.term.hour = newhour
                self.term.minute = newminute



#lesson = Lesson(Term(Day.TUE, 9, 35), "Programowanie", "Polak", 3)
#print(lesson)