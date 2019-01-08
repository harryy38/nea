#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.17
# In conjunction with Tcl version 8.6
#    Jan 07, 2019 04:55:25 PM GMT  platform: Windows NT

import sys
import loginHandler
import registerHandler

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
    registerHandler.launchGUI()
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

