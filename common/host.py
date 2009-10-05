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

import common.error;

class Host:
    def __init__(self, name=None, ip=None):
        self.name = name;
        self.ip = ip;

    def __repr__(self):
        return "myt.host.Host(\"" + self.name + "\")";

    def __str__(self):
        return self.name;

    def lookup(self, refresh=False):
        if self.name == None:
            raise Exception, "Attempted host lookup without name.";

        if self.ip != None and not refresh:
            return;

        raise NotImplementedError;

