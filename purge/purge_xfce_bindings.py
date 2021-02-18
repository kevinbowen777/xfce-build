#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: purge_xfce_bindings.py
# Purpose: delete the local Xfce bindings repositories originally pulled from
#           https://gitlab.xfce.org/bindings
#
# version: 0.6
# updated: 20210218
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import os
import shutil
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from packages.repo_arrays import xfce_bindings_list
from packages.query import query_yes_no
from packages.repodir import repodir


repopath = repodir('bindings')
os.chdir(currentdir)

confirm = query_yes_no('Are you sure you want to remove the Xfce bindings '
                       'repositories? ')
if confirm == 'yes':
    for item in xfce_bindings_list:
        filePath = (repopath + item)
        try:
            shutil.rmtree(filePath)
            print(item + ' directory has been deleted.')
        except ValueError:
            print("Error while deleting", item + " directory.")
    try:
        shutil.rmtree(repopath)
        print('The bindings directory has been deleted.')
    except ValueError:
        print("Error while deleting bindings directory.")
else:
    print("No repositories have been deleted. Have a nice day.")
