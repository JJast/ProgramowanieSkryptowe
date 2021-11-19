from DeanerySystem.term import Term
from DeanerySystem.day import Day

class Diff(object):
    def __init__(self, term1, term2):
        self.days = abs(term1.__termday__.difference(term2.__termday__))
        self.hours = 24*self.days + abs(term1.__hour - term2.__hour)
        self.minutes = 60*self.hours + abs(term1.__minute - term2.__minute)