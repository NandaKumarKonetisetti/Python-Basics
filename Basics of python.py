Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 4
>>> y = 34
>>> x+y
38
>>> _+3
41
>>> nanda = "kumar"
>>> nanda
'kumar'
>>> nanda[0]
'k'
>>> nanda[0:]
'kumar'
>>> nanda.capitalize
<built-in method capitalize of str object at 0x0000018688703930>
>>> nanda
'kumar'
>>> nanda.()
SyntaxError: invalid syntax
>>> nand
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    nand
NameError: name 'nand' is not defined
>>> nanda
'kumar'
>>> nanda.capitalize()
'Kumar'
>>> nanda[-1:]
'r'
>>> nanda[-5:]
'kumar'
>>> nanda[:-1}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> nanda[:-1]
'kuma'
>>> nanda[0]
'k'
>>> nanda[9]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    nanda[9]
IndexError: string index out of range
>>> nanda[4]
'r'
>>> nanda[1:3]
'um'
>>> nanda[0] = 'm'
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    nanda[0] = 'm'
TypeError: 'str' object does not support item assignment
>>> nanda[1:3] = 'ku'
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    nanda[1:3] = 'ku'
TypeError: 'str' object does not support item assignment
>>> 'nanda '+ kumar
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    'nanda '+ kumar
NameError: name 'kumar' is not defined
>>> 'nanda '+nada
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    'nanda '+nada
NameError: name 'nada' is not defined
>>> 'nanda '+nanda
'nanda kumar'
>>> print('nanda"S laptop')
nanda"S laptop
>>> print('nanda\"s 'laptop'')
SyntaxError: invalid syntax
>>> print('nanda\'s "laptop"')
nanda's "laptop"
>>> print('"nanda\"s 'laptop'')
SyntaxError: invalid syntax
>>> print('"nanda\'s" laptop');
"nanda's" laptop
>>> list = [1,2,3,4,5,6,7,8,9,10]
>>> list.append(11);
>>> list.append("nanda")
>>> list
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 'nanda']
>>> list.pop()
'nanda'
>>> list
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
>>> list.pop(1)
2
>>> list.pop(1:)
SyntaxError: invalid syntax
>>> list.pop[1:]
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    list.pop[1:]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> list[1:]
[3, 4, 5, 6, 7, 8, 9, 10, 11]
>>> list.count
<built-in method count of list object at 0x00000186868B71C0>
>>> list.count()
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    list.count()
TypeError: list.count() takes exactly one argument (0 given)
>>> list.insert(1)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    list.insert(1)
TypeError: insert expected 2 arguments, got 1
>>> list.length()
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    list.length()
AttributeError: 'list' object has no attribute 'length'
>>> list[0]
1
>>> list
[1, 3, 4, 5, 6, 7, 8, 9, 10, 11]
>>> list[1] = 2
>>> list
[1, 2, 4, 5, 6, 7, 8, 9, 10, 11]
>>> list.insert[1,3]
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    list.insert[1,3]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> list.insert[1,4]
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    list.insert[1,4]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> list
[1, 2, 4, 5, 6, 7, 8, 9, 10, 11]
>>> list.insert(2,3)
>>> list
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
>>> list.remove(1)
>>> list
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
>>> list.remove(6)
>>> list
[2, 3, 4, 5, 7, 8, 9, 10, 11]
>>> list.reverse()
>>> list()
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    list()
TypeError: 'list' object is not callable
>>> list
[11, 10, 9, 8, 7, 5, 4, 3, 2]
>>> list.sort()
>>> list
[2, 3, 4, 5, 7, 8, 9, 10, 11]
>>> list
[2, 3, 4, 5, 7, 8, 9, 10, 11]
>>> list.extend([12,13,14,15])
>>> list
[2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15]
>>> list1 = [20,21,22,26,27,28,29]
>>> list.extend([list1])
>>> list
[2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, [20, 21, 22, 26, 27, 28, 29]]
>>> del list[7:]
>>> list
[2, 3, 4, 5, 7, 8, 9]
>>> min(list)
2
>>> max(list)
9
>>> sum(list)
38
>>> list.index[9]
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    list.index[9]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> list.index(9)
6
>>> list.index(2)
0
>>> list.copy
<built-in method copy of list object at 0x00000186868B71C0>
>>> list1.copy(list)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    list1.copy(list)
TypeError: list.copy() takes no arguments (1 given)
>>> list.copy(list)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    list.copy(list)
TypeError: list.copy() takes no arguments (1 given)
>>> print(list.copy)
<built-in method copy of list object at 0x00000186868B71C0>
>>> list
[2, 3, 4, 5, 7, 8, 9]
>>> list.pop(-1)
9
>>> list
[2, 3, 4, 5, 7, 8]
>>> list.append(9)
>>> list
[2, 3, 4, 5, 7, 8, 9]
>>> list.remove(3)
>>> list
[2, 4, 5, 7, 8, 9]
>>> list.insert(1,3)
>>> list
[2, 3, 4, 5, 7, 8, 9]
>>> list.insert(0,1)
>>> list.remove(4:)
SyntaxError: invalid syntax
>>> del list[4:]
>>> list
[1, 2, 3, 4]
>>> del list[0:]
>>> list
[]
>>> list.extend([1,2,3,4,45,5,6,76,78,8])
>>> list
[1, 2, 3, 4, 45, 5, 6, 76, 78, 8]
>>> list1 = list.copy()
>>> list1
[1, 2, 3, 4, 45, 5, 6, 76, 78, 8]
>>> print(list.count())
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    print(list.count())
TypeError: list.count() takes exactly one argument (0 given)
>>> count(list)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    count(list)
NameError: name 'count' is not defined
>>> count method  is used to fidnd the number of the occurances of a particular word inside a given list
SyntaxError: invalid syntax
>>> list.extend([1,1,1,1,1,1,1])
>>> list
[1, 2, 3, 4, 45, 5, 6, 76, 78, 8, 1, 1, 1, 1, 1, 1, 1]
>>> list.count(1)
8
\
>>> tuple = (1,2,3,"mam")
>>> tuple
(1, 2, 3, 'mam')
>>> tuple.index(3)
2
>>> list.index('mam')
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    list.index('mam')
ValueError: 'mam' is not in list
>>> tuple.index('mam')
3
>>> tuple1 = [1,2,3,3,3,3,34,4,4,4,65,6,6]
>>> tuple
(1, 2, 3, 'mam')
>>> tuple1
[1, 2, 3, 3, 3, 3, 34, 4, 4, 4, 65, 6, 6]
>>> tuple1.count(4)
3
>>> set = {1,2,45,24,15,7,8,36,65,95,78}
>>> set
{65, 2, 1, 36, 7, 8, 45, 78, 15, 24, 95}
>>> set does not contain the duplicate values
SyntaxError: invalid syntax
>>> set = {9,5,1,3,4,6}
>>> set
{1, 3, 4, 5, 6, 9}
>>> set1 = {1,2,3,4,5,6,7,8,9,,1,1,1,2,2,2,3,3,3}
SyntaxError: invalid syntax
>>> set1 = {1,2,3,4,4,4,5,5,6,6,9}
>>> set1
{1, 2, 3, 4, 5, 6, 9}
>>> set = {1,1,2,3,4,5,6,7,8,9}\
set
SyntaxError: invalid syntax
>>> set
{1, 3, 4, 5, 6, 9}
>>> set.add(2)
>>> set
{1, 2, 3, 4, 5, 6, 9}
>>> set1 = set.copy()
>>> set1
{1, 2, 3, 4, 5, 6, 9}
>>> set
{1, 2, 3, 4, 5, 6, 9}
>>> set.clear()
>>> set
set()
>>> set
set()
>>> set =set1.copy()
>>> set
{1, 2, 3, 4, 5, 6, 9}
>>> set.difference()
{1, 2, 3, 4, 5, 6, 9}
>>> set1 = {5,6,9,0}
>>> diff = set1.difference(Set)
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    diff = set1.difference(Set)
NameError: name 'Set' is not defined
>>> diff = set.difference(set1)
>>> diff
{1, 2, 3, 4}
>>> diffe = set1.difference(set)
>>> diffe
{0}
>>> set
{1, 2, 3, 4, 5, 6, 9}
>>> set1
{0, 9, 5, 6}
>>> differenceupdate = set.difference_update(set1)
>>> differenceupdate
>>> set
{1, 2, 3, 4}
>>> set.add(5)
>>> set.add(6)
>>> set.add(1)
>>> set
{1, 2, 3, 4, 5, 6}
>>> set.add(9)
>>> intersection =  set.intersection(set1)
>>> intersection
{9, 5, 6}
>>> set
{1, 2, 3, 4, 5, 6, 9}
>>> set1
{0, 9, 5, 6}
>>> intersection method returns the common elements in the both of the sets
SyntaxError: invalid syntax
>>> intersecupda =  set1.intersection_update(set)
>>> intersecupda
>>> set1
{9, 5, 6}
>>> set
{1, 2, 3, 4, 5, 6, 9}
>>> inter = set.intersection_update(set1)
>>> set
{9, 5, 6}
>>> set.discard(1)
>>> set
{9, 5, 6}
>>> set.discard(9)
>>> set
{5, 6}
>>> set.update