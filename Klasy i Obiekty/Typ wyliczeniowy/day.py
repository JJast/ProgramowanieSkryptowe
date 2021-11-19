from enum import Enum

class Day(Enum):
    MON = 0
    TUE = 1
    WED = 2
    THU = 3
    FRI = 4
    SAT = 5
    SUN = 6

    def difference(self, day):
        temp1 = day.value - self.value
        temp2 = 7-abs(temp1)
        if(self.value < day.value): # jezeli tak, to temp1 = nextVal, temp2 = prevVal
            if(temp2 < abs(temp1)):
                return -1 * temp2
            return temp1
        # temp1 = prevVal, temp2 = nextVal
        if(temp2 < abs(temp1)): 
            return temp2
        return -1 * abs(temp1)


def nthDayFrom(n, day):
    temp = (day.value + n) % 7
    return Day(temp)

