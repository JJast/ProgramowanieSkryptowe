import math


class BasicTerm(object):

    def __init__(self, hour, minute, duration=90):
        self.hour = hour
        self.minute = minute
        self.duration = duration