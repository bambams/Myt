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

import daemon; # http://pypi.python.org/pypi/python-daemon/
import getopt;
import mytd.config;
import os;
import sys;

EXIT_FAILURE = -1;
EXIT_SUCCESS = 0;

def main(argv):
    try:
        status, cfg = parse_args(argv);
        if status < 0:
            sys.exit(EXIT_FAILURE);
        elif status == 0:
            sys.exit(EXIT_SUCCESS);
        cfg.load();
        if cfg.print_config:
            print cfg;
            sys.exit(EXIT_SUCCESS);
        with daemon.DaemonContext(
                chroot_directory=cfg.chroot,
                detach_process=cfg.detach,
                gid=cfg.gid,
                stderr=cfg.stderr,
                stdin=cfg.stdin,
                stdout=cfg.stdout,
                uid=cfg.uid,
                umask=cfg.umask,
                working_directory=cfg.workdir):
            pass;
        return EXIT_SUCCESS;
    except Exception as ex:
        print ex;
        return EXIT_FAILURE;

def parse_args(argv):
    """Parse Myt server command-line arguments.
    """;
    opts = "0:1:2:C:c:G:hLU:u:VvW:";
    longopts = ["chroot=", "config=", "gid=", "help", "license", "no-detach",
                "print-config", "stderr=", "stdin=", "stdout=", "uid=", "umask=",
                "version", "verbose", "workdir="];
    status = 1;
    cfg = mytd.config.Config();
    optlist, args = getopt.gnu_getopt(argv[1:], opts, longopts);
    if len(optlist) == 0:
        cfg.interactive = True;
    else:
        status = process_opts(cfg, optlist);
    return status, cfg;

def print_help():
    """Print the command usage/help message.
    """;
    print """  Copyright (C) 2009 Brandon McCaig, Samuel Henderson

  mytd is the server application for the Myt project, an attempt to offer
  secure E-mail and chat services in an open way.

    mytd [ -0 <file> | --stdin=<file> ] [ -1 <file> | --stdout=<file> ]
           [ -2 <file> | --stderr=<file> ]
           [ -C <directory> | --chroot <directory> ]
           [ -c <file> | --config=<file> ] [ -G <gid> | --gid=<gid> ]
           [ --no-detach ] [ --print-config ] [ -U <uid> | --uid=<uid> ]
           [ -u <umask> | --umask=<umask> ] [ -v | --verbose ]
           [ -W <directory> | --workdir=<directory> ]
    mytd [ -h | --help ]
    mytd [ -L | --license ]
    mytd [ -V | --version ]

  -0, --stdin=<file>
      Specify a file to use for stdin (NOTE: may not be used).

  -1, --stdout=<file>
      Specify a file to use for stdout (NOTE: may not be used).

  -2, --stderr=<file>
      Specify a file to use for stderr (NOTE: may not be used).

  -C, --chroot=<directory>
      Specify a directory to chroot to.

  -c, --config=<file>
      Specify a config file instead of the default.

  -G, --gid=<gid>
      The system gid to run as.

  -h, --help
      Print this message and exit.

  -L, --license
      Print the software license and exit.

  --no-detach
      Do not detach the process context.
      (See detach_process in daemon.daemon.DaemonContext).

  --print-config
      Load configuration settings from the command-line and configuration file
      and print them to standard output; then exit.

  -U, --uid=<uid>
      The system uid to run as.

  -u, --umask=<umask>
      The file creation umask to set.

  -V, --version
      Print the software version and exit.

  -v, --verbose
      Be verbose.

  -W, --workdir=<directory>
      Specify the working directory to use.
""";

def print_license():
    """Write the software license to stdout.
    """;
    print """
Myt is a secure messaging system composed of E-mail and chat facilities.
Copyright (C) 2009 Brandon McCaig, Samuel Henderson

This program is part of Myt.

Myt is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 2 of the License, or
(at your option) any later version.

Myt is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Myt.  If not, see <http://www.gnu.org/licenses/>.
""";

def print_version():
    """Write the software version to stdout.
    """;
    print "<Version goes here>";

def process_opts(cfg, optlist):
    """Process Myt server command-line options.
    """;
    for o, a in optlist:
        if o in ("-0", "--stdin"):
            print "Received stdin '" + a + "'";
            pass;
        if o in ("-1", "--stdout"):
            print "Received stdout '" + a + "'";
            pass;
        if o in ("-2", "--stderr"):
            print "Received stderr '" + a + "'";
            pass;
        elif o in ("-C", "--chroot"):
            cfg.chroot = a;
        elif o in ("-c", "--config"):
            print "Received config '" + a + "'";
            pass;
        elif o in ("-G", "--gid"):
            print "Received gid '" + a + "'";
            pass;
        elif o in ("-h", "--help"):
            print_help();
            return 0;
        elif o in ("-L", "--license"):
            print_license();
            return 0;
        elif o == "--no-detach":
            cfg.detach = False;
        elif o == "--print-config":
            cfg.print_config = True;
        elif o in ("-U", "--uid"):
            print "Received uid '" + a + "'";
            pass;
        elif o in ("-u", "--umask"):
            cfg.umask = a;
        elif o in ("-V", "--version"):
            print_version();
            return 0;
        elif o in ("-v", "--verbose"):
            cfg.verbose = True;
        elif o in ("-W", "--workdir"):
            cfg.workdir = a;
    return 1;

if __name__ == "__main__":
    sys.exit(main(sys.argv));

