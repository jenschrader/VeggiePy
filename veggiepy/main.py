# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 16:19:51 2022

@author: JenSc
"""


###############################################################################

# =============================================================================
# *-- FINAL PROJECT: VeggiePy --*
# *************************************
# USE: code editor
# FEATURES: text editing, runtime environment, syntax highlighting
# following youtube tutorials by Coding Lifestyle 4U,
# CodersLegacy
# console class for python interpreter in text widget
# https://stackoverflow.com/questions/21811464/how-can-i-embed-a-python-interpreter-frame-in-python-using-tkinter

# *************************************

# =============================================================================

# *-- imports --*
# *************************************
# import tkinter (all)
import console_class as console
import tkinter as tk

from tkinter import font
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import *
import subprocess

# *************************************


# =============================================================================
# *-- program --*
# TODO messy -- clean up
# *************************************


# *-- creating class --*
# *************************************
class VeggiePy():

    def __init__(self):

        # TODO change to custom tkinter, set up style
        # *-- window set up --*
        # *************************************
        self.main_window = tk.Tk()
        self.main_window.geometry('1270x670+120+60')
        self.main_window.title('VeggiePy')
        self.path = ''
        self.check = StringVar()
        self.check.set('dark')
        # self.my_count = IntVar()
        # *************************************

        # *-- change icon image for window --*
        # *************************************
        # create object of photoimage class
        icon_img = tk.PhotoImage(file='img/veg_ico.png')
        self.main_window.iconphoto(False, icon_img)

        # *************************************
        # *-- font --*
        # *************************************
        self.custom_font = tk.font.nametofont('TkDefaultFont')
        self.custom_font.config(family='VT323', size=12)
        self.font_style = 'VT323'
        self.new_font_size = 12
        self.font_size = 14

        # *************************************
        # *-- icons and images --*
        # *************************************
        # light
        # TODO add these to light theme
        self.file_icon = tk.PhotoImage(file='img/file_icon.png')
        self.newfile_icon = tk.PhotoImage(file='img/newfile_icon.png')
        self.openfile_icon = tk.PhotoImage(file='img/openfile_icon.png')
        self.savefile_icon = tk.PhotoImage(file='img/savefile_icon.png')
        self.saveas_icon = tk.PhotoImage(file='img/saveas_icon.png')
        self.quit_icon = tk.PhotoImage(file='img/quit_icon.png')
        self.undo_icon = tk.PhotoImage(file='img/undo_icon.png')
        self.redo_icon = tk.PhotoImage(file='img/redo_icon.png')
        self.copy_icon = tk.PhotoImage(file='img/copy_icon.png')
        self.paste_icon = tk.PhotoImage(file='img/paste_icon.png')
        self.cut_icon = tk.PhotoImage(file='img/cut_icon.png')
        self.find_icon = tk.PhotoImage(file='img/find_icon.png')
        self.run_icon = tk.PhotoImage(file='img/runfile_icon.png')
        # dark
        self.file_icon_w = tk.PhotoImage(file='img/file_icon_white.png')
        self.newfile_icon_w = tk.PhotoImage(file='img/newfile_icon_white.png')
        self.openfile_icon_w = tk.PhotoImage(file='img/openfile_icon_white.png')
        self.savefile_icon_w = tk.PhotoImage(file='img/save_icon_white.png')
        self.saveas_icon_w = tk.PhotoImage(file='img/saveas_icon_white.png')
        self.quit_icon_w = tk.PhotoImage(file='img/quit_icon_white.png')
        self.undo_icon_w = tk.PhotoImage(file='img/undo_icon_white.png')
        self.redo_icon_w = tk.PhotoImage(file='img/redo_icon_white.png')
        self.copy_icon_w = tk.PhotoImage(file='img/copy_icon_white.png')
        self.paste_icon_w = tk.PhotoImage(file='img/paste_icon_white.png')
        self.cut_icon_w = tk.PhotoImage(file='img/cut_icon_white.png')
        self.find_icon_w = tk.PhotoImage(file='img/find_icon_white.png')
        self.run_icon_w = tk.PhotoImage(file='img/runfile_icon_white.png')

        # *************************************
        # *-- menu set up --*
        # *************************************
        # !!!
        # this doesnt work on OS
        self.main_menu = tk.Menu(self.main_window, bg='#0a0a0a', fg='white')

        # file menu set up
        # make sure file menu can't be moved
        self.file_menu = tk.Menu(self.main_menu, tearoff=False, font=self.custom_font)

        # new file
        self.file_menu.add_command(
            label='new\n file...',
            accelerator='ctrl+n',
            command=self.new_file,
            image=self.newfile_icon_w,
            compound='left')

        # open file
        self.file_menu.add_command(
            label='open\n file...',
            accelerator='ctrl+o',
            command=self.open_file,
            image=self.openfile_icon_w,
            compound='left')

        # save file
        self.file_menu.add_command(
            label='save...',
            accelerator='ctrl+s',
            command=self.save_file,
            image=self.savefile_icon_w,
            compound='left')

        # save as
        self.file_menu.add_command(
            label='save as...',
            accelerator='ctrl+a',
            command=self.save_as,
            image=self.saveas_icon_w,
            compound='left')

        self.file_menu.add_separator()

        # quit
        self.file_menu.add_command(
            label='quit...',
            accelerator='ctrl+q',
            command=self.exit_veggie,
            image=self.quit_icon_w,
            compound='left')

        self.main_menu.add_cascade(label='file', menu=self.file_menu)

        # edit menu set up
        # TODO add redo/undo
        self.edit_menu = tk.Menu(self.main_menu, tearoff=False, font=self.custom_font)
        # # undo
        # self.edit_menu.add_command(
        #     label='undo...',
        #     accelerator='ctrl+z',
        #     image=self.undo_icon,
        #     compound='left', command=lambda: self.text_area.event_generate('<Control z>'))
        # # redo
        # self.edit_menu.add_command(
        #     label='redo...',
        #     accelerator='ctrl+y',
        #     image=self.redo_icon,
        #     compound='left', command=lambda: self.text_area.event_generate('<Control y>'))
        # self.edit_menu.add_separator()

        # cut
        self.edit_menu.add_command(
            label='cut\n...',
            accelerator='ctrl+x',
            image=self.cut_icon_w,
            compound='left',
            command=lambda: self.text_area.event_generate('<Control x>'))

        # copy
        self.edit_menu.add_command(
            label='copy\n...',
            accelerator='ctrl+c',
            image=self.copy_icon_w,
            compound='left',
            command=lambda: self.text_area.event_generate('<Control c>'))

        # paste
        self.edit_menu.add_command(
            label='paste\n...',
            accelerator='ctrl+v',
            image=self.paste_icon_w,
            compound='left',
            command=lambda: self.text_area.event_generate('<Control v>'))

        self.edit_menu.add_separator()

        # find
        self.edit_menu.add_command(
            label='find\n...',
            accelerator='ctrl+f',
            image=self.find_icon_w,
            compound='left',
            command=self.find_and_replace)

        self.main_menu.add_cascade(label='edit', menu=self.edit_menu)

        # theme menu set up
        # TODO add more themes
        self.theme_menu = tk.Menu(
            self.main_menu,
            tearoff=False,
            font=self.custom_font)

        # light theme
        self.theme_menu.add_radiobutton(
            label='light',
            variable=self.check,
            value='light',
            command=self.set_theme)

        # dark theme -- default
        self.theme_menu.add_radiobutton(
            label='dark',
            variable=self.check,
            value='dark',
            command=self.set_theme)

        self.main_menu.add_cascade(label='theme', menu=self.theme_menu)

        # clear menu set up
        self.clear_menu = tk.Menu(
            self.main_menu,
            tearoff=False,
            font=self.custom_font)

        self.clear_menu.add_command(label='clear all', command=self.clear_all)
        self.clear_menu.add_command(label='clear console', command=self.clear_output)
        self.main_menu.add_cascade(label='clear', menu=self.clear_menu)

        # # preferences menu set up
        # self.preferences_menu = tk.Menu(self.main_menu, tearoff=False, font=self.custom_font)
        # self.font_menu.add_check

        # run menu set up
        self.run_menu = tk.Menu(self.main_menu, tearoff=False, font=self.custom_font)

        self.run_menu.add_command(
            label='run code',
            command=self.run_code,
            image=self.run_icon_w,
            compound='left')

        self.main_menu.add_cascade(label='run', menu=self.run_menu)

        # user manual/help set up
        self.help_menu = tk.Menu(
            self.main_menu,
            tearoff=False,
            font=self.custom_font)

        self.help_menu.add_command(
            label='user manual',
            image=self.file_icon_w,
            compound='left',
            command=self.get_help)

        self.main_menu.add_cascade(label='help', menu=self.help_menu)

        # main menu config
        self.main_window.config(menu=self.main_menu)

        # *************************************

        # *-- tool bar set up --*
        # *************************************
        # TODO change placement/fix theme issue
        # create tool bar label
        self.tool_bar = tk.Label(self.main_window)
        self.tool_bar.pack(side='top', fill='x')

        # get fonts
        self.fonts = font.families()
        self.font_var = StringVar()

        # create combobox for font choices
        self.font_menu = tk.ttk.Combobox(
            self.tool_bar,
            width=30,
            values=self.fonts,
            state='readonly',
            textvariable=self.font_var)

        # set default font
        self.font_menu.current(self.fonts.index('VT323'))
        self.font_menu.grid(row=0, column=0)

        # create combobox for font size
        self.size_var = StringVar()

        self.font_size_menu = tk.ttk.Combobox(
            self.tool_bar,
            width=14,
            textvariable=self.size_var,
            state='readonly',
            values=tuple(range(8, 43)))

        # set default font size
        self.font_size_menu.current(4)
        self.font_size_menu.grid(row=0, column=1)

        # *-- status bar set up --*
        # TODO add functionality!!!
        # *************************************
        self.status_bar = tk.Label(
            self.main_window,
            text='status bar',
            font=self.custom_font)

        self.status_bar.pack(side='bottom', fill='x')
        # *************************************

        # *-- frame to hold editor/console --*
        # *************************************
        self.container_frame = tk.Frame(self.main_window)
        self.container_frame.pack(fill='both', expand=True)

        # *-- text editor set up --*
        # *************************************
        # frame for txt editor
        # !!!
        self.editor_frame = tk.LabelFrame(
            self.container_frame,
            text='code',
            font=('Silkscreen', 14, 'bold'))

        # frame placement
        # self.editor_frame.place(x=0, y=0, relheight=1, width=500)
        self.editor_frame.pack(
            side='left',
            fill='both',
            expand='true',
            padx=15)

        # create scrollbars
        self.scroll_bar_v1 = tk.Scrollbar(self.editor_frame, orient='vertical')
        self.scroll_bar_h1 = tk.Scrollbar(self.editor_frame, orient='horizontal')

        # place scrollbars
        self.scroll_bar_v1.pack(side='right', fill='y')
        self.scroll_bar_h1.pack(side='bottom', fill='x')

        # set up line number label
        self.line_numbers = tk.Text(
            self.editor_frame, width=3,
            font=('VT323', self.font_size),
            state='disabled',
            bg='white',
            fg='#0a0a0a',
            takefocus=0,
            bd=5,
            relief='ridge',
            yscrollcommand=self.scroll_bar_v1.set)

        self.line_numbers.pack(
            side='left',
            fill='both',
            expand=False,
            padx=10,
            ipady=10)

        # text set up
        self.text_area = tk.Text(
            self.editor_frame,
            font=('VT323', self.font_size),
            relief='ridge',
            bd=5,
            yscrollcommand=self.scroll_bar_v1.set,
            xscrollcommand=self.scroll_bar_h1.set)

        # tags for syntax highlighting
        self.text_area.tag_configure('red', foreground='#de6546')
        self.text_area.tag_configure('green', foreground='#8dc8a1')
        self.text_area.tag_configure('blue', foreground='#639bff')
        self.text_area.tag_configure('yellow', foreground='#e0aa71')
        self.text_area.tag_configure('pink', foreground='#ed9a9a')
        self.text_area.tag_configure('purple', foreground='#8d7be8')

        # tag name list
        self.tags = ['red', 'blue', 'green', 'purple', 'pink', 'yellow']

        # syntax list
        # TODO - maybe store these in txt files?
        self.syntax_list = [
            # keywords
            ['False', 'None', 'True', 'and',
             'as', 'assert', 'break', 'class',
             'continue', 'def', 'del', 'elif',
             'else', 'except', 'finally', 'for',
             'from', 'global', 'if', 'import',
             'in', 'is', 'lambda', 'nonlocal',
             'not', 'or', 'pass', 'raise',
             'return', 'try', 'while', 'with', 'yield'],
            # builtins
            ['abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray',
             'bytes', 'callable', 'chr', 'classmethod',
             'compile', 'complex', 'copyright', 'credits',
             'delattr', 'dict', 'dir', 'divmod', 'enumerate',
             'eval', 'exec', 'exit', 'filter', 'float', 'format',
             'frozenset', 'getattr', 'globals', 'hasattr',
             'hash', 'help', 'hex', 'id', 'input', 'int',
             'isinstance', 'issubclass', 'iter', 'len',
             'license', 'list', 'locals', 'map', 'max',
             'memoryview', 'min', 'next', 'object',
             'oct', 'open', 'ord', 'pow', 'print',
             'property', 'quit', 'range', 'repr',
             'reversed', 'round', 'set',
             'setattr', 'slice', 'sorted',
             'staticmethod', 'str', 'sum',
             'super', 'tuple', 'type', 'vars', 'zip'],
            # numbers
            ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
            # assignment operators
            ['=', '+=', '-=', '*=', '/=', '%=', '//=', '**=', '&=', '|=', '^=', '>>=', '<<='],
            # arthmetic operators
            ['+', '-', '*', '/', '%', '**', '//'],
            # comparison operators
            ['==', '!=', '>', '<', '>=', '<='],
            ]

        # txt area placement
        self.text_area.pack(
            side='left',
            fill='both',
            expand=True)

        # config
        self.scroll_bar_v1.config(command=self.dual_scrolling)
        self.scroll_bar_h1.config(command=self.text_area.xview)
        # *************************************

        #  *-- output frame set up --*
        # *************************************
        # old code
        # self.output_frame = tk.LabelFrame(
        #     self.container_frame,
        #     text='console',
        #     font=('Silkscreen', 14, 'bold'))

        self.output_frame = console.Console(self.container_frame)

        # place output frame
        self.output_frame.pack(
            side='right',
            fill='both',
            expand=True,
            padx=10)

        # //////////////////////////////////////////////////////////
        # old code
        # create scrollbars
        # self.scroll_bar_v2 = tk.Scrollbar(self.output_frame, orient='vertical')
        # self.scroll_bar_h2 = tk.Scrollbar(self.output_frame, orient='horizontal')
        # # place scrollbars
        # self.scroll_bar_v2.pack(side='right', fill='y')
        # self.scroll_bar_h2.pack(side='bottom', fill='x')
        # # text set up
        # self.output_area = tk.Text(
        #     self.output_frame,
        #     font=('VT323', self.font_size),
        #     bd=5,
        #     relief='ridge')
        # self.output_frame.createWidgets(self.output_area)
        # # # txt area placement
        # self.output_area.pack(side='right', fill='both', expand=True, padx=10)
        # # # config
        # self.scroll_bar_v2.config(command=self.output_area.yview)
        # self.scroll_bar_h2.config(command=self.output_area.xview)
        # //////////////////////////////////////////////////////////

        # event binding
        # FIXME -- change bindings for line numbering and syntax highlighting
        self.main_window.bind('<Control-n>', self.new_file)
        self.main_window.bind('<Control-o>', self.open_file)
        self.main_window.bind('<Control-s>', self.save_file)
        self.main_window.bind('<Control-q>', self.exit_veggie)
        self.main_window.bind('<Control-a>', self.save_as)

        # !!!
        for t in [self.text_area]:
            self.text_area.bind('<Return>', self.update_line_number, add='+')
            self.text_area.bind('<Any-KeyPress>', self.update_line_number, add='+')
            self.text_area.bind('<BackSpace>', self.update_line_number, add='+')

        self.font_menu.bind('<<ComboboxSelected>>', self.get_font_style)
        self.font_size_menu.bind('<<ComboboxSelected>>', self.get_font_size)
        self.text_area.bind('<MouseWheel>', self.mousewheel_moving)
        self.line_numbers.bind('<MouseWheel>', self.mousewheel_moving)
        # self.status_bar.bind('<Any-KeyPress>', self.update_status)
        # !!!
        self.text_area.bind('<Any-KeyPress>', self.syntax_highlight, add='+')

        self.text_area.bind('<Return>', self.auto_indent, add='+')
        

        # make dark theme default
        self.file_menu.config(bg='#0a0a0a', fg='white')
        self.theme_menu.config(bg='#0a0a0a', fg='white', selectcolor='white')
        self.clear_menu.config(bg='#0a0a0a', fg='white')
        self.edit_menu.config(bg='#0a0a0a', fg='white')
        # self.run_menu.config(bg='#0a0a0a', fg='white')
        self.container_frame.config(bg='#0a0a0a')
        # self.output_frame.config(bg='#0a0a0a', fg='white')
        self.text_area.config(bg='#0a0a0a', fg='white', insertbackground='white')
        # self.output_area.config(bg='#0a0a0a', fg='white')
        self.editor_frame.config(bg='#0a0a0a', fg='white')
        self.line_numbers.config(bg='#0a0a0a', fg='white')
        self.status_bar.config(bg='#0a0a0a', fg='white')
        self.tool_bar.config(bg='#0a0a0a', fg='white')
        self.run_menu.config(bg='#0a0a0a', fg='white')
        self.help_menu.config(bg='#0a0a0a', fg='white')

        tk.mainloop()
# =============================================================================

# =============================================================================
    # *-- creating functionality --*
    # *************************************
    # TODO add error handling

    # * -- file menu --*
    # *************************************

    # save as
    def save_as(self, event=None):
        self.path = tk.filedialog.asksaveasfilename(filetypes=[('Python Files', '*.py')], defaultextension=('.py'))
        if self.path != '':
            self.py_file = open(self.path, 'w')
            self.py_file.write(self.text_area.get(1.0, 'end'))
            self.py_file.close()

    # open file
    def open_file(self, event=None):

        self.path = tk.filedialog.askopenfilename(filetypes=[('Python Files', '*.py')], defaultextension=('.py'))
        if self.path != '':
            self.py_file = open(self.path, 'r')
            self.py_data = self.py_file.read()
            self.text_area.delete(1.0, 'end')
            self.text_area.insert(1.0, self.py_data)
            self.py_file.close()

    # save file
    def save_file(self, event=None):
        if self.path == '':
            self.save_as()
        else:
            self.py_file = open(self.path, 'w')
            self.py_file.write(self.text_area.get(1.0, 'end'))
            self.py_file.close()

    # new file
    def new_file(self, event=None):
        self.path = ''
        self.text_area.delete(1.0, 'end')
        # self.output_frame.delete(1.0, 'end')

    # exit program
    def exit_veggie(self, event=None):
        if self.text_area.edit_modified():
            self.save_answer = tk.messagebox.askyesnocancel('warning', 'do you want to save before quitting?')
            if self.save_answer == True:
                if self.path != '':
                    self.save_file()
                    self.main_window.destroy()
                else:
                    self.save_as()
                    self.main_window.destroy()
            elif self.save_answer == None:
                pass
            else:
                self.main_window.destroy()

        else:
            self.answer = tk.messagebox.askyesno('quit', 'are you sure you want to quit VeggiePy?')
            if self.answer:
                self.main_window.destroy()
            else:
                pass
    # *************************************

    # *-- theme menu --*
    # *************************************
    # TODO - change to style format, add more themes, change colors
    def set_theme(self):
        if self.check.get() == 'light':
            self.file_menu.config(bg='white', fg='#0a0a0a')
            self.theme_menu.config(bg='white', fg='#0a0a0a', selectcolor='#0a0a0a')
            self.clear_menu.config(bg='white', fg='#0a0a0a')
            self.run_menu.config(bg='white', fg='#0a0a0a')
            self.output_frame.config(bg='white', fg='#0a0a0a')
            self.text_area.config(bg='white', fg='#0a0a0a', insertbackground='#0a0a0a')
            # self.output_area.config(bg='white', fg='#0a0a0a')
            self.edit_menu.config(bg='white', fg='#0a0a0a')
            self.container_frame.config(bg='white')
            self.editor_frame.config(bg='white', fg='#0a0a0a')
            self.line_numbers.config(bg='white', fg='#0a0a0a')
            self.status_bar.config(bg='white', fg='#0a0a0a')
            self.tool_bar.config(bg='white', fg='#0a0a0a')
            self.run_menu.config(bg='white', fg='#0a0a0a')
            self.help_menu.config(bg='white', fg='#0a0a0a')

        if self.check.get() == 'dark':
            self.file_menu.config(bg='#0a0a0a', fg='white')
            self.theme_menu.config(bg='#0a0a0a', fg='white', selectcolor='white')
            self.clear_menu.config(bg='#0a0a0a', fg='white')
            self.edit_menu.config(bg='#0a0a0a', fg='white')
            # self.run_menu.config(bg='#0a0a0a', fg='white')
            self.container_frame.config(bg='#0a0a0a')
            self.output_frame.config(bg='#0a0a0a', fg='white')
            self.text_area.config(bg='#0a0a0a', fg='white', insertbackground='white')
            # self.output_area.config(bg='#0a0a0a', fg='white')
            self.editor_frame.config(bg='#0a0a0a', fg='white')
            self.line_numbers.config(bg='#0a0a0a', fg='white')
            self.status_bar.config(bg='#0a0a0a', fg='white')
            self.tool_bar.config(bg='#0a0a0a', fg='white')
            self.run_menu.config(bg='#0a0a0a', fg='white')
            self.help_menu.config(bg='#0a0a0a', fg='white')
    # *************************************

    # *-- help menu --*
    # *************************************
    def get_help(self):
        # make top lvl window for user manual
        self.help_window = tk.Toplevel()
        self.help_window.title('help')
        self.help_window.geometry('650x600+500+100')
        self.help_window.resizable(False, False)

        # container frame for layout
        self.window_container = tk.Frame(self.help_window, bg='#0a0a0a')
        self.window_container.pack(fill='both', expand=True)

        # set up label frame for user manual
        self.help_frame = tk.LabelFrame(
            self.window_container,
            text='user manual',
            font=('Silkscreen', 20, 'bold'),
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

        # menu item heading
        self.user_guide.tag_configure(
            'item',
            font=('Silkscreen', 15),
            foreground='white')

        # menu item description
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
        self.file_txt = '''
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
        # insert
        self.user_guide.insert(tk.END, '\n')
        self.user_guide.insert(tk.END, '\tHow to use VeggiePy', 'section')
        self.user_guide.insert(tk.END, self.intro, 'body')
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

        # place
        self.user_guide.pack(fill='both', expand=True, padx=20, pady=20)

        self.help_window.mainloop()
    # *************************************

    # * -- edit menu --*
    # *************************************

    # find function
    def find_word(self):
        # clear highlight of word
        self.text_area.tag_remove('found', 1.0, 'end')
        self.start_pos = '1.0'
        self.word = self.find_entry.get()

        # only run if word is entered in entry field
        if self.word:
            while True:
                self.start_pos = self.text_area.search(
                    self.word,
                    self.start_pos,
                    stopindex='end')

                # break loop if nothing found
                if not self.start_pos:
                    break
                self.end_pos = f'{self.start_pos} + {len(self.word)}c'

                # create tag for highlight
                self.text_area.tag_add('found', self.start_pos, self.end_pos)

                # config tag
                self.text_area.tag_config(
                    'found',
                    background='#9badb7',
                    foreground='#ac3232')
                # start searching after last found
                self.start_pos = self.end_pos

    # replace function
    def replace_word(self):
        self.word = self.find_entry.get()
        self.replace = self.replace_entry.get()
        self.selected = self.text_area.get(1.0, 'end')
        self.new_word = self.selected.replace(self.word, self.replace)
        self.text_area.delete(1.0, 'end')
        self.text_area.insert(1.0, self.new_word)

    # clear highlight function
    def clear_highlight(self):
        self.text_area.tag_remove('found', 1.0, 'end')
        self.second_window.destroy()

    def find_and_replace(self):

        # make top lvl window for search and find
        self.second_window = tk.Toplevel()
        self.second_window.title('find')
        self.second_window.geometry('400x200+600+300')
        self.second_window.resizable(0, 0)

        # make label frame
        self.find_labelframe = tk.LabelFrame(self.second_window, text='find & replace')

        # placement
        self.find_labelframe.pack()

        # labels
        self.find_label = tk.Label(self.find_labelframe, text='find')
        self.replace_label = tk.Label(self.find_labelframe, text='replace')

        # entry
        self.find_entry = tk.Entry(self.find_labelframe)
        self.replace_entry = tk.Entry(self.find_labelframe)

        # placement
        self.find_label.grid(row=0, column=0, padx=5, pady=5)
        self.replace_label.grid(row=1, column=0, padx=5, pady=5)
        self.find_entry.grid(row=0, column=1, padx=5, pady=5)
        self.replace_entry.grid(row=1, column=1, padx=5, pady=5)

        # create and place find button
        self.find_button = tk.Button(self.find_labelframe, text='find', command=self.find_word)
        self.find_button.grid(row=2, column=0, padx=5, pady=5)

        # create and place replace button
        self.replace_button = tk.Button(self.find_labelframe, text='replace', command=self.replace_word)
        self.replace_button.grid(row=2, column=1, padx=5, pady=5)

        # if window closed unhighlight found words
        self.second_window.protocol('WM_DELETE_WINDOW', self.clear_highlight)
        self.second_window.mainloop()
    # *************************************

    # *-- clear menu --*
    # *************************************
    # clear only output
    def clear_output(self):
        self.output_frame.destroy()
        self.output_frame = console.Console(self.container_frame)
        self.output_frame.pack(side='right', fill='both', expand=True, padx=10)

    # clear all of screen -- console & output
    def clear_all(self):
        self.text_area.delete(1.0, 'end')
        self.output_frame.destroy()
        self.output_frame = console.Console(self.container_frame)
        self.output_frame.pack(side='right', fill='both', expand=True, padx=10)
    # *************************************

    # *-- run --*
    # FIXME - make console output clearer, adjust theme, font size & style...
    # *************************************
    def run_code(self):
        try:
            if self.path == '':
                tk.messagebox.showerror('hold up', 'save the file first :)')
            else:
                self.run_command = f'python {self.path}'
                # shutil.copyfile(self.path, 'console.py')
                if self.path != '':
                    # self.py_file = open(self.path, 'r')
                    # self.py_data = self.py_file.read()
                    self.output_frame.run(f'exec(open(\'{self.path}\').read()) ')
                    self.output_frame.line_start -= 1

                self.run_file = subprocess.Popen(
                    self.run_command,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
                self.output, self.error = self.run_file.communicate()
                # self.output_frame.run()
                # self.container_frame.delete(1.0, 'end')
                # self.container_frame.insert(1.0, self.output)
                # self.container_frame.insert(1.0, self.error)

        except EOFError:
            pass

    # def get_input(self):

    # *************************************

    # *-- get current line number & display --*
    # FIXME -- numbers are janky
    # *************************************
    def get_line_num(self):
        self.line_output = ''
        self.row, self.col = self.text_area.index('end').split('.')
        for self.i in range(1, int(self.row)):
            self.line_output += str(self.i) + ('\n')
        return self.line_output

    # update number
    def update_line_number(self, event=None):
        self.current_num = self.get_line_num()
        self.line_numbers.config(state='normal')
        self.line_numbers.delete(1.0, 'end')
        self.line_numbers.insert(1.0, self.current_num)
        self.line_numbers.config(state='disabled')
    # ************************************

    # *-- connecting line number and text area scrolling --*
    # FIXME -- scroll bar doesn't move correctly w/ mousewheel
    # ************************************
    def dual_scrolling(self, *args):
        self.line_numbers.yview(*args)
        self.text_area.yview(*args)

    def mousewheel_moving(self, event):
        self.text_area.yview('scroll', event.delta, 'units')
        self.line_numbers.yview('scroll', event.delta, 'units')
        return 'break'

    # *-- get font --*
    # ************************************
    # font style
    def get_font_style(self, event):
        self.font_style = self.font_var.get()
        self.text_area.config(font=(self.font_style, self.new_font_size))
        self.line_numbers.config(font=(self.font_style, 12))
        self.output_frame.config(font=(self.font_style, 12))
        self.editor_frame.config(font=(self.font_style, 12))
        # self.output_area.config(font=(self.font_style, 12))

    # font size
    def get_font_size(self, event):
        self.new_font_size = self.size_var.get()
        self.text_area.config(font=(self.font_style, self.new_font_size))
    # *************************************

    # TODO -- status bar functionality
    # *-- get status--*
    # *************************************
    # def get_status(self):
    #     self.row_status = ''
    #     self.col_status = ''
    #     self.row, self.col = self.text_area.index('end').split('.')
    #     for self.i in range(1, int(self.row)):
    #         self.row_status += str(self.i) + ('\n')
    #     return self.row_status

    # def update_status(self, event=None):
    #     self.status = self.get_status()
    #     self.status_bar.config(state='normal')
    #     self.status_bar.delete(1.0, 'end')
    #     self.status_bar.insert(1.0, self.current_num)
    #     self.status_bar.config(state='disabled')

    # FIXME -- when opening a file, syntax highlight only appears after enter key pressed
    # *-- syntax highlighting --*
    # *************************************
    def syntax_highlight(self, event):
        # start var
        self.start_index = '1.0'
        # end var
        self.end_index = 'end'

        # highlight syntax
        for self.highlight_list in self.syntax_list:
            self.index_num = int(self.syntax_list.index(self.highlight_list))
            for self.word_in in self.highlight_list:
                self.text_area.mark_set('start_of_match', self.start_index)
                self.text_area.mark_set('end_of_match', self.start_index)
                self.text_area.mark_set('search_limiter', self.end_index)
                self.my_count = IntVar()
                while True:
                    index = self.text_area.search(
                        self.word_in,
                        'end_of_match',
                        'search_limiter',
                        count=self.my_count,
                        regexp=False)
                    if index == '':
                        break
                    if self.my_count.get() == 0:
                        break
                    self.text_area.mark_set('start_of_match', index)
                    self.text_area.mark_set('end_of_match', '%s+%sc' % (index, self.my_count.get()))
                    # self.text_area.tag_add(self.tags[self.index_num], 'start_of_match', 'end_of_match')
                    pre_index = '%s-%sc' % (index, 1)
                    post_index = '%s+%sc' % (index, self.my_count.get())
                    if self.check_word(index, pre_index, post_index):
                        self.text_area.tag_add(self.tags[self.index_num], 'start_of_match', 'end_of_match')

    def check_word(self, index, pre, post):
        self.letter_list = ['a', 'b', 'c', 'd',
                            'e', 'f', 'g', 'h',
                            'i', 'j', 'k', 'l',
                            'm', 'n', 'o', 'p',
                            'q', 'r', 's', 't',
                            'u', 'v', 'w', 'x',
                            'y', 'z']
        if self.text_area.get(index) == self.text_area.get(pre):
            pre = index
        else:
            if self.text_area.get(pre) in self.letter_list:
                return 0
        if self.text_area.get(post) in self.letter_list:
            return 0
        return 1
    # *************************************

    # *-- auto indent --*
    # *************************************
    def auto_indent(self, event):
        self.colon = ":"
        self.indent = 'hi'
        if self.text_area.get('1.0') == self.colon:
            self.text_area.insert('1.0', self.indent)
            
        else:
            pass

            
    # code

    # *************************************

    # *-- predictive txt --*
    # *************************************

    # code

    # *************************************

    # *-- auto complete --*
    # *************************************

    # code

    # *************************************

# =============================================================================


# *************************************
if __name__ == "__main__":
    VeggiePy()

# *************************************

###############################################################################
