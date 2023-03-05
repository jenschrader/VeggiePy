# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 14:08:26 2022

@author: JenSc
"""


###############################################################################

# =============================================================================
# *-- CONSOLE CLASS --*
# *************************************
# console class for python interpreter in text widget
# found from stackoverflow below:
# https://stackoverflow.com/questions/21811464/how-can-i-embed-a-python-interpreter-frame-in-python-using-tkinter
# *************************************

# =============================================================================
# *-- imports --*

import tkinter as tk
import subprocess
import queue
import os
from threading import Thread

# =============================================================================
# code


class Console(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(
            self,
            parent,
            text='console',
            bg='#0a0a0a',
            fg='white',
            font=('Silkscreen', 14, 'bold'))
        self.parent = parent
        self.createWidgets()

        # get the path to the console.py file assuming it is in the same folder
        consolePath = os.path.join(os.path.dirname(__file__), "console.py")
        # open the console.py file (replace the path to python with the correct one for your system)
        # e.g. it might be "C:\\Python35\\python"
        self.p = subprocess.Popen(["C:/Users/JenSc/AppData/Local/Programs/Python/Python310/python.exe", consolePath],
                                  stdout=subprocess.PIPE,
                                  stdin=subprocess.PIPE,
                                  stderr=subprocess.PIPE)

        # make queues for keeping stdout and stderr whilst it is transferred between threads
        self.outQueue = queue.Queue()
        self.errQueue = queue.Queue()

        # keep track of where any line that is submitted starts
        self.line_start = 0

        # make the enter key call the self.enter function
        self.ttyText.bind("<Return>",self.enter)

        # a daemon to keep track of the threads so they can stop running
        self.alive = True
        # start the functions that get stdout and stderr in separate threads
        Thread(target=self.readFromProccessOut).start()
        Thread(target=self.readFromProccessErr).start()

        # start the write loop in the main thread
        self.writeLoop()

    def destroy(self):
        "This is the function that is automatically called when the widget is destroyed."
        self.alive=False
        # write exit() to the console in order to stop it running
        self.p.stdin.write("exit()\n".encode())
        self.p.stdin.flush()
        # call the destroy methods to properly destroy widgets
        self.ttyText.destroy()
        tk.Frame.destroy(self)
        
    def enter(self,e):
        "The <Return> key press handler"
        print(self.line_start)
        string = self.ttyText.get(1.0, tk.END)[self.line_start:]
        self.line_start+=len(string)
        # self.line_start -= 1
            
        print(self.line_start)
        self.p.stdin.write(string.encode())
        self.p.stdin.flush()

    def readFromProccessOut(self):
        "To be executed in a separate thread to make read non-blocking"
        while self.alive:
            data = self.p.stdout.raw.read(1024).decode()
            self.outQueue.put(data)

    def readFromProccessErr(self):
        "To be executed in a separate thread to make read non-blocking"
        while self.alive:
            data = self.p.stderr.raw.read(1024).decode()
            self.errQueue.put(data)

    def writeLoop(self):
        "Used to write data from stdout and stderr to the Text widget"
        # if there is anything to write from stdout or stderr, then write it
        if not self.errQueue.empty():
            self.write(self.errQueue.get())
        if not self.outQueue.empty():
            self.write(self.outQueue.get())

        # run this method again after 10ms
        if self.alive:
            self.after(10,self.writeLoop)

    def write(self,string):
        self.ttyText.insert(tk.END, string)
        self.ttyText.see(tk.END)
        self.line_start+=len(string)
        print(self.line_start)

    def createWidgets(self):
        self.ttyText = tk.Text(
            self,
            bg='#0a0a0a',
            fg='white',
            font=('VT323', 18),
            bd=5,
            relief='ridge',
            insertbackground='white')
        self.ttyText.pack(side='right', fill=tk.BOTH, expand=True, padx=15)

    def run(self, string):
        self.ttyText.insert(tk.END, string)
        self.enter(None)




if __name__ == '__main__':
    root = tk.Tk()
    root.config(background="red")
    main_window = Console(root)
    main_window.pack(fill=tk.BOTH,expand=True)
    root.mainloop()









# =============================================================================


# *************************************


# *************************************

###############################################################################
