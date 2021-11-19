from DeanerySystem import *


class Break(object):
    def __init__(self, term: BasicTerm):
        self.__term = term

    @property
    def term(self):
        return self.__term

    @term.setter
    def term(self, val):
        self.__term = val

    def __str__(self):
        return "Przerwa"