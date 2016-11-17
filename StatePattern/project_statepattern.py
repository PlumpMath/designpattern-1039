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

    def get_currentstate(self):
        return self.state

    def change_currentwork(self):
        if not self.state:
            self.set_currentstate(BuildState())
        else:
            self.state.change_currentwork(self)

    def do_currentwork(self):
        self.state.do(self)


class BuildState:
    def do(self, project):
        print("%s is on the build state." % project.get_name())

    def change_currentwork(self, project):
        project.set_currentstate(DevelopState())


class DevelopState:
    def do(self, project):
        print("%s in on the develop state." % project.get_name())

    def change_currentwork(self, project):
        project.set_currentstate(TestState())


class TestState:
    def do(self, project):
        print("%s in on the test state." % project.get_name())

    def change_currentwork(self, project):
        project.set_currentstate(EndState())


class EndState:
    def do(self, project):
        print("%s in on the end state." % project.get_name())


class Work:
    def __init__(self, name):
        self.project = Project()
        self.project.set_name(name)

    def do_work(self):
        for i in range(4):
            self.project.change_currentwork()
            self.project.do_currentwork()
        print("%s is done." % self.project.get_name())

if __name__ == '__main__':
    projectA = Work("Free ROI")
    projectA.do_work()
