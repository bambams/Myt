#
# Myt is a secure messaging system composed of E-mail and chat facilities.
# Copyright (C) 2009 Brandon McCaig, Samuel Henderson
#
# This file is part of Myt.
#
# Myt is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# Myt is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Myt.  If not, see <http://www.gnu.org/licenses/>.
#

import grp;
import myt.mode;
import os;
import pwd;
import string;
# import xml;

DEFAULT_FILE = "/etc/mytd.xml";

class Config:
    def __init__(self):
        self.chroot = None;
        self.detach = None;
#        self.file = DEFAULT_FILE;
        self.gid = os.getgid();
        self.print_config = False;
        self.stderr = None;
        self.stdin = None;
        self.stdout = None;
        self.uid = os.getuid();
        self.umask = 0;
        self.workdir = "/";
    
    def load(self):
        pass;
    
    def __str__(self):
        FORMAT = """chroot = {0}
detach = {1}
gid = {2} ({3})
stderr = {4}
stdin = {5}
stdout = {6}
uid = {7} ({8})
umask = {9}
workdir = {10}""";

        return str.format(FORMAT, self.chroot, self.detach,
                          grp.getgrgid(self.gid)[0], self.gid, self.stderr,
                          self.stdin, self.stdout, pwd.getpwuid(self.uid)[0],
                          self.uid, self.umask, self.workdir);

