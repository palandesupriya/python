#
#	These are the path from where python modules are loaded.
#
>>> import sys
>>> print sys.path
['', 'C:\\Windows\\system32\\python27.zip', 'E:\\python27\\DLLs', 'E:\\python27\
\lib', 'E:\\python27\\lib\\plat-win', 'E:\\python27\\lib\\lib-tk', 'E:\\python27
', 'E:\\python27\\lib\\site-packages', 'E:\\python27\\lib\\site-packages\\pefile
-2017.11.5-py2.7.egg', 'E:\\python27\\lib\\site-packages\\future-0.16.0-py2.7.eg
g']

>>> import atm
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named atm
>>> sys.path.append(r"E:\\pyprograms\\bank")	# this code adds this path to searching module
>>> import atm
>>> print sys.path
['', 'C:\\Windows\\system32\\python27.zip', 'E:\\python27\\DLLs', 'E:\\python27
\lib', 'E:\\python27\\lib\\plat-win', 'E:\\python27\\lib\\lib-tk', 'E:\\python2
', 'E:\\python27\\lib\\site-packages', 'E:\\python27\\lib\\site-packages\\pefil
-2017.11.5-py2.7.egg', 'E:\\python27\\lib\\site-packages\\future-0.16.0-py2.7.e
g', 'E:\\\\pyprograms\\\\bank']

>>>sys.modules	#all the modules that are currently loaded

#provide shortcut name to a module name while importing so that when further accessed we can use the
#shortcut
>>>import threading as winthread
#Purpose:
		if os == 'windows':
			import xls as reader
		elif os == 'linux':
			import openpyxls as reader

#When we do import sys, py file is loaded (Here we can access everything from this module)
#even if we do from sys import path, also loads whole py(Here we can access only submodule from this module)
#Hence difference lies in understanding from where we are importing what for developer.
