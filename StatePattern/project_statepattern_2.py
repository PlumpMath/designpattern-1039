#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
  Example code for state pattern.
  A procedure of completing a project.
  The relation between abstract and concrete class do not use inheritance.
"""


class Project:
    def __init__(self):
        self.name = None
        self.state = None

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_currentstate(self, state):
        self.state = state

    def get_currentstate(self):
        return self.state

    def do_currentwork(self):
        self.state.do(self)


class BuildState:
    def do(self, project):
        print("%s is on the build state." % project.get_name())
        project.set_currentstate(DevelopState())


class DevelopState:
    def do(self, project):
        print("%s in on the develop state." % project.get_name())
        project.set_currentstate(TestState())


class TestState:
    def do(self, project):
        print("%s in on the test state." % project.get_name())
        project.set_currentstate(EndState())


class EndState:
    def do(self, project):
        print("%s in on the end state." % project.get_name())
        print("%s is done." % project.get_name())


class Work:
    def __init__(self, name):
        self.project = Project()
        self.project.set_name(name)
        self.project.set_currentstate(BuildState())

    def do_work(self):
        print("------Begin------")
        self.project.do_currentwork()
        print("------Next------")
        self.project.do_currentwork()
        print("------Next------")
        self.project.do_currentwork()
        print("------Next------")
        self.project.do_currentwork()
        print("------End------")

if __name__ == '__main__':
    projectA = Work("Free ROI")
    projectA.do_work()
