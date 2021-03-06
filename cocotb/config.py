#!/usr/bin/env python
###############################################################################
# Copyright (c) 2013 Potential Ventures Ltd
# Copyright (c) 2013 SolarFlare Communications Inc
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of Potential Ventures Ltd,
#       SolarFlare Communications Inc nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL POTENTIAL VENTURES LTD BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
###############################################################################

"""
Module for querying the cocotb configuration

This module provides information in module global variables and through a
``main()`` function that is used in the cocotb-config script.

Global variables:
    share_dir: str, path where the cocotb data is stored
    makefiles_dir: str, path where the cocotb makefiles are installed
"""
import argparse
import os
import sys
import cocotb

__all__ = ["share_dir", "makefiles_dir"]


share_dir = os.path.join(os.path.dirname(cocotb.__file__), "share")
makefiles_dir = os.path.join(os.path.dirname(cocotb.__file__), "share", "makefiles")


class PrintAction(argparse.Action):
    def __init__(self, option_strings, dest, text=None, **kwargs):
        super(PrintAction, self).__init__(option_strings, dest, nargs=0, **kwargs)
        self.text = text

    def __call__(self, parser, namespace, values, option_string=None):
        print(self.text)
        parser.exit()


def get_parser():
    prefix_dir = os.path.dirname(os.path.dirname(cocotb.__file__))
    version = cocotb.__version__
    python_bin = sys.executable

    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        "--prefix",
        help="echo the package-prefix of cocotb",
        action=PrintAction,
        text=prefix_dir,
    )
    parser.add_argument(
        "--share",
        help="echo the package-share of cocotb",
        action=PrintAction,
        text=share_dir,
    )
    parser.add_argument(
        "--makefiles",
        help="echo the package-makefiles of cocotb",
        action=PrintAction,
        text=makefiles_dir,
    )
    parser.add_argument(
        "--python-bin",
        help="echo the path to the Python binary cocotb is installed for",
        action=PrintAction,
        text=python_bin,
    )
    parser.add_argument(
        "-v",
        "--version",
        help="echo the version of cocotb",
        action=PrintAction,
        text=version,
    )

    return parser


def main():
    parser = get_parser()

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()


if __name__ == "__main__":
    main()
