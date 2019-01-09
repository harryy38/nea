#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
'''
[:] File: loginHandler.py
[:] Function: Login GUI
[:] Author: Harry Hegarty
[:] NEA Information:
    [Center Number]: 52221
    [Candidate Number]: 4062
'''


import sys

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

import login_support

def incorrectInfo():
    xsmax = 1

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tkinter.TopLevel()
    login_support.set_Tk_var()
    top = New_Toplevel (root)
    login_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    login_support.set_Tk_var()
    top = New_Toplevel (w)
    login_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Courier New} -size 11 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font9 = "-family {Courier New} -size 11 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("788x344+531+298")
        top.title("Mad Dice Game - v[0.1]")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")



        self.LoginFrame = Frame(top)
        self.LoginFrame.place(relx=-0.013, rely=0.0, relheight=1.04
                , relwidth=1.015)
        self.LoginFrame.configure(borderwidth="2")
        self.LoginFrame.configure(background="#db2222")
        self.LoginFrame.configure(highlightbackground="#d9d9d9")
        self.LoginFrame.configure(highlightcolor="black")
        self.LoginFrame.configure(width=800)

        self.UsernameEntry = ttk.Entry(self.LoginFrame)
        self.UsernameEntry.place(relx=0.463, rely=0.529, relheight=0.062
                , relwidth=0.208)
        self.UsernameEntry.configure(font=font10)
        self.UsernameEntry.configure(textvariable=login_support.usrVar)
        self.UsernameEntry.configure(takefocus="")
        self.UsernameEntry.configure(cursor="ibeam")

        self.UsernameLabel = ttk.Label(self.LoginFrame)
        self.UsernameLabel.place(relx=0.325, rely=0.529, height=19, width=86)
        self.UsernameLabel.configure(background="#DB2222")
        self.UsernameLabel.configure(foreground="#FFFFFF")
        self.UsernameLabel.configure(font=font9)
        self.UsernameLabel.configure(relief=FLAT)
        self.UsernameLabel.configure(text='''Username:''')

        self.PasswordLabel = ttk.Label(self.LoginFrame)
        self.PasswordLabel.place(relx=0.325, rely=0.618, height=19, width=86)
        self.PasswordLabel.configure(background="#DB2222")
        self.PasswordLabel.configure(foreground="#FFFFFF")
        self.PasswordLabel.configure(font=font9)
        self.PasswordLabel.configure(relief=FLAT)
        self.PasswordLabel.configure(justify=CENTER)
        self.PasswordLabel.configure(text='''Password:''')

        
        self.PasswordEntry = ttk.Entry(self.LoginFrame)
        self.PasswordEntry.place(relx=0.463, rely=0.618, relheight=0.062
                , relwidth=0.208)
        self.PasswordEntry.configure(font=font10)
        self.PasswordEntry.configure(textvariable=login_support.pswVar)
        self.PasswordEntry.configure(takefocus="")
        self.PasswordEntry.configure(cursor="ibeam")

        self.fra40_tLa42 = ttk.Label(self.LoginFrame)
        self.fra40_tLa42.place(relx=0.25, rely=0.029, height=151, width=416)
        self.fra40_tLa42.configure(background="#DB2222")
        self.fra40_tLa42.configure(foreground="#000000")
        self.fra40_tLa42.configure(font="TkDefaultFont")
        self.fra40_tLa42.configure(relief=FLAT)
        self.fra40_tLa42.configure(text='''MadDiceGame''')
        self.fra40_tLa42.configure(width=416)
        self._img1 = PhotoImage(file="ico/logo.png")
        self.fra40_tLa42.configure(image=self._img1)

        self.LoginButton = Button(self.LoginFrame)
        self.LoginButton.place(relx=0.325, rely=0.735, height=24, width=277)
        self.LoginButton.configure(activebackground="#600606")
        self.LoginButton.configure(activeforeground="white")
        self.LoginButton.configure(activeforeground="#000000")
        self.LoginButton.configure(background="#ffffff")
        self.LoginButton.configure(command=login_support.exportVars)
        self.LoginButton.configure(disabledforeground="#ffffff")
        self.LoginButton.configure(font=font9)
        self.LoginButton.configure(foreground="#db2222")
        self.LoginButton.configure(highlightbackground="#ffffff")
        self.LoginButton.configure(highlightcolor="black")
        self.LoginButton.configure(pady="0")
        self.LoginButton.configure(relief=FLAT)
        self.LoginButton.configure(text='''Login''')

        self.RegisterButton = Button(self.LoginFrame)
        self.RegisterButton.place(relx=0.325, rely=0.824, height=24, width=277)
        self.RegisterButton.configure(activebackground="#600606")
        self.RegisterButton.configure(activeforeground="white")
        self.RegisterButton.configure(activeforeground="#000000")
        self.RegisterButton.configure(background="#ffffff")
        self.RegisterButton.configure(command=login_support.registerUser)
        self.RegisterButton.configure(disabledforeground="#ffffff")
        self.RegisterButton.configure(font=font9)
        self.RegisterButton.configure(foreground="#db2222")
        self.RegisterButton.configure(highlightbackground="#ffffff")
        self.RegisterButton.configure(highlightcolor="black")
        self.RegisterButton.configure(pady="0")
        self.RegisterButton.configure(relief=FLAT)
        self.RegisterButton.configure(text='''Register''')

    @staticmethod
    def popup1(event, *args, **kwargs):
        Popupmenu1 = Menu(root, tearoff=0)
        Popupmenu1.configure(activebackground="#f9f9f9")
        Popupmenu1.configure(activeborderwidth="1")
        Popupmenu1.configure(activeforeground="black")
        Popupmenu1.configure(background="#d9d9d9")
        Popupmenu1.configure(borderwidth="1")
        Popupmenu1.configure(disabledforeground="#a3a3a3")
        Popupmenu1.configure(font="{Segoe UI} 9")
        Popupmenu1.configure(foreground="black")
        Popupmenu1.post(event.x_root, event.y_root)






if __name__ == '__main__':
    vp_start_gui()


