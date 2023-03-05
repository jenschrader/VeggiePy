# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 17:09:43 2022

@author: JenSc
"""


###############################################################################

# =============================================================================
# *-- PROGRAM TITLE --*
# *************************************
# program description
# *************************************
# naming convention
# =============================================================================
import tkinter as tk
from tkinter import *

# =============================================================================
# code



# *-- help menu --*
# *************************************
class test():
    def __init__(self):
        

            # make top lvl window for user manual
            self.help_window = tk.Tk()
            self.help_window.title('help')
            self.help_window.geometry('650x600+600+300')
            self.help_window.resizable(False, False)
            
            # container frame for layout 
            self.window_container = tk.Frame(self.help_window, bg='#0a0a0a')
            self.window_container.pack(fill='both', expand=True)
            
            # set up label frame for user manual
            self.help_frame = tk.LabelFrame(
                self.window_container,
                text='user manual',
                font=('Silkscreen', 20,'bold'),
                background='#0a0a0a',
                foreground='white')
            self.help_frame.pack(fill='both', expand='true', padx=20, pady=20)
            
            # scroll bars
            self.scroll_y = tk.Scrollbar(self.help_frame, orient='vertical')
            self.scroll_x = tk.Scrollbar(self.help_frame, orient='horizontal')
            # place scroll
            self.scroll_y.pack(side='right', fill='y')
            self.scroll_x.pack(side='bottom', fill='x')
            # set up to display info
            # heading
            # self.heading = tk.Label(
            #     self.help_frame,
            #     text='how to use VeggiePy',
            #     font=('VT323 20'),
            #     background='#0a0a0a',
            #     foreground='white')
            # self.heading.pack(side='top')
            
            # info/howto
            self.user_guide = tk.Text(
                self.help_frame, 
                font=('VT323 12'), 
                background='#0a0a0a',
                relief='ridge',
                bd=5,
                yscrollcommand=self.scroll_y.set,
                xscrollcommand=self.scroll_x.set)
            
            # tags for formatting
            # section heading
            self.user_guide.tag_configure(
                'section',
                font=('Silkscreen', 18, 'bold'),
                foreground='white')
            
            # section body
            self.user_guide.tag_configure(
                'body',
                font=('VT323', 14),
                foreground='white')
            
            self.user_guide.tag_configure(
                'item',
                font=('Silkscreen', 15),
                foreground='white')
            
            self.user_guide.tag_configure(
                'description',
                font=('VT323', 14),
                foreground='white')
            
        
            # putting txt in variables
            self.intro = '''
    ***********************************************************
    *   VeggiePy is a code editor designed to                 *
    *   help you write Python code more efficiently.          *
    *   VeggiePy's interface includes a main menubar          *
    *   where you can find various drop-down menus for        *
    *   file management, editing, customizing,                *
    *   and running programs. This user manual will           *
    *   cover the 'how to' and 'where to find' of VeggiePy!   *
    ***********************************************************
    \n'''
            self.menubar_txt = '''
    ***********************************************************
    *   The main menubar hosts the File, Edit,                *
    *   Clear, Theme, Run, and Help drop-down menus.          *
    ***********************************************************
    \n'''
    
            self.line = '''
    ***********************************************************
    '''
            self.file_txt ='''
    * ------------------------------------------------------- *
    * new file      |   opens a new .py file                  *
    * ------------------------------------------------------- *
    * open file     |   opens an existing .py file            *
    * ------------------------------------------------------- *
    * save          |   saves a .py file                      *
    * ------------------------------------------------------- *
    * save as       |   saves a .py file with specified name  *
    * ------------------------------------------------------- *
    * quit          |   quits the program                     *
    * ------------------------------------------------------- *
    \n'''
            self.edit_txt = '''
    * ------------------------------------------------------- *
    * cut           |   cuts and copies the selected text     *
    * ------------------------------------------------------- *
    * copy          |   copies the selected text              *
    * ------------------------------------------------------- *
    * paste         |   pastes the copied text at insertion   *
    * ------------------------------------------------------- *
    * find          |  displays a pop-up window that allows   *
    *               |  you to search for an entered word,     *
    *               |  highlights all occurences, and then    *
    *               |  replaces all occurences of the word    *
    *               |  with the new word entered.             *
    * ------------------------------------------------------- *
    \n'''
    
            self.theme_txt = '''
    * ------------------------------------------------------- *
    * light         |   changes application to light mode     *
    * ------------------------------------------------------- *
    * dark          |   changes application to dark mode      *
    * ------------------------------------------------------- *
    \n'''
            self.clear_txt = '''
    * ------------------------------------------------------- *
    * clear all     |   clears entire text area               *
    *               |   and console area                      *
    * ------------------------------------------------------- *
    * clear console |   clears entire console area            *
    * ------------------------------------------------------- *
    \n'''
            self.run_txt = '''
    * ------------------------------------------------------- *
    * run code      |   runs code within text area            *
    *               |   and displays results to console.      *
    * ------------------------------------------------------- *
    \n'''
            self.help_txt = '''
    * ------------------------------------------------------- *
    * user manual   |   displays a pop-up window with the     *
    *               |   the user manual for VeggiePy.         *
    * ------------------------------------------------------- * 
    '''
            self.user_guide.insert(tk.END,'\n' )
            self.user_guide.insert(tk.END, '\tHow to use VeggiePy', 'section')
            self.user_guide.insert(tk.END, self.intro, 'body')
            
            # menu bar
            self.user_guide.insert(tk.END, '\tMenubar', 'section')
            self.user_guide.insert(tk.END, self.menubar_txt, 'body')
            self.user_guide.insert(tk.END, '\tFunctionality', 'section')
            self.user_guide.insert(tk.END, self.line, 'body')
            self.user_guide.insert(tk.END, '\n\tFile Menu', 'item')
            self.user_guide.insert(tk.END, self.file_txt, 'description')
            self.user_guide.insert(tk.END, '\n\tEdit Menu', 'item')
            self.user_guide.insert(tk.END, self.edit_txt, 'description')
            self.user_guide.insert(tk.END, '\n\tTheme Menu', 'item')
            self.user_guide.insert(tk.END, self.theme_txt, 'description')
            self.user_guide.insert(tk.END, '\n\tClear Menu', 'item')
            self.user_guide.insert(tk.END, self.clear_txt, 'description')
            self.user_guide.insert(tk.END, '\n\tRun Menu', 'item')
            self.user_guide.insert(tk.END, self.run_txt, 'description')
            self.user_guide.insert(tk.END, '\n\tHelp Menu', 'item')
            self.user_guide.insert(tk.END, self.help_txt, 'description')
            self.user_guide.insert(tk.END, self.line, 'body')
            
            
            
            self.user_guide.pack(fill='both', expand=True, padx=20, pady=20)
            
            
               
            
            
            
            self.help_window.mainloop()








# =============================================================================


# *************************************
if __name__ == "__main__":
    test()

# *************************************

###############################################################################
