Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x= None
>>> x
>>> print(x)
None
>>> n = 5
>>> id(n)
1579818969520
>>> a =n
>>> id(a)
1579818969520
>>> j = 45
>>> k = j
>>> id(j)
1579818970800
>>> id(k)
1579818970800
>>> a = 9
>>>  id(a)
 
SyntaxError: unexpected indent
>>> id(a)
1579818969648
>>> b=9
>>> id(b)
1579818969648
>>> b = a
>>> id(b)
1579818969648
>>> PI = 3.14
>>> PI
3.14
>>> for all the data that have beem working for the nation to get the data that are working for our nation of the data as itself in the working for all the data that have been working for all t
SyntaxError: invalid syntax
>>> 
>>> type(PI)
<class 'float'>
>>> inside the numeric there are some sub types like int,float,boolean,and  complex
SyntaxError: invalid syntax
>>> a=9
>>> type(a)
<class 'int'>
>>> b = 9.0
>>> type(b)
<class 'float'>
>>> c = 9+5i
SyntaxError: invalid syntax
>>> c = 9+5j
>>> type(c)
<class 'complex'>
>>> d =0
>>> type(d)
<class 'int'>
>>> d = True
>>> type(d)
<class 'bool'>
>>> list = [1,2,3,4]
>>> type(list)
<class 'list'>
>>> marks = (23,24,25,26)
>>> type(marks)
<class 'tuple'>
>>> marks[0] =9
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    marks[0] =9
TypeError: 'tuple' object does not support item assignment
>>> marks[0]
23
>>> grades = {'a','b','c','d'}
>>> type(grades)
<class 'set'>
>>> dictionary = {'phone':'iphone','device':'apple','os' :'ios'}
>>> type(dictionary)
<class 'dict'>
>>> dictionary.fromkeys(0)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    dictionary.fromkeys(0)
TypeError: 'int' object is not iterable
>>> dictionary.fromkeys({1,2})
{1: None, 2: None}
>>> dic = dict.fromkeys(dictionary)
>>> dic
{'phone': None, 'device': None, 'os': None}
>>> list = ['iphone','apple','ios']
>>> data = dict.fromkeys(dictionary,list)
>>> data
{'phone': ['iphone', 'apple', 'ios'], 'device': ['iphone', 'apple', 'ios'], 'os': ['iphone', 'apple', 'ios']}
>>> dictionary.get('iphone')
>>> dat = dictionary.get('iphone')
>>> dat
>>> dictionary.get('phone')
'iphone'
>>> dictionary.items()
dict_items([('phone', 'iphone'), ('device', 'apple'), ('os', 'ios')])
>>> dictionary.keys()
dict_keys(['phone', 'device', 'os'])
>>> dictionary.values()
dict_values(['iphone', 'apple', 'ios'])
>>> dictionary.update('phone':'samsung')
SyntaxError: invalid syntax
>>> dictionary.update('phone'='samsung')
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
>>> dictionary.update({'phone':'samsung'})
>>> dictionary
{'phone': 'samsung', 'device': 'apple', 'os': 'ios'}
>>> dictionary.popitem('phone'0
		   
SyntaxError: invalid syntax
>>> dictionary.popitem('phone')
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    dictionary.popitem('phone')
TypeError: dict.popitem() takes no arguments (1 given)
>>> dictionary.pop()
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    dictionary.pop()
TypeError: pop expected at least 1 argument, got 0
>>> dictionary.popitem()
('os', 'ios')
>>> dictionary.update({'os':'ios'})
>>> dictionary
{'phone': 'samsung', 'device': 'apple', 'os': 'ios'}
>>> dictionary.pop('device')
'apple'
>>> dictionary.setdefault('device' = 'android')
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
>>> dictionary.setdefault('device1' , 'android')
'android'
>>> dictionary
{'phone': 'samsung', 'os': 'ios', 'device1': 'android'}
>>> operators in python
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    operators in python
NameError: name 'operators' is not defined
>>> x =90
>>> y = 98
>>> z = x+y
>>> z
188
>>> x>y
False
>>> x<y
True
>>> X==y
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    X==y
NameError: name 'X' is not defined
>>> x ==y
False
>>> x!=y
True
>>> a=9
>>> b = 7
>>> a>b
True
>>> a<b
False
>>> x<y and x!=y
True
>>> x<y and x==y
False
>>> x<y or x==y
True
>>> a = True
>>> not a
False
>>> !a
SyntaxError: invalid syntax
>>> x = !x
SyntaxError: invalid syntax
>>> a = !a
SyntaxError: invalid syntax
>>> a = not a
>>> a
False
>>> b= False
>>> b
False
>>> b = !b
SyntaxError: invalid syntax
>>> b = not b
>>> b
True
>>> b = not b
>>> b
False
>>> not b
True
>>> not b
True
>>> bot
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    bot
]NameError: name 'bot' is not defined
>>> not b
True
>>> b = not b
>>> b
True
>>> b =False
>>> b
False
>>> b = not b
>>> b
True
>>> b = not b
>>> b
False
>>> not b
True
>>> not b
True
>>> not b
True
>>> b = not b
>>> b
True
>>> b=
SyntaxError: invalid syntax
>>> a = True
>>> a
True
>>> not a
False
>>> not a
False
>>> a = not a
>>> a
False
>>> b= False
>>> b
False
>>> b = not b
>>> b
True
>>> b= not v
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    b= not v
NameError: name 'v' is not defined
>>> b= not b
>>> b
False
>>> a = 90
>>> bin(a)
'0b1011010'
>>> '0b1011010'
'0b1011010'
>>> 0b1011010
90
>>> 12
12
>>> a - 7
83
]
>>> a =7
>>> oct(a)
'0o7'
>>> 0o7
7
>>> hex(a)
'0x7'
>>> a = 15
>>> hex(a)
'0xf'
>>> 0xf
15
>>> # SWAPPING OF TWO VARIABLE IN PYTHON
>>> a= 90
>>> b=87
>>> # SWAPPING USING TEMPORARY VARIABLES
>>> temp = a
>>> a= b;
>>> b= temp
>>> aq
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    aq
NameError: name 'aq' is not defined
>>> a
87
>>> b
90
>>> #SWAPPING OF TWO VARIABLES WITHOUT USING THE TEMPORARY VARIABLES
>>> a =7
>>> b = 4
>>> a =a+b
>>> b = a -b
>>> a =  a-b
>>> a
4
>>> b
7
>>> # SWAPPING OF TWO VARIABLES USING XOR OPERATOR
>>>  a = a^b
 
SyntaxError: unexpected indent
>>> a = a^b
>>> a = a^b
>>> b =a^b
>>> a
4
>>> b
3
>>> a= a^b
>>> b =a^b
>>> a =a^b
>>> a
3
>>> b
4
>>> 10<<2
40
>>> 10<<4
160
>>> 10><2
SyntaxError: invalid syntax
>>> 10>2
True
>>> 10>>1
5
>>> 10>>2
2
>>> 10<6
False
>>> 2<<6
128
\
>>> .
SyntaxError: invalid syntax
>>> 10^7
13
>>> #IN XOR OPERATOR IF ONE OF THE BIT IS 0 AND THE OTHER ONE IS 1 THEN IT RETURNS 1 . IF BOTH OF THE BITS ARE 0 AND 1 THEN IT RETURNS 0
>>> 17^8
25
>>> 