#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
'''
[:] File: login_support.py
[:] Function: Support the login gui, stores variables and send them off
[:] Author: Harry Hegarty
[:] NEA Information:
    [Center Number]: 52221
    [Candidate Number]: 4062
'''


import sys
import loginHandler
import registerUserGUI

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def set_Tk_var():
    global usrVar
    usrVar = StringVar()
    global pswVar
    pswVar = StringVar()

def exportVars():
    userVar = (usrVar.get())
    passVar = (pswVar.get())
    loginHandler.importVars(userVar, passVar)
    sys.stdout.flush()

def registerUser():
    registerUserGUI.vp_start_gui()
    sys.stdout.flush()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import login
    login.vp_start_gui()

