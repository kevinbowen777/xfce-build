#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: purge_xfce_core.py
# Purpose: delete the local Xfce4 core repositories originally pulled from
#           https://gitlab.xfce.org/xfce
#
# version: 0.3
# updated: 20210130
# @author: kevin.bowen@gmail.com
#
# ---------------------------------------------------------------------- #


import os

xfce_core_list = ['exo', 'garcon', 'libxfce4ui', 'libxfce4util',
                   'thunar', 'thunar-volman', 'tumbler',
                   'xfce4-appfinder', 'xfce4-dev-tools',
                   'xfce4-panel', 'xfce4-power-manager', 'xfce4-session',
                   'xfce4-settings', 'xfconf', 'xfdesktop', 'xfwm4']

confirm = input('Are you sure you want to remove the Xfce core repos? ')
if confirm.lower() == 'yes':
    for item in xfce_core_list:
        os.system('rm -rf ../core/' + item)
        print("The " + item + " Xfce core repo has been purged.")
    os.system('rmdir ../core/')
    print('The core directory has been deleted.')
else:
    print("No repositories have been deleted. Have a nice day.")
