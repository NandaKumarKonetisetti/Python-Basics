Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> set = {1,2,3,4,4,6,8,3,0}
>>> set
{0, 1, 2, 3, 4, 6, 8}
>>> set1 = {12,15,18,16,54,64,52,52}\


       
>>> 
>>> set1
{64, 16, 18, 52, 54, 12, 15}
>>> se5t
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    se5t
NameError: name 'se5t' is not defined
>>> set
{0, 1, 2, 3, 4, 6, 8}
>>> set1
{64, 16, 18, 52, 54, 12, 15}
>>> set.isdisjoint
<built-in method isdisjoint of set object at 0x000001AB4ECEB9E0>
>>> print(set.isdisjoint(set1))
True
>>> set2 = {1,2,3}
>>> set3 = {}
>>> print(set3.issubset(set))
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(set3.issubset(set))
AttributeError: 'dict' object has no attribute 'issubset'
>>> print(set2.issubset(set))
True
>>> print(set3.issubset(set))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(set3.issubset(set))
AttributeError: 'dict' object has no attribute 'issubset'
>>> print(set.union(set1))
{0, 1, 2, 3, 4, 64, 6, 8, 12, 15, 16, 18, 52, 54}
>>> set.issuperset(set2)
True
>>> set.symmetric_difference(set2)
{0, 4, 6, 8}
>>> set.symmetric_difference_update(set2)
>>> set
{0, 4, 6, 8}
>>> set.pop(4)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    set.pop(4)
TypeError: set.pop() takes no arguments (1 given)
>>> set.pop()
0
>>> set
{4, 6, 8}
>>> set.pop()
4
>>> set
{6, 8}
>>> set.add(1)
>>> set.add(@)
SyntaxError: invalid syntax
>>> set.add(8)
>>> set.add(3)
>>> set.add(5)
>>> set
{1, 3, 5, 6, 8}
>>> set.remove(6)
>>> set
{1, 3, 5, 8}
>>> setset.pop(0


	   se
	   
SyntaxError: invalid syntax
>>> set.pop()
5
>>> inside the set the pop method removes the ramdom item from the set
SyntaxError: invalid syntax
>>> set.update(set2)
>>> set
{1, 2, 3, 8}
>>> set2
{1, 2, 3}
>>> set2.add(4)
>>> set2.add(5)
>>> set2
{1, 2, 3, 4, 5}
>>> set
{1, 2, 3, 8}
>>> set.update(set2)
>>> set
{1, 2, 3, 4, 5, 8}
>>> set = {1,2,3}\


      
>>> set1 = {2,3,4}
>>> set.isdisjoint(set1)
False
>>> set.update(set10








	   h
	   
SyntaxError: invalid syntax
>>> set.update(set1)
>>> set
{1, 2, 3, 4}
>>> set = {1,2,3,4,5}
>>> set1 = {3,4,5,6}
>>> set.update(set1)
>>> set
{1, 2, 3, 4, 5, 6}
>>> data = {1:"Nanda",2:"Kumar",3:"Konetisetty"}
>>> data[1]
'Nanda'
>>> data[2]
'Kumar'
\
>>> data[3] = 'nanda'
>>> data[3]
'nanda'
>>> data[2]
'Kumar'
>>> data[5]
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    data[5]
KeyError: 5
>>> data.get(1)
'Nanda'
>>> data.get(5)
>>> data.get(3
	 )
'nanda'
>>> print(data.get(5))
None
>>> data.get(5,'key not found')
'key not found'
>>> data.get(1,"not Found")
'Nanda'
>>> # we can get the value of the data u;sing two ways one os using directly and the other way is using data.get() method
>>> key = ['name','age','sex',"dob"]
>>> value = ['Nanda kumar Konetisetty',20,'male','26/06/2001']
>>> dictionary = dict.zip(key,value))
SyntaxError: unmatched ')'
>>> dictionary = dict.zip(key,value)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    dictionary = dict.zip(key,value)
AttributeError: type object 'dict' has no attribute 'zip'
>>> dictionary = dict(zip(key,value))
>>> dict = dictionary
>>> dict(1)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    dict(1)
TypeError: 'dict' object is not callable
>>> dict[1]
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    dict[1]
KeyError: 1
>>> dict['name')
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> dict['name']
'Nanda kumar Konetisetty'
>>> dict
{'name': 'Nanda kumar Konetisetty', 'age': 20, 'sex': 'male', 'dob': '26/06/2001'}
>>> # to add the value innside a dictionaary is given below
>>> dict['subject'] = 'python'
>>> dict
{'name': 'Nanda kumar Konetisetty', 'age': 20, 'sex': 'male', 'dob': '26/06/2001', 'subject': 'python'}
>>> del dict('sex')
SyntaxError: cannot delete function call
>>> del dict['sex']
>>> dict
{'name': 'Nanda kumar Konetisetty', 'age': 20, 'dob': '26/06/2001', 'subject': 'python'}
>>> 
>>> 
>>> programs = {'c':'c editor','javascript':'vs code','python':['pycharm','sublime'],'java':{'javaSE':'NetBeans','javaEE':'Eclipse'}}

>>> 
>>> programs
{'c': 'c editor', 'javascript': 'vs code', 'python': ['pycharm', 'sublime'], 'java': {'javaSE': 'NetBeans', 'javaEE': 'Eclipse'}}
>>> java['c']
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    java['c']
NameError: name 'java' is not defined
>>> programs['c']
'c editor'
>>> programs['pycharm']
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    programs['pycharm']
KeyError: 'pycharm'
>>> programs['python']]\
		     
SyntaxError: unmatched ']'
>>> programs['python']
['pycharm', 'sublime']
>>> programs['pycharm'][0]
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    programs['pycharm'][0]
KeyError: 'pycharm'
>>> programs['python'][0]
'pycharm'
>>> programs['java']['javaSE']
'NetBeans'
>>> computerlanguages = programs.copy()
>>> computerlanguages
{'c': 'c editor', 'javascript': 'vs code', 'python': ['pycharm', 'sublime'], 'java': {'javaSE': 'NetBeans', 'javaEE': 'Eclipse'}}
>>> computerlanguages.clear(0
			)
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    computerlanguages.clear(0
TypeError: dict.clear() takes no arguments (1 given)
>>> computelanguages.clear();
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    computelanguages.clear();
NameError: name 'computelanguages' is not defined
>>> computerlanguages.clear()
>>> computerlanguages
{}
>>> computerlanguages.fromkeys
<built-in method fromkeys of type object at 0x00007FF8BC8778B0>
>>> lang = programs.copy()
>>> lang
{'c': 'c editor', 'javascript': 'vs code', 'python': ['pycharm', 'sublime'], 'java': {'javaSE': 'NetBeans', 'javaEE': 'Eclipse'}}
>>> lang1 = dict.fromkeys(lang)
>>> lang1
{'c': None, 'javascript': None, 'python': None, 'java': None}
>>> value = [1,5]
>>> result =  dict.fromkeys(lang,value)
>>> result
{'c': [1, 5], 'javascript': [1, 5], 'python': [1, 5], 'java': [1, 5]}
>>>  keya = lang.keys
 
SyntaxError: unexpected indent
>>> keya = lang.keys
>>> keya
<built-in method keys of dict object at 0x000001AB4ED1D740>
>>> keys = lang.keys()
>>> keys
dict_keys(['c', 'javascript', 'python', 'java'])
>>>   items = lang.items()
  
SyntaxError: unexpected indent
>>> items = lang.items()
>>> items
dict_items([('c', 'c editor'), ('javascript', 'vs code'), ('python', ['pycharm', 'sublime']), ('java', {'javaSE': 'NetBeans', 'javaEE': 'Eclipse'})])
>>> lang.popitem('c')
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    lang.popitem('c')
TypeError: dict.popitem() takes no arguments (1 given)
>>> lang.pop()
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    lang.pop()
TypeError: pop expected at least 1 argument, got 0
>>> lang.popitem()
('java', {'javaSE': 'NetBeans', 'javaEE': 'Eclipse'})
>>> lang
{'c': 'c editor', 'javascript': 'vs code', 'python': ['pycharm', 'sublime']}
>>> lang.pop('c')
'c editor'
>>> values = lang.values()
>>> values
dict_values(['vs code', ['pycharm', 'sublime']])
>>> lang.setdefault('javascript
		
SyntaxError: EOL while scanning string literal
>>> lang.setdefault('javascript','subj')
'vs code'
>>> lang.setdefault('javascript')
'vs code'
>>> lang.values
<built-in method values of dict object at 0x000001AB4ED1D740>
>>> lang.update({'name':'nanda'});
>>> ;amg
SyntaxError: invalid syntax
>>> lang
{'javascript': 'vs code', 'python': ['pycharm', 'sublime'], 'name': 'nanda'}
>>> lang.pop()
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    lang.pop()
TypeError: pop expected at least 1 argument, got 0
>>> lang.popitem()
('name', 'nanda')
>>> lang.update({'name':'kumar'})
>>> lanng
Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    lanng
NameError: name 'lanng' is not defined
>>> lang
{'javascript': 'vs code', 'python': ['pycharm', 'sublime'], 'name': 'kumar'}
>>> lang.pop("name)
	 
SyntaxError: EOL while scanning string literal
>>> lang.pop('name')
'kumar'
>>> lang.values