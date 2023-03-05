# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 17:34:56 2022

@author: JenSc
"""

import code

   

if __name__ == '__main__':
    vars = globals().copy()
    vars.update(locals())
    shell = code.InteractiveConsole(vars)
    shell.interact() # -*- coding: utf-8 -*-
