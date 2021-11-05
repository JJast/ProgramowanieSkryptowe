import math
import unittest
from typing import List
from term import Term
from day import Day
from action import Action
from lesson import Lesson


class BasicTimetable:
    def __init__(self):
        self.lessonList = {}

    ##########################################################
    def can_be_transferred_to(self, term: Term, full_time: bool) -> bool:
        """
Informs whether a lesson can be transferred to the given term
Parameters
----------
term : Term
    The term checked for the transferability
full_time : bool
    Full-time or part-time studies
Returns
-------
bool
    **True** if the lesson can be transferred to this term
        """
        pass

    ##########################################################

    def busy(self, term: Term) -> bool:
        """
Informs whether the given term is busy.  Should not be confused with ``can_be_transfered_to()``
since there might be free term where the lesson cannot be transferred.
Parameters
----------
term : Term
    Checked term
Returns
-------
bool
    **True** if the term is busy
        """
        pass

    ##########################################################

    def put(self, lesson: Lesson) -> bool:
        """
Add the given lesson to the timetable.
Parameters
----------
lesson : Lesson
    The added  lesson
Returns
-------
bool
    **True**  if the lesson was added.  The lesson cannot be placed if the timetable slot is already occupied.
        """
        if self.can_be_transferred_to(lesson.term, lesson.full_time):
            self.lessonList[Term.convertTermToNumer(lesson.term)] = lesson
            return True
        # return False
        raise ValueError("Nie mozna wstawic lekcji " + lesson.name + " do rozkladu!")

    ##########################################################

    def parse(self, actions: List[str]) -> List[Action]:
        """
Converts an array of strings to an array of 'Action' objects.
Parameters
----------
actions:  List[str]
    A list containing the strings: "d-", "d+", "t-" or "t+"
Returns
-------
    List[Action]
        A list containing the values:  DAY_EARLIER, DAY_LATER, TIME_EARLIER or TIME_LATER
        """
        actionList = []
        for action in actions:
            if action == "d-":
                actionList.append(Action.DAY_EARLIER)
            elif action == "d+":
                actionList.append(Action.DAY_LATER)
            elif action == "t-":
                actionList.append(Action.TIME_EARLIER)
            elif action == "t+":
                actionList.append(Action.TIME_LATER)
            else:
                # print("Undefined action: \n", action)
                raise ValueError("Translation " + action + " is incorrect")
        return actionList

    ##########################################################

    def perform(self, actions: List[Action]):
        """
Transfer the lessons included in the timetable as described in the list of actions. N-th action should be sent the n-th lesson in the timetable.
Parameters
----------
actions : List[Action]
    Actions to be performed
        """

        sorted_lessonList = sorted(self.lessonList.items())
        lessonIndex = 0
        for action in actions:
            if action == Action.DAY_EARLIER:
                sorted_lessonList[lessonIndex][1].earlierDay()
            elif action == Action.DAY_LATER:
                sorted_lessonList[lessonIndex][1].laterDay()
            elif action == Action.TIME_EARLIER:
                sorted_lessonList[lessonIndex][1].earlierTime()
            elif action == Action.TIME_LATER:
                sorted_lessonList[lessonIndex][1].laterTime()
            lessonIndex = (lessonIndex + 1) % len(self.lessonList)

    ##########################################################

    def get(self, term: Term) -> Lesson:
        """
Get object (lesson) indicated by the given term.
Parameters
----------
term: Term
    Lesson date
Returns
-------
lesson: Lesson
    The lesson object or None if the term is free
        """
        if Term.convertTermToNumer(term) in self.lessonList.keys():
            return self.lessonList[Term.convertTermToNumer(term)]
        return None

    def getNthLesson(self, i: int) -> Lesson:
        sorted_lessonList = sorted(self.lessonList,
                                   key=lambda x: (24 * 60 * x.termday__.value + 60 * x.hour + x.minute))
        print(sorted_lessonList)
        return sorted_lessonList[i]

    def getDayLesson(self, day: Day) -> List[Lesson]:
        dayLessons = []
        for lesson in self.lessonList.values():
            if lesson.term.__termday__ == day:
                dayLessons.append(lesson)
        return dayLessons

    ##########################################################