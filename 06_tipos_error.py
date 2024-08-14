#Error Types

#_SyntaxError
#print'Error'           •Error
print('Error')


#_NameError              •'name' is not defined           
#print(name)


#_IndexError
my_list = ['python', 'kotlin', 'js', 'php']
#print(my_list[4])      •IndexError: list index out of range
print(my_list[0])       


#_ModuleNotFoundError   •ModuleNotFoundError: No module named 'maths'
#import maths
import math


#_AtributeError
#print(math.PI)          •AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
print(math.pi)


#_keyError
my_dict = {"js":"javascript", "kt":"kotlin", "py":"python", "sw":"switf"}
print(my_dict["js"])
#print(my_dict["ktl"])      •KeyError: 'ktl'


#_TypeError
#print(my_list['python'])    •TypeError: list indices must be integers or slices, not str


#_ImportEror
#_from math import PI        •ImportError: cannot import name 'PI' from 'math' (unknown location). Did you mean: 'pi'?
from math import pi


#_ValueError
ten = int('10 Años')          #ValueError: invalid literal for int() with base 10: '10 A�os'
print(type(ten))


#_ZeroDivisionError
print(4/2)
print(4/0)                    #ZeroDivisionError: division by zero