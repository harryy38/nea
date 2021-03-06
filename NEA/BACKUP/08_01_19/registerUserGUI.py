#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.17
# In conjunction with Tcl version 8.6
#    Jan 07, 2019 05:08:44 PM GMT  platform: Windows NT

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

        self.PasswordLabel = ttk.Label(self.LoginFrame)
        self.PasswordLabel.place(relx=0.3, rely=0.288, height=19, width=116)
        self.PasswordLabel.configure(background="#DB2222")
        self.PasswordLabel.configure(foreground="#FFFFFF")
        self.PasswordLabel.configure(font=font10)
        self.PasswordLabel.configure(relief=FLAT)
        self.PasswordLabel.configure(justify=CENTER)
        self.PasswordLabel.configure(text='''Full Name:''')
        self.PasswordLabel.configure(width=116)

        self.PasswordEntry = ttk.Entry(self.LoginFrame)
        self.PasswordEntry.place(relx=0.513, rely=0.288, relheight=0.029
                , relwidth=0.208)
        self.PasswordEntry.configure(font=font9)
        self.PasswordEntry.configure(textvariable=register_support.fullNameVar)
        self.PasswordEntry.configure(takefocus="")
        self.PasswordEntry.configure(cursor="ibeam")

        self.fra40_tLa42 = ttk.Label(self.LoginFrame)
        self.fra40_tLa42.place(relx=0.25, rely=0.014, height=151, width=416)
        self.fra40_tLa42.configure(background="#DB2222")
        self.fra40_tLa42.configure(foreground="#000000")
        self.fra40_tLa42.configure(font="TkDefaultFont")
        self.fra40_tLa42.configure(relief=FLAT)
        self.fra40_tLa42.configure(text='''MadDiceGame''')
        self.fra40_tLa42.configure(width=416)
        self._img1 = PhotoImage(file="ico/logo.png")
        self.fra40_tLa42.configure(image=self._img1)

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

        self.PasswordLabel_1 = ttk.Label(self.LoginFrame)
        self.PasswordLabel_1.place(relx=0.3, rely=0.329, height=19, width=116)
        self.PasswordLabel_1.configure(background="#DB2222")
        self.PasswordLabel_1.configure(foreground="#FFFFFF")
        self.PasswordLabel_1.configure(font=font10)
        self.PasswordLabel_1.configure(relief=FLAT)
        self.PasswordLabel_1.configure(justify=CENTER)
        self.PasswordLabel_1.configure(text='''Email:''')

        self.PasswordEntry_2 = ttk.Entry(self.LoginFrame)
        self.PasswordEntry_2.place(relx=0.513, rely=0.329, relheight=0.029
                , relwidth=0.208)
        self.PasswordEntry_2.configure(font=font9)
        self.PasswordEntry_2.configure(textvariable=register_support.emailVar)
        self.PasswordEntry_2.configure(takefocus="")
        self.PasswordEntry_2.configure(cursor="ibeam")

        self.PasswordLabel_2 = ttk.Label(self.LoginFrame)
        self.PasswordLabel_2.place(relx=0.3, rely=0.37, height=19, width=116)
        self.PasswordLabel_2.configure(background="#DB2222")
        self.PasswordLabel_2.configure(foreground="#FFFFFF")
        self.PasswordLabel_2.configure(font=font10)
        self.PasswordLabel_2.configure(relief=FLAT)
        self.PasswordLabel_2.configure(justify=CENTER)
        self.PasswordLabel_2.configure(text='''Password:''')

        self.PasswordEntry_3 = ttk.Entry(self.LoginFrame)
        self.PasswordEntry_3.place(relx=0.513, rely=0.37, relheight=0.029
                , relwidth=0.208)
        self.PasswordEntry_3.configure(font=font9)
        self.PasswordEntry_3.configure(textvariable=register_support.passwordVar)
        self.PasswordEntry_3.configure(takefocus="")
        self.PasswordEntry_3.configure(cursor="ibeam")

        self.PasswordLabel_3 = ttk.Label(self.LoginFrame)
        self.PasswordLabel_3.place(relx=0.3, rely=0.411, height=19, width=156)
        self.PasswordLabel_3.configure(background="#DB2222")
        self.PasswordLabel_3.configure(foreground="#FFFFFF")
        self.PasswordLabel_3.configure(font=font10)
        self.PasswordLabel_3.configure(relief=FLAT)
        self.PasswordLabel_3.configure(justify=CENTER)
        self.PasswordLabel_3.configure(text='''Confirm Password:''')
        self.PasswordLabel_3.configure(width=156)

        self.PasswordEntry_4 = ttk.Entry(self.LoginFrame)
        self.PasswordEntry_4.place(relx=0.513, rely=0.411, relheight=0.029
                , relwidth=0.208)
        self.PasswordEntry_4.configure(font=font9)
        self.PasswordEntry_4.configure(textvariable=register_support.confPasswordVar)
        self.PasswordEntry_4.configure(width=166)
        self.PasswordEntry_4.configure(takefocus="")
        self.PasswordEntry_4.configure(cursor="ibeam")

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


