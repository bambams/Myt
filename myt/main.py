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
import getopt;
import myt.config;
import sys;

EXIT_FAILURE = -1;
EXIT_SUCCESS = 0;

def assert_recipients_unset(cfg):
    """Assert that primary recipients are unset.

    If the recipients are set already then we have too many recipients arguments
    and need to asplode.
    """;
    if cfg.recipient != None:
        raise CmdLineOptionError(msg="Too many recipients arguments.");

def main(argv):
    """The main routine for the Myt client.
    """;
    status, cfg = parse_args(argv);
    if status < 0:
        sys.exit(EXIT_FAILURE);
    elif status == 0:
        sys.exit(EXIT_SUCCESS);
    cfg.load();
    if cfg.print_config:
        print cfg;
        sys.exit(EXIT_SUCCESS);
    if cfg.interactive:
        print "Interactive mode activated.";
    return EXIT_SUCCESS;

def parse_args(argv):
    """Parse Myt client command-line arguments.
    """;
    opts = "B:C:c:H:hiLM:P:R:T:U:Vv";
    longopts = ["bcc", "cc", "config", "host", "help", "interactive",
                "license", "message", "password", "print-config",
                "recipients", "to", "user", "version", "verbose"];
    status = 1;
    cfg = myt.config.Config();
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

  myt is the client application for the Myt project, an attempt to offer
  secure E-mail and chat services in an open way.

    myt [ -B BCC | --bcc=BCC ] [ -C CC | -cc=CC ] [ -c FILE | --config=FILE ]
          [ -H HOST | --host=HOST ] [ -i | --interactive ]
          [ -M MESSAGE | --message=MESSAGE ]
          [ -P PASSWORD | --password=PASSWORD ] [ --print-config ]
          [ -R RECIPIENTS | --recipients=RECIPIENTS
              | -T RECIPIENTS | --to=RECIPIENTS ] [ -U USER | --user=USER ]
          [ -v | --verbose ]
    myt [ -h | --help ]
    myt [ -L | --license ]
    myt [ -V | --version ]

  -B, --bcc=BCC
      A semi-colon (;) delimited list of one or more recipients that will be
      sent a blind carbon-copy of the message. Contrary to conventional
      E-mail, no trace of them will be sent to other recipients.

  -C, --cc=CC
      A semi-colon (;) delimited list of one or more recipients that will be
      sent a carbon-copy of the message.

  -c, --config=FILE
      Specify a config file instead of the default.

  -H, --host=HOST
      The host server to use.

  -h, --help
      Print this message and exit.

  -i, --interactive
      Run in interactive mode.

  -L, --license
      Print the software license and exit.

  -M, --message=MESSAGE
      Specifies the message to send.

  --non-interactive
      Override interactive option.

  -P, --password=PASSWORD
      The user's password used to authenticate with the host. If this option
      is not supplied (recommended) then you will be prompted.

  --print-config
      Load configuration settings from the command-line and configuration file
      and print them to standard output.

  -R, --recipients=RECIPIENTS
      A semi-colon (;) delimited list of the primary recipients of the
      message.

  -T, --to=RECIPIENTS
      An alias for --recipients.

  -U, --user=USER
      The user name used to authenticate with the host.

  -V, --version
      Print the software version and exit.

  -v, --verbose
      Be verbose.
""";

def print_license():
    """Write the software license to stdout.
    """;
    print """
Myt is a secure messaging system composed of E-mail and chat facilities.
Copyright (C) 2009 Brandon McCaig, Samuel Henderson

This file is part of Myt.

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
    """Process Myt client command-line options.
    """;
    for o, a in optlist:
        if o in ("-B", "--bcc"):
            pass;
        elif o in ("-C", "--cc"):
            pass;
        elif o in ("-c", "--config"):
            pass;
        elif o in ("-H", "--host"):
            pass;
        elif o in ("-h", "--help"):
            print_help();
            return 0;
        elif o in ("-i", "--interactive"):
            pass;
        elif o in ("-L", "--license"):
            print_license();
            return 0;
        elif o in ("-M", "--message"):
            pass;
        elif o == "--non-interactive":
            pass;
        elif o in ("-P", "--password"):
            pass;
        elif o == "--print-config":
            cfg.print_config = True;
        elif o in ("-R", "--recipients"):
            assert_recipients_unset(cfg);
        elif o in ("-T", "--to"):
            assert_recipients_unset(cfg);
        elif o in ("-U", "--user"):
            pass;
        elif o in ("-V", "--version"):
            print_version();
            return 0;
        elif o in ("-v", "--verbose"):
            cfg.verbose = True;
    return 1;

if __name__ == "__main__":
    sys.exit(main(sys.argv));

