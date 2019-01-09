#! /usr/bin/env python
#  -*- coding: utf-8 -*-

'''
[:] File: registerUserGUI.py
[:] Function: The GUI For registering
[:] Author: Harry Hegarty
[:] NEA Information:
    [Center Number]: 52221
    [Candidate Number]: 4062
'''


import sys
import register_support

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


def vp_start_gui():
    import register_support
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    register_support.set_Tk_var()
    top = New_Toplevel (root)
    register_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    register_support.set_Tk_var()
    top = New_Toplevel (w)
    register_support.init(w, top, *args, **kwargs)
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
        font10 = "-family {Courier New} -size 11 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Courier New} -size 11 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("786x383+645+180")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")



        self.LoginFrame = Frame(top)
        self.LoginFrame.place(relx=-0.013, rely=0.0, relheight=1.906
                , relwidth=1.018)
        self.LoginFrame.configure(borderwidth="2")
        self.LoginFrame.configure(background="#db2222")
        self.LoginFrame.configure(highlightbackground="#d9d9d9")
        self.LoginFrame.configure(highlightcolor="black")
        self.LoginFrame.configure(width=800)

        self.UsernameEntry = ttk.Entry(self.LoginFrame)
        self.UsernameEntry.place(relx=0.513, rely=0.247, relheight=0.029
                , relwidth=0.208)
        self.UsernameEntry.configure(font=font9)
        self.UsernameEntry.configure(textvariable=register_support.usernameVar)
        self.UsernameEntry.configure(takefocus="")
        self.UsernameEntry.configure(cursor="ibeam")

        self.UsernameLabel = ttk.Label(self.LoginFrame)
        self.UsernameLabel.place(relx=0.3, rely=0.247, height=19, width=86)
        self.UsernameLabel.configure(background="#DB2222")
        self.UsernameLabel.configure(foreground="#FFFFFF")
        self.UsernameLabel.configure(font=font10)
        self.UsernameLabel.configure(relief=FLAT)
        self.UsernameLabel.configure(text='''Username:''')

        self.FullNameLabel = ttk.Label(self.LoginFrame)
        self.FullNameLabel.place(relx=0.3, rely=0.288, height=19, width=116)
        self.FullNameLabel.configure(background="#DB2222")
        self.FullNameLabel.configure(foreground="#FFFFFF")
        self.FullNameLabel.configure(font=font10)
        self.FullNameLabel.configure(relief=FLAT)
        self.FullNameLabel.configure(justify=CENTER)
        self.FullNameLabel.configure(text='''Full Name:''')
        self.FullNameLabel.configure(width=116)

        
        self.FullNameEntry = ttk.Entry(self.LoginFrame)
        self.FullNameEntry.place(relx=0.513, rely=0.288, relheight=0.029
                , relwidth=0.208)
        self.FullNameEntry.configure(font=font9)
        self.FullNameEntry.configure(textvariable=register_support.fullNameVar)
        self.FullNameEntry.configure(takefocus="")
        self.FullNameEntry.configure(cursor="ibeam")

        self.fra40_tLa43 = ttk.Label(self.LoginFrame)
        self.fra40_tLa43.place(relx=0.25, rely=0.014, height=151, width=416)
        self.fra40_tLa43.configure(background="#DB2222")
        self.fra40_tLa43.configure(foreground="#000000")
        self.fra40_tLa43.configure(font="TkDefaultFont")
        self.fra40_tLa43.configure(relief=FLAT)
        self.fra40_tLa43.configure(text='''MadDiceGame''')
        self.fra40_tLa43.configure(width=416)
        self._img2 = PhotoImage(file="ico/logo.png")
        self.fra40_tLa43.configure(image=self._img2)

        self.RegisterButton = Button(self.LoginFrame)
        self.RegisterButton.place(relx=0.338, rely=0.466, height=24, width=277)
        self.RegisterButton.configure(activebackground="#600606")
        self.RegisterButton.configure(activeforeground="white")
        self.RegisterButton.configure(activeforeground="#000000")
        self.RegisterButton.configure(background="#ffffff")
        self.RegisterButton.configure(command=register_support.registerUser)
        self.RegisterButton.configure(disabledforeground="#ffffff")
        self.RegisterButton.configure(font=font10)
        self.RegisterButton.configure(foreground="#db2222")
        self.RegisterButton.configure(highlightbackground="#ffffff")
        self.RegisterButton.configure(highlightcolor="black")
        self.RegisterButton.configure(pady="0")
        self.RegisterButton.configure(relief=FLAT)
        self.RegisterButton.configure(text='''Register User''')

        self.EmailLabel = ttk.Label(self.LoginFrame)
        self.EmailLabel.place(relx=0.3, rely=0.329, height=19, width=116)
        self.EmailLabel.configure(background="#DB2222")
        self.EmailLabel.configure(foreground="#FFFFFF")
        self.EmailLabel.configure(font=font10)
        self.EmailLabel.configure(relief=FLAT)
        self.EmailLabel.configure(justify=CENTER)
        self.EmailLabel.configure(text='''Email:''')


        self.EmailLabel = ttk.Entry(self.LoginFrame)
        self.EmailLabel.place(relx=0.513, rely=0.329, relheight=0.029
                , relwidth=0.208)
        self.EmailLabel.configure(font=font9)
        self.EmailLabel.configure(textvariable=register_support.emailVar)
        self.EmailLabel.configure(takefocus="")
        self.EmailLabel.configure(cursor="ibeam")

        self.PasswordLabel = ttk.Label(self.LoginFrame)
        self.PasswordLabel.place(relx=0.3, rely=0.37, height=19, width=116)
        self.PasswordLabel.configure(background="#DB2222")
        self.PasswordLabel.configure(foreground="#FFFFFF")
        self.PasswordLabel.configure(font=font10)
        self.PasswordLabel.configure(relief=FLAT)
        self.PasswordLabel.configure(justify=CENTER)
        self.PasswordLabel.configure(text='''Password:''')

        self.PasswordEntry = ttk.Entry(self.LoginFrame)
        self.PasswordEntry.place(relx=0.513, rely=0.37, relheight=0.029
                , relwidth=0.208)
        self.PasswordEntry.configure(font=font9)
        self.PasswordEntry.configure(textvariable=register_support.passwordVar)
        self.PasswordEntry.configure(takefocus="")
        self.PasswordEntry.configure(cursor="ibeam")

        self.ConfPassLabel = ttk.Label(self.LoginFrame)
        self.ConfPassLabel.place(relx=0.3, rely=0.411, height=19, width=156)
        self.ConfPassLabel.configure(background="#DB2222")
        self.ConfPassLabel.configure(foreground="#FFFFFF")
        self.ConfPassLabel.configure(font=font10)
        self.ConfPassLabel.configure(relief=FLAT)
        self.ConfPassLabel.configure(justify=CENTER)
        self.ConfPassLabel.configure(text='''Confirm Password:''')
        self.ConfPassLabel.configure(width=156)

        self.ConfPassEntry = ttk.Entry(self.LoginFrame)
        self.ConfPassEntry.place(relx=0.513, rely=0.411, relheight=0.029
                , relwidth=0.208)
        self.ConfPassEntry.configure(font=font9)
        self.ConfPassEntry.configure(textvariable=register_support.confPasswordVar)
        self.ConfPassEntry.configure(width=166)
        self.ConfPassEntry.configure(takefocus="")
        self.ConfPassEntry.configure(cursor="ibeam")

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


