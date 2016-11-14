#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
  Example code for observer pattern.
"""


class publisher():
    """Abstract observer"""
    def __init__(self):
        self.followers = []
        self.state = ' '

    def add(self, concrete_follower):
        self.followers.append(concrete_follower)

    def remove(self, concrete_follower):
        self.followers.remove(concrete_follower)

    def __inform(self):
        for person in self.followers:
            person.notify()

    def __state_changed(self):
        print("Notice: %s" % self.state)
        self.__inform()

    def publish(self, concrete_publish):
        self.state = concrete_publish
        self.__state_changed()


class observer():
    """Observer"""
    def __init__(self, name):
        self.name = name

    def notify(self):
        pass


class active_student(observer):
    def notify(self):
        print("%s: I have get your message, thank you." % self.name)


class inactive_student(observer):
    def notify(self):
        print("%s: Oh, I see." % self.name)

if __name__ == "__main__":
    publisher1 = publisher()
    observer1 = active_student('Tom')
    observer2 = inactive_student('Jerry')
    publisher1.add(observer1)
    publisher1.add(observer2)
    message = "We will have an exam next class."
    publisher1.publish(message)