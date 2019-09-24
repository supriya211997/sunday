
Python developed in 1989.
officialy released in 1991.
'Guido Van Rossum' who developed Python.

Python features:

freeware(without licsence).
Open Source (Source code available and you can also develop your own code and register that 
									code with Python community)
Platform Indepedent.
OPPs 
functional (like 'C')
Scripting.
Dynamicaly Typed(There is no need to defining data type).
Modula 3.




Python Identifiers: (identifier is which identify what it is.)
 Name: name  is an identifier
 	->variables: variables are the name of reserved cell in the memmory(RAM).
 			a = 10
 			here we are assigning the value to a.
 	class
 	methods	
 
 There are some rules for Identifiers
 1. Single Character
 	A-Z
 	a-z
 	0-9
 	_(under score)

2.Identifiers should not start with digit. But it can be in end.
		12ac = 10==> not allowed
		ac12 = 20 ==> allowed
3.Python identifiers are case sensitive.
	a = 10
	A = 20
	both are treated as diferent variable.
4.No length limit of identifier in Python
	 aaaaaaaaaaaaaaaaaaa=20==> allowed

5.we can't use reserved key word.

	x = 30
	_x = 10  protected variable
	__x = 20 private variable

Reserved Key Words:- We can't use these reserved keywords as our custom.
reserved key word == True, False, None ,
and,or,not,is, if ,
elif,else,while,for,break,continue,return,
in,yield,try,except,
finally,raise,assert,
 import,from ,as,class,
def,pass,global,nonlocal,
lambda,del,with

all these 33 key words have satart with alphabets but except only three i.e. 
True,False,None have start with capital letter

*switch concept is not allowed in python.
*do-while is not allowed in python. 


Q.when we use ('')single quotes, when we use (" ") double quotes, 
and when we use (''' ''') triple single quotes?
For single line content then use single quote(' ') and double quots(" ").
If we use multi line content then we use triple single quotes(''' ''').

x = "hi kundan. How r u?"

a = '''This class for Python students only.To use '@' and '!' as normal character
	in our string. To define docstring.'''
print(a)

Q. What is Datatype?

Ans: Datatypes are just gives the information about reserved cell in memmory.
		like size of cell and the type of data which will be store in cell.

Datatype in Python:-
-----------------------
In python we could not need to define type of data explicitly that's 
python is dynamicaly typed language..


various datatypes in python:-

int, float, complex, bool, str, list, set, tuple, dict,
frozenset, bytes, bytearray, range, None.


=>> Every thing in Python is an object.
	a = 10
	print(id(a))
	output:-- 140714738553952 the refrence of that object i.e. 10 inside the 
				memory.

int:- In python we have only two integral data type i.e. int for small number
	 and long for bigger value but in only python 2.x, but this long concept 
	 is not applicable in python 3.x .we use only int in python 3.x .

	 There is no char datatype in python only str we use.

index:- left to right +ive (0,1,2,3,....)
		right to left -ive (-1,-2,-3,...)

slice:- ([:]) part of string
		[begin index : end index]
		at the time return the value==>[begin index : end-1]

		Application of slice operator
		------------------------------
		s = 'seemant'
		a = s[0].upper()+s[1:]
		print(a)
		o/p=> Seemant

		if we want first character and last charachter will be in upper case.
		then we use slice as 

		b = s[0].upper()+s[1:len(s)-1]+s[-1].upper()
		print(b)

		str data type
		---------------
			+ operator for string
			s = 'Good'+'afternoon'
			print(s)

			compulsory both argument must be string
			otherwise it gives TypeError

			s = 'good'+10
			print(s)==>this is type error

			s = 'Good'+str(10)
			print(s)

			output==>Good10


		Operator:  
		----------
		String Repetation operator (*)
		 a = 'abc'*3
		 print(a)==> abcabcabc

		 a = 3*'abc'
		 print(a)==>abcabcabc

		 Rule:--one must be string and other must be int.
		 ------------------------------------------

		 a = 'abc'*'xyz'
		 print(a)==>type error
	


		 
