#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: clone_xfce_all.py
# Purpose: clone oll of the Xfce repositories from
#           https://gitlab.xfce.org/
#
# version: 0.6
# updated: 20210218
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #


import os
import subprocess
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
os.chdir(currentdir)


subprocess.call("clone_xfce_apps.py", shell=True)
subprocess.call("clone_xfce_bindings.py", shell=True)
subprocess.call("clone_xfce_core.py", shell=True)
subprocess.call("clone_xfce_panel_plugins.py", shell=True)
subprocess.call("clone_xfce_thunar_plugins.py", shell=True)
subprocess.call("clone_xfce_www.py", shell=True)
