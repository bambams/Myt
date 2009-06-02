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
import common.host;

class User:
    """Represents a Myt user.
    """;
    def __init__(self, name, host):
        if not isinstance(host, myt.host.Host):
            raise InvalidArgumentError(argname="host", msg="Expected object of type myt.host.Host.");
        if not isinstance(name, str):
            raise InvalidArgumentError(argname="name", msg="Expected object of type str.");

        self.name = name;
        self.host = host;

    def __repr__(self):
        return "myt.user.User(\"" + self.name + "\", \"" + self.host + "\")";

    def __str__(self):
        return self.name + '@' + self.host;

