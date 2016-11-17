#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
  Copy from Wikipedia.
"""


class Observable:
    def __init__(self):
        self.__observers = []

    def register_observer(self, observer):
        self.__observers.append(observer)

    def notify_observers(self, *args):
        for observer in self.__observers:
            observer.notify(self, *args)


class Observer:
    def __init__(self, observable):
        observable.register_observer(self)

    def notify(self, observable, *args):
        print('Got', args, 'From', observable)


subject = Observable()
observer = Observer(subject)
subject.notify_observers('test')