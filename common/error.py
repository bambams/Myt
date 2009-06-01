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


class Error(Exception):
    """Base class for Myt exceptions.
    """;
    pass;

class ArgumentError(Error):
    """Indicates that one or more arguments is invalid.

    Attributes:
        [argname] -- The name of the argument.
        [msg] -- A contextual message.
    """;
    DEFAULT = "Invalid argument.";
    NAMEONLY = "Argument '{0}' is invalid.";
    MSGONLY = "{0} {1}";
    BOTH = "{0} {1}";
    
    def __init__(self, argname=None, msg=None):
        self.argname = argname;
        self.message = msg;
    
    def __str__(self):
        if(self.argname == None and self.message == None):
            return DEFAULT;
        elif(self.argname != None and self.message == None):
            return string.format(NAMEONLY, self.argname);
        elif(self.argname == None and self.message != None):
            return string.format(MSGONLY, DEFAULT, self.message);
        else:
            return string.format(BOTH, string.format(NAMEONLY, self.argname), self.message);

class CmdLineArgumentError(ArgumentError):
    """Indicates that one or more command-line arguments is invalid.
    """;

class CmdLineOptionError(CmdLineArgumentError):
    """Indicates that one or more command-line options is invalid.
    """;
    NAMEONLY = "Option '{0}' is invalid.";

