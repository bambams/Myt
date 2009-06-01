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

import myt.mode;
import string;
# import xml;

#DEFAULT_FILE = "~/.myt/config.xml";

class Config:
    def __init__(self):
        self.bcc = None;
        self.cc = None;
#        self.file = DEFAULT_FILE;
        self.interactive = False;
        self.host = None;
        self.message = None;
        self.mode = myt.mode.mail;
        self.password = None;
        self.print_config = False;
        self.recipient = None;
        self.user = None;
        self.verbose = False;
     
    def load(self):
        pass;
    
    def __str__(self):
        FORMAT = """bcc: {0}
cc: {1}
interactive: {2}
host: {3}
len(message): {4}
mode: {5}
password: {6}
recipient: {7}
user: {8}
verbose: {9}""";
        msglen = [lambda msg: len(msg), lambda msg: 0][self.message == None](self.message);
        return str.format(FORMAT, self.bcc, self.cc,
                          self.interactive, self.host, msglen, self.mode,
                          self.password, self.recipient, self.user,
                          self.verbose);

