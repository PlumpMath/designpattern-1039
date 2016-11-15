#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
  Example code for state pattern.
  A procedure of completing a project.
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

    def do_currentwork(self):
        self.state.do(self)

    def do(self, project):
        pass


class BuildState(Project):
    def do(self, project):
        print("%s is on the build state." % project.get_name())
        self.set_currentstate(DevelopState)


class DevelopState(Project):
    def do(self, project):
        print("%s in on the develop state." % project.get_name())


class TestState(Project):
    def do(self, project):
        print("%s in on the test state." % project.get_name())


class EndState(Project):
    def do(self, project):
        print("%s in on the end state." % project.get_name())
        print("%s is done." % project.get_name())


class Work:
    def __init__(self, name):
        self.project = Project()
        self.project.set_name(name)

    def do_work(self):
        print("------Begin------")
        self.project.set_currentstate(BuildState())
        self.project.do_currentwork()
        print("------Next------")
        self.project.set_currentstate(DevelopState())
        self.project.do_currentwork()
        print("------Next------")
        self.project.set_currentstate(TestState())
        self.project.do_currentwork()
        print("------Next------")
        self.project.set_currentstate(EndState())
        self.project.do_currentwork()
        print("------End------")

if __name__ == '__main__':
    projectA = Work("Free ROI")
    projectA.do_work()
