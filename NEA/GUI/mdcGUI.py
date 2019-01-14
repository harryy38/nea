#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.17
# In conjunction with Tcl version 8.6
#    Jan 13, 2019 07:35:38 PM GMT  platform: Windows NT

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

import mdc_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    mdc_support.set_Tk_var()
    top = New_Toplevel (root)
    mdc_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    mdc_support.set_Tk_var()
    top = New_Toplevel (w)
    mdc_support.init(w, top, *args, **kwargs)
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

        top.geometry("1047x615+729+238")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")



        self.mainFrame = Frame(top)
        self.mainFrame.place(relx=-0.029, rely=-0.081, relheight=1.496
                , relwidth=1.309)
        self.mainFrame.configure(borderwidth="2")
        self.mainFrame.configure(background="#db2222")
        self.mainFrame.configure(highlightbackground="#d9d9d9")
        self.mainFrame.configure(highlightcolor="black")
        self.mainFrame.configure(width=1370)

        self.ScoreLabel = ttk.Label(self.mainFrame)
        self.ScoreLabel.place(relx=0.051, rely=0.685, height=19, width=136)
        self.ScoreLabel.configure(background="#DB2222")
        self.ScoreLabel.configure(foreground="#FFFFFF")
        self.ScoreLabel.configure(font=font9)
        self.ScoreLabel.configure(relief=FLAT)
        self.ScoreLabel.configure(justify=CENTER)
        self.ScoreLabel.configure(text='''Score Counter:''')

        self.fra40_tLa42 = ttk.Label(self.mainFrame)
        self.fra40_tLa42.place(relx=0.255, rely=0.011, height=151, width=406)
        self.fra40_tLa42.configure(background="#DB2222")
        self.fra40_tLa42.configure(foreground="#000000")
        self.fra40_tLa42.configure(font="TkDefaultFont")
        self.fra40_tLa42.configure(relief=FLAT)
        self.fra40_tLa42.configure(text='''FusionCopLogo''')
        self.fra40_tLa42.configure(width=406)
        self._img1 = PhotoImage(file="ico/logo.png")
        self.fra40_tLa42.configure(image=self._img1)

        self.LoginButton = Button(self.mainFrame)
        self.LoginButton.place(relx=0.051, rely=0.652, height=24, width=277)
        self.LoginButton.configure(activebackground="#600606")
        self.LoginButton.configure(activeforeground="white")
        self.LoginButton.configure(activeforeground="#000000")
        self.LoginButton.configure(background="#ffffff")
        self.LoginButton.configure(command=mdc_support.rollUserOne)
        self.LoginButton.configure(disabledforeground="#ffffff")
        self.LoginButton.configure(font=font9)
        self.LoginButton.configure(foreground="#db2222")
        self.LoginButton.configure(highlightbackground="#ffffff")
        self.LoginButton.configure(highlightcolor="black")
        self.LoginButton.configure(pady="0")
        self.LoginButton.configure(relief=FLAT)
        self.LoginButton.configure(text='''Roll (Player 1)''')

        self.RegisterButton = Button(self.mainFrame)
        self.RegisterButton.place(relx=0.555, rely=0.652, height=24, width=277)
        self.RegisterButton.configure(activebackground="#600606")
        self.RegisterButton.configure(activeforeground="white")
        self.RegisterButton.configure(activeforeground="#000000")
        self.RegisterButton.configure(background="#ffffff")
        self.RegisterButton.configure(command=mdc_support.rollUserTwo)
        self.RegisterButton.configure(disabledforeground="#ffffff")
        self.RegisterButton.configure(font=font9)
        self.RegisterButton.configure(foreground="#db2222")
        self.RegisterButton.configure(highlightbackground="#ffffff")
        self.RegisterButton.configure(highlightcolor="black")
        self.RegisterButton.configure(pady="0")
        self.RegisterButton.configure(relief=FLAT)
        self.RegisterButton.configure(text='''Roll (Player 2)''')

        self.errorInfo = ttk.Label(self.mainFrame)
        self.errorInfo.place(relx=0.175, rely=0.359, height=19, width=276)
        self.errorInfo.configure(background="#DB2222")
        self.errorInfo.configure(foreground="#DB2222")
        self.errorInfo.configure(font=font9)
        self.errorInfo.configure(relief=FLAT)
        self.errorInfo.configure(anchor=CENTER)
        self.errorInfo.configure(text='''Username/Password Incorrect''')

        self.scoreLabelP2 = ttk.Label(self.mainFrame)
        self.scoreLabelP2.place(relx=0.555, rely=0.685, height=19, width=136)
        self.scoreLabelP2.configure(background="#DB2222")
        self.scoreLabelP2.configure(foreground="#FFFFFF")
        self.scoreLabelP2.configure(font=font9)
        self.scoreLabelP2.configure(relief=FLAT)
        self.scoreLabelP2.configure(justify=CENTER)
        self.scoreLabelP2.configure(text='''Score Counter:''')

        self.scoreCounterP1 = ttk.Label(self.mainFrame)
        self.scoreCounterP1.place(relx=0.153, rely=0.685, height=19, width=136)
        self.scoreCounterP1.configure(background="#DB2222")
        self.scoreCounterP1.configure(foreground="#FFFFFF")
        self.scoreCounterP1.configure(font=font9)
        self.scoreCounterP1.configure(relief=FLAT)
        self.scoreCounterP1.configure(justify=CENTER)
        self.scoreCounterP1.configure(textvariable=mdc_support.scoreCounterP1)

        self.scoreCounterP2 = ttk.Label(self.mainFrame)
        self.scoreCounterP2.place(relx=0.657, rely=0.685, height=19, width=136)
        self.scoreCounterP2.configure(background="#DB2222")
        self.scoreCounterP2.configure(foreground="#FFFFFF")
        self.scoreCounterP2.configure(font=font9)
        self.scoreCounterP2.configure(relief=FLAT)
        self.scoreCounterP2.configure(justify=CENTER)
        self.scoreCounterP2.configure(textvariable=mdc_support.scoreCounterP1)

        self.roundCounterVar = ttk.Label(self.mainFrame)
        self.roundCounterVar.place(relx=0.35, rely=0.641, height=19, width=136)
        self.roundCounterVar.configure(background="#DB2222")
        self.roundCounterVar.configure(foreground="#FFFFFF")
        self.roundCounterVar.configure(font=font9)
        self.roundCounterVar.configure(relief=FLAT)
        self.roundCounterVar.configure(justify=CENTER)
        self.roundCounterVar.configure(textvariable=mdc_support.roundCount)

        self.ScoreLabel_6 = ttk.Label(self.mainFrame)
        self.ScoreLabel_6.place(relx=0.343, rely=0.62, height=19, width=166)
        self.ScoreLabel_6.configure(background="#DB2222")
        self.ScoreLabel_6.configure(foreground="#FFFFFF")
        self.ScoreLabel_6.configure(font=font9)
        self.ScoreLabel_6.configure(relief=FLAT)
        self.ScoreLabel_6.configure(justify=CENTER)
        self.ScoreLabel_6.configure(text='''Round:''')

        self.ScoreLabel_7 = ttk.Label(self.mainFrame)
        self.ScoreLabel_7.place(relx=0.358, rely=0.185, height=19, width=136)
        self.ScoreLabel_7.configure(background="#DB2222")
        self.ScoreLabel_7.configure(foreground="#FFFFFF")
        self.ScoreLabel_7.configure(font=font9)
        self.ScoreLabel_7.configure(relief=FLAT)
        self.ScoreLabel_7.configure(justify=CENTER)
        self.ScoreLabel_7.configure(text='''Roll Counter:''')

        self.roll1_1 = ttk.Label(self.mainFrame)
        self.roll1_1.place(relx=0.343, rely=0.217, height=41, width=46)
        self.roll1_1.configure(background="#dd2222")
        self.roll1_1.configure(foreground="#000000")
        self.roll1_1.configure(font="TkDefaultFont")
        self.roll1_1.configure(relief=FLAT)
        self.roll1_1.configure(text='''roll1_1''')
        self.roll1_1.configure(width=46)
        self._img2 = PhotoImage(file="ico/dd2222.png")
        self.roll1_1.configure(image=self._img2)

        self.roll2_1 = ttk.Label(self.mainFrame)
        self.roll2_1.place(relx=0.423, rely=0.217, height=41, width=46)
        self.roll2_1.configure(background="#dd2222")
        self.roll2_1.configure(foreground="#000000")
        self.roll2_1.configure(font="TkDefaultFont")
        self.roll2_1.configure(relief=FLAT)
        self.roll2_1.configure(text='''roll2_1''')
        self.roll2_1.configure(width=46)
        self._img3 = PhotoImage(file="ico/dd2222.png")
        self.roll2_1.configure(image=self._img3)

        self.roll1_2 = ttk.Label(self.mainFrame)
        self.roll1_2.place(relx=0.343, rely=0.272, height=41, width=46)
        self.roll1_2.configure(background="#dd2222")
        self.roll1_2.configure(foreground="#000000")
        self.roll1_2.configure(font="TkDefaultFont")
        self.roll1_2.configure(relief=FLAT)
        self.roll1_2.configure(text='''roll1_2''')
        self.roll1_2.configure(width=46)
        self._img4 = PhotoImage(file="ico/dd2222.png")
        self.roll1_2.configure(image=self._img4)

        self.roll2_2 = ttk.Label(self.mainFrame)
        self.roll2_2.place(relx=0.423, rely=0.272, height=41, width=46)
        self.roll2_2.configure(background="#dd2222")
        self.roll2_2.configure(foreground="#000000")
        self.roll2_2.configure(font="TkDefaultFont")
        self.roll2_2.configure(relief=FLAT)
        self.roll2_2.configure(text='''roll2_2''')
        self.roll2_2.configure(width=46)
        self._img5 = PhotoImage(file="ico/dd2222.png")
        self.roll2_2.configure(image=self._img5)

        self.roll1_3 = ttk.Label(self.mainFrame)
        self.roll1_3.place(relx=0.343, rely=0.326, height=41, width=46)
        self.roll1_3.configure(background="#dd2222")
        self.roll1_3.configure(foreground="#000000")
        self.roll1_3.configure(font="TkDefaultFont")
        self.roll1_3.configure(relief=FLAT)
        self.roll1_3.configure(text='''roll1_3''')
        self.roll1_3.configure(width=46)
        self._img6 = PhotoImage(file="ico/dd2222.png")
        self.roll1_3.configure(image=self._img6)

        self.roll2_3 = ttk.Label(self.mainFrame)
        self.roll2_3.place(relx=0.423, rely=0.326, height=41, width=46)
        self.roll2_3.configure(background="#dd2222")
        self.roll2_3.configure(foreground="#000000")
        self.roll2_3.configure(font="TkDefaultFont")
        self.roll2_3.configure(relief=FLAT)
        self.roll2_3.configure(text='''roll2_3''')
        self.roll2_3.configure(width=46)
        self._img7 = PhotoImage(file="ico/dd2222.png")
        self.roll2_3.configure(image=self._img7)

        self.roll1_4 = ttk.Label(self.mainFrame)
        self.roll1_4.place(relx=0.343, rely=0.38, height=41, width=46)
        self.roll1_4.configure(background="#dd2222")
        self.roll1_4.configure(foreground="#000000")
        self.roll1_4.configure(font="TkDefaultFont")
        self.roll1_4.configure(relief=FLAT)
        self.roll1_4.configure(text='''roll1_4''')
        self.roll1_4.configure(width=46)
        self._img8 = PhotoImage(file="ico/dd2222.png")
        self.roll1_4.configure(image=self._img8)

        self.roll2_4 = ttk.Label(self.mainFrame)
        self.roll2_4.place(relx=0.423, rely=0.38, height=41, width=46)
        self.roll2_4.configure(background="#dd2222")
        self.roll2_4.configure(foreground="#000000")
        self.roll2_4.configure(font="TkDefaultFont")
        self.roll2_4.configure(relief=FLAT)
        self.roll2_4.configure(text='''roll2_4''')
        self.roll2_4.configure(width=46)
        self._img9 = PhotoImage(file="ico/dd2222.png")
        self.roll2_4.configure(image=self._img9)

        self.roll1_5 = ttk.Label(self.mainFrame)
        self.roll1_5.place(relx=0.343, rely=0.435, height=41, width=46)
        self.roll1_5.configure(background="#dd2222")
        self.roll1_5.configure(foreground="#000000")
        self.roll1_5.configure(font="TkDefaultFont")
        self.roll1_5.configure(relief=FLAT)
        self.roll1_5.configure(text='''roll1_5''')
        self.roll1_5.configure(width=46)
        self._img10 = PhotoImage(file="ico/dd2222.png")
        self.roll1_5.configure(image=self._img10)

        self.roll2_5 = ttk.Label(self.mainFrame)
        self.roll2_5.place(relx=0.423, rely=0.435, height=41, width=46)
        self.roll2_5.configure(background="#dd2222")
        self.roll2_5.configure(foreground="#000000")
        self.roll2_5.configure(font="TkDefaultFont")
        self.roll2_5.configure(relief=FLAT)
        self.roll2_5.configure(text='''roll2_5''')
        self.roll2_5.configure(width=46)
        self._img11 = PhotoImage(file="ico/dd2222.png")
        self.roll2_5.configure(image=self._img11)

        self.roll1_6 = ttk.Label(self.mainFrame)
        self.roll1_6.place(relx=0.343, rely=0.489, height=41, width=46)
        self.roll1_6.configure(background="#dd2222")
        self.roll1_6.configure(foreground="#000000")
        self.roll1_6.configure(font="TkDefaultFont")
        self.roll1_6.configure(relief=FLAT)
        self.roll1_6.configure(text='''roll1_6''')
        self.roll1_6.configure(width=46)
        self._img12 = PhotoImage(file="ico/dd2222.png")
        self.roll1_6.configure(image=self._img12)

        self.roll2_6 = ttk.Label(self.mainFrame)
        self.roll2_6.place(relx=0.423, rely=0.489, height=41, width=46)
        self.roll2_6.configure(background="#dd2222")
        self.roll2_6.configure(foreground="#000000")
        self.roll2_6.configure(font="TkDefaultFont")
        self.roll2_6.configure(relief=FLAT)
        self.roll2_6.configure(text='''roll2_6''')
        self.roll2_6.configure(width=46)
        self._img13 = PhotoImage(file="ico/dd2222.png")
        self.roll2_6.configure(image=self._img13)

        self.roll1_7 = ttk.Label(self.mainFrame)
        self.roll1_7.place(relx=0.343, rely=0.543, height=41, width=46)
        self.roll1_7.configure(background="#dd2222")
        self.roll1_7.configure(foreground="#000000")
        self.roll1_7.configure(font="TkDefaultFont")
        self.roll1_7.configure(relief=FLAT)
        self.roll1_7.configure(text='''roll1_7''')
        self.roll1_7.configure(width=46)
        self._img14 = PhotoImage(file="ico/dd2222.png")
        self.roll1_7.configure(image=self._img14)

        self.roll2_7 = ttk.Label(self.mainFrame)
        self.roll2_7.place(relx=0.423, rely=0.543, height=41, width=46)
        self.roll2_7.configure(background="#dd2222")
        self.roll2_7.configure(foreground="#000000")
        self.roll2_7.configure(font="TkDefaultFont")
        self.roll2_7.configure(relief=FLAT)
        self.roll2_7.configure(text='''roll2_7''')
        self.roll2_7.configure(width=46)
        self._img15 = PhotoImage(file="ico/dd2222.png")
        self.roll2_7.configure(image=self._img15)

        self.currRoll_1 = ttk.Label(self.mainFrame)
        self.currRoll_1.place(relx=0.051, rely=0.217, height=261, width=276)
        self.currRoll_1.configure(background="#dbdbdb")
        self.currRoll_1.configure(foreground="#000000")
        self.currRoll_1.configure(font="TkDefaultFont")
        self.currRoll_1.configure(relief=FLAT)
        self.currRoll_1.configure(text='''roll1_1''')
        self.currRoll_1.configure(width=276)
        self._img16 = PhotoImage(file="ico/logo.png")
        self.currRoll_1.configure(image=self._img16)

        self.currRoll_2 = ttk.Label(self.mainFrame)
        self.currRoll_2.place(relx=0.555, rely=0.217, height=261, width=276)
        self.currRoll_2.configure(background="#dbdbdb")
        self.currRoll_2.configure(foreground="#000000")
        self.currRoll_2.configure(font="TkDefaultFont")
        self.currRoll_2.configure(relief=FLAT)
        self.currRoll_2.configure(text='''roll1_1''')
        self.currRoll_2.configure(width=276)
        self._img17 = PhotoImage(file="ico/logo.png")
        self.currRoll_2.configure(image=self._img17)

        self.ScoreLabel_1 = ttk.Label(self.mainFrame)
        self.ScoreLabel_1.place(relx=0.029, rely=0.065, height=19, width=136)
        self.ScoreLabel_1.configure(background="#DB2222")
        self.ScoreLabel_1.configure(foreground="#FFFFFF")
        self.ScoreLabel_1.configure(font=font9)
        self.ScoreLabel_1.configure(relief=FLAT)
        self.ScoreLabel_1.configure(justify=CENTER)
        self.ScoreLabel_1.configure(text='''CenNo: 52221''')

        self.ScoreLabel_8 = ttk.Label(self.mainFrame)
        self.ScoreLabel_8.place(relx=0.029, rely=0.087, height=19, width=136)
        self.ScoreLabel_8.configure(background="#DB2222")
        self.ScoreLabel_8.configure(foreground="#FFFFFF")
        self.ScoreLabel_8.configure(font=font9)
        self.ScoreLabel_8.configure(relief=FLAT)
        self.ScoreLabel_8.configure(justify=CENTER)
        self.ScoreLabel_8.configure(text='''CanNo: 4062''')

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

