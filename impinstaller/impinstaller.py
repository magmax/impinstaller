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
from optparse import OptionParser
from Patterns import Singleton
from log import Log
import consts

class Configuration (object):
    def __init__(self):
        parser = OptionParser(version=consts.VERSION)

        self.options, self.files = parser.parse_args()

        if len(self.files) != 1:
            Log.error  ("Incorrect number of arguments")
            parser.error ("incorrect number of arguments")

class Installer (object):
    name = None
    shortname = None
    vendor = None
    version = None

    def build (self):
        self.__check_mandatory_arguments()

        print 'Building Application: ' + self.name

    def __check_mandatory_arguments(self):
        assert self.name, 'You must add the Application name'
        assert self.shortname, 'You must add the Application short name'
        assert self.vendor, 'You must add the vendor name'


class InstructionsReader (object):
    __config = Configuration()

    def read(self):
        for filename in self.__config.files:
            filedata = open (filename)
            exec filedata
            filedata.close()


def main ():
    try:
        reader = InstructionsReader()
        reader.read()
    except Exception as e:
        Log.error ( sys.exc_info()[0] )
        Log.error ( sys.exc_info()[1:] )
        exit (2)

if __name__ == '__main__':
    main ()
