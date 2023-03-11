# identifiers
'''
identifiers are the user defined words. if you take any python entity and name it then that's going to consider as identifiers.
like file name, function name, class name, module name etc

there are some rules to defines identifiers:
1. identifiers should start with alphabets or underscore but it shouldn't start with number
2. no special characters are allowed except '_'
3 there is a method called isidentifier() where it's going to check whether the given identifier is valid or not.
'''
print("python_class".isidentifier())
print("_pythonclass".isidentifier())
print("_1pythonclass".isidentifier())
print("1pythonclass".isidentifier())
print(" python".isidentifier())

#keywords
'''
1.keywords are the special words in python
2. each keyword has a different meaning
3. there are 35 keywords in python
4. to get all the keywords we could use
import keywords
keywords.kwlist
(or)
help("keywords)
5.we shouldnt use keywords for identifiers or variables
6.to check whether the given word is keyword or not we have one method called iskeyword()
7.keywords are case sensitive
'''

import keyword
print(keyword.kwlist)

help("keywords")

print(keyword.iskeyword("True"))
print(keyword.iskeyword("import"))
print(keyword.iskeyword("return"))
print(keyword.iskeyword("true"))
print(keyword.iskeyword("Lambda"))

#variables
'''1. if we have data to store thats going to store in the memory, if we name that memory address
 we can call that as variable
 eg:- a = 10, b = 10.0, c = "abc", d = [1,2,[1,2]]
 
 rules to declare varibles are same as identifiers
'''

#memory managment in python
'''
memory managemant happens inside the random access memory, inside the ram there are two more memories called
stack memory and heap memory.

there is one more memory inside stack memory which is called as main frame

in the main frame all the variables are going to store 
in the heap memory all the data are going to store in the form of objects

varaibales are going to make a relationship with the data in the form of references

if the object has no reference there is a garbage collecotr in python which is going to collect those object
and its going to clear
'''