'''
Date: 13th Jan 2018
'''

FUNCTIONS HAVE:
	1)Positional Parameters
	2)Keyword arguments
		def add(a, b):
			return a+b
		
		add(b=10, a=3)	//	Keyword argument call
		
	3)default arguments
	4)Variable arguments
	5)Variable arguments dictionary:
		eg:var_arg_dict.py
		def VarArgsDictionaryDemo(a, b, c, *args, **kwargs):
			print(a, b, c)
			print (type(args))
			for x in args:
				print x
			print(type(kwargs))
			for key, value in kwargs.items():
				print (key, value)
				
				
