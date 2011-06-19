#!/usr/bin/python
# -*- coding:utf-8; tab-width:4; mode:python -*-

# impinstaller
#
# Copyright (C) 2011 Miguel Ángel García
#
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA


import sys, os
from Patterns import Singleton, TypedAttr
from log import Log
import consts


class ImpObject(object):
    def __init__(self):
        self.name = None
        self.description = None

class ImpInstaller(ImpObject):
    def __init__(self):
        super(ImpInstaller, self).__init__()
        self.actions = []
        self.components = []

    def addComponent (self, component):
        if not isinstance (component, Component):
            raise TypeError
        self.components.append(component)

    def addAction (self, action):
        if not isinstance (action, Action):
            raise TypeError
        self.actions.append (action)

class Component(ImpObject):
    path = TypedAttr ('__path', str) 

    def __init__(self, path, mandatory=False):
        super(Component, self).__init__()
        self.__path = path
        self.mandatory = mandatory
        self.files = []

    def addFile (self, impfile):
        if not isinstance (impfile, File):
            raise TypeError
        self.files.append(impfile)

class File(ImpObject):
    def __init__(self, origin, target=None):
        super(File, self).__init__()
        self.origin = origin
        self.target = target

class Action(ImpObject):
    def __init__(self):
        super(Action, self).__init__()
        self.conditions = []


    def when (self, variable):
        self.conditions.append (Condition(variable))

class ActionShowWindow (Action):
    def __init__(self):
        super(ActionShowWindow, self).__init__()
        
class Condition(ImpObject):
    def __init__(self, variable):
        super(Condition, self).__init__()
        self.variable = variable
        self.type = None
        self.target = None

    def isEqualTo (self, variable):
        self.type = 'equality'
        self.target = variable
