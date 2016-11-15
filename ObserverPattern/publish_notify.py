#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
  Example code for observer pattern.
  Teacher publishes notices and students receive them.
"""


class publisher():
    """ Abstract publisher """
    """ Could add, remove, and inform the followers. """
    def __init__(self):
        self.followers = []
        self.state = ' '

    def add(self, *args):
        for concrete_follower in args:
            self.followers.append(concrete_follower)

    def remove(self, *args):
        for concrete_follower in args:
            self.followers.remove(concrete_follower)

    def publisher(self, *args):
        pass

    def inform(self):
        for person in self.followers:
            person.notify()


class teacher(publisher):
    """ Concrete publisher """
    """ Have their own publisher style. """
    def publisher(self, concrete_publish):
        self.state = concrete_publish
        print(self.state)
        self.inform()


class observer():
    """ Abstract observer """
    """ Could receive notice. """
    def __init__(self, name):
        self.name = name

    def notify(self):
        pass


class active_student(observer):
    """ One type of student, concrete observer. """
    def notify(self):
        print("%s: I have get your message, thank you." % self.name)


class inactive_student(observer):
    """ Concrete observer """
    def notify(self):
        print("%s: Oh, I see." % self.name)

if __name__ == "__main__":
    """ init """
    publisher1 = teacher()
    observer1 = active_student('Tom')
    observer2 = inactive_student('Jerry')
    publisher1.add(observer1, observer2)

    """ publish notices """
    message1 = "We will have an exam next class."
    publisher1.publisher(message1)
    print("-----Remove Observer1 From the Inform List-----")
    publisher1.remove(observer1)
    message2 = "%s is not on the inform list." % observer1.name
    publisher1.publisher(message2)
