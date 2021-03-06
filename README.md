[![License](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://gitlab.com/kevinbowen/xfce-repocapp/-/blob/master/LICENSE)

# Xfce-repocapp

repocapp - repository (C)lone (A)utogen (P)ull (P)urge
              (This also includes clean & installation scripts)

A collection of scripts to maintain local Xfce repositories.

The purpose of the scripts contained in the xfce-repocapp repository is to
facilitate managing your local Xfce repositories in bulk.
Cloning, running automake, installing, purging and updating tasks are
performed in groups, organized by categories, according to the official
Xfce repository structure (https://gitlab.xfce.org).

xfce-repocapp.sh provides a rudimentary menu-driven option to run the scripts.
    This is entirely optional. All of the scripts can be independently.


----
### Clone scripts

        Clone Xfce repositories from https://gitlab.xfce.org

 - clone_xfce_all.py
 - clone_xfce_apps.py
 - clone_xfce_bindings.py
 - clone_xfce_core.py
 - clone_xfce_panel_plugins.py
 - clone_xfce_thunar_plugins.py
 - clone_xfce_www.py

----
### Autogen (Build) scripts

        Run autogen & make against local component repositories

**N.B.: These scripts perform _NO_ checks for missing system libraries or the
order of component compilation. It is assumed that you know what you are
doing. Use at your own risk. No guarantees.**

For additional information on building Xfce see: https://docs.xfce.org/xfce/building

 - build_xfce_all.py
 - build_xfce_apps.py
 - build_xfce_bindings.py
 - build_xfce_core.py
 - build_xfce_panel_plugins.py
 - build_xfce_template.py
 - build_xfce_thunar_plugins.py

----
### Pull (Update) scripts

         Update local component repositories with git pull

 - pull_xfce_all.py
 - pull_xfce_apps.py
 - pull_xfce_bindings.py
 - pull_xfce_core.py
 - pull_xfce_panel_plugins.py
 - pull_xfce_thunar_plugins.py
 - pull_xfce_www.py

----
### Purge scripts

        Delete local component repositories by category

 - purge_xfce_all.py
 - purge_xfce_apps.py
 - purge_xfce_core.py
 - purge_xfce_bindings.py
 - purge_xfce_panel_plugins.py
 - purge_xfce_thunar_plugins.py
 - purge_xfce_www.py

----

### Installation scripts

          Install components into local system with sudo make install

 - install_xfce_all.py
 - install_xfce_apps.py
 - install_xfce_bindings.py
 - install_xfce_core.py
 - install_xfce_panel_plugins.py
 - install_xfce_thunar_plugins.py

----

### Clean scripts

          Clean local component directories (make clean)

 - clean_xfce_all.py
 - clean_xfce_apps.py
 - clean_xfce_bindings.py
 - clean_xfce_core.py
 - clean_xfce_panel_plugins.py
 - clean_xfce_thunar_plugins.py

----

### Installation of xfce-build project

        git clone https://gitlab.com/kevinbowen/xfce-repocapp.git
        git clone https://github.com/kevinbowen777/xfce-repocapp.git

----
### Reporting Bugs

   Visit the [Issues page](https://gitlab.com/kevinbowen/xfce-repocapp/-/issues)
     to view currently open bug reports or open a new issue.
