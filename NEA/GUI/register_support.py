#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
'''
[:] File: loginHandler.py
[:] Function: Support the register GUI, stores variables and passes them on
[:] Author: Harry Hegarty
[:] NEA Information:
    [Center Number]: 52221
    [Candidate Number]: 4062
'''

import sys
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
    global usernameVar
    usernameVar = StringVar()
    global fullNameVar
    fullNameVar = StringVar()
    global emailVar
    emailVar = StringVar()
    global passwordVar
    passwordVar = StringVar()
    global confPasswordVar
    confPasswordVar = StringVar()

def registerUser():
    usrVar = (usernameVar.get())
    pswVar = (passwordVar.get())
    confPswVar = (confPasswordVar.get())
    fnVar = (fullNameVar.get())
    emVar = (emailVar.get())
    registerHandler.newUser(usrVar, pswVar, confPswVar, fnVar, emVar)
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
    import register
    register.vp_start_gui()

