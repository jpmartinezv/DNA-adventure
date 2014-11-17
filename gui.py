#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.3.1
# In conjunction with Tcl version 8.6
#    Nov 16, 2014 07:33:45 PM
import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import gui_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    root.title('New_Toplevel_1')
    root.geometry('1500x450+350+150')
    w = New_Toplevel_1 (root)
    gui_support.init(root, w)
    root.mainloop()

w = None
def create_New_Toplevel_1 (root, param=None):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    w.title('New_Toplevel_1')
    w.geometry('600x450+650+150')
    w_win = New_Toplevel_1 (w)
    gui_support.init(w, w_win, param)
    return w_win

def destroy_New_Toplevel_1 ():
    global w
    w.destroy()
    w = None

import multibox

class New_Toplevel_1:
    def __init__(self, master=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 


        self.MultiListBox1 = multibox.MultiListbox(master, (('ID', 7), ('Nombre', 10), ('Secuencia', 10)))
        self.MultiListBox1.place(relx=0.03,rely=0.11,relheight=0.56,relwidth=0.26)
        self.MultiListBox1.configure(background="white")
        self.MultiListBox1.configure(width=154)
        
        """
        self.Listbox1 = Listbox (master)
        self.Listbox1.place(relx=0.03,rely=0.11,relheight=0.56,relwidth=0.26)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(font="TkFixedFont")
        self.Listbox1.configure(width=154)
        """

        self.Text1 = Text (master)
        self.Text1.place(relx=0.33,rely=0.11,relheight=0.15,relwidth=0.63)
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(width=376)

        self.Text2 = Text (master)
        self.Text2.place(relx=0.33,rely=0.31,relheight=0.15,relwidth=0.63)
        self.Text2.configure(background="white")
        self.Text2.configure(font="TkTextFont")
        self.Text2.configure(selectbackground="#c4c4c4")
        self.Text2.configure(width=376)

        self.Text3 = Text (master)
        self.Text3.place(relx=0.33,rely=0.51,relheight=0.15,relwidth=0.63)
        self.Text3.configure(background="white")
        self.Text3.configure(font="TkTextFont")
        self.Text3.configure(selectbackground="#c4c4c4")
        self.Text3.configure(width=376)

        self.Label1 = Label (master)
        self.Label1.place(relx=0.08,rely=0.04,height=19,width=92)
        self.Label1.configure(text='''Lista de MOTIF''')

        self.Label2 = Label (master)
        self.Label2.place(relx=0.35,rely=0.07,height=19,width=78)
        self.Label2.configure(text='''Secuencia 1''')

        self.Label3 = Label (master)
        self.Label3.place(relx=0.35,rely=0.27,height=19,width=78)
        self.Label3.configure(text='''Secuencia 2''')

        self.Label4 = Label (master)
        self.Label4.place(relx=0.35,rely=0.47,height=19,width=78)
        self.Label4.configure(text='''Secuencia 3''')

        self.Label5 = Label (master)
        self.Label5.place(relx=0.07,rely=0.71,height=19,width=73)
        self.Label5.configure(text='''% distancia''')

        self.Entry1 = Entry (master)
        self.Entry1.place(relx=0.25,rely=0.71,relheight=0.05,relwidth=0.24)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")

        self.Label6 = Label (master)
        self.Label6.place(relx=0.02,rely=0.78,height=19,width=136)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(text='''radio de conservacion''')

        self.Entry2 = Entry (master)
        self.Entry2.place(relx=0.25,rely=0.84,relheight=0.05,relwidth=0.24)
        self.Entry2.configure(background="white")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(selectbackground="#c4c4c4")

        self.Entry3 = Entry (master)
        self.Entry3.place(relx=0.25,rely=0.78,relheight=0.05,relwidth=0.24)
        self.Entry3.configure(background="white")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(selectbackground="#c4c4c4")

        self.Label7 = Label (master)
        self.Label7.place(relx=0.05,rely=0.84,height=19,width=98)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(text='''% conservacion''')

        self.Procesar = Button (master)
        self.Procesar.place(relx=0.57,rely=0.71,height=87,width=237)
        self.Procesar.configure(activebackground="#d9d9d9")
        self.Procesar.configure(text='''Procesar''')
        self.Procesar.configure(width=237)





if __name__ == '__main__':
    vp_start_gui()



