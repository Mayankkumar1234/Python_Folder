import sys
>>> sys.platform
'win32'
>>> import python
chai aur python
lemon tea
>>>

PS C:\Users\hp\Desktop\PythonPractise\03_Python_Day-3> python
Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
PS C:\Users\hp\Desktop\PythonPractise\03_Python_Day-3> python
Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.platform
'win32'
>>> import python
chai aur python
lemon tea
>>> python.chai(3)
3
>>> python.chai_one
'lemon tea'
>>> python.chai_four
Traceback (most recent call last):
  File "<python-input-5>", line 1, in <module>
    python.chai_four
AttributeError: module 'python' has no attribute 'chai_four'. Did you mean: 'chai_one'?
>>> from importlib import reload
>>> reload()
Traceback (most recent call last):
  File "<python-input-7>", line 1, in <module>
    reload()
    ~~~~~~^^
TypeError: reload() missing 1 required positional argument: 'module'
>>> 



lemon tea
<module 'python' from 'C:\\Users\\hp\\Desktop\\PythonPractise\\03_Python_Day-3\\python.py'>
>>> python.chai_four
'mint tea'
>>>       

