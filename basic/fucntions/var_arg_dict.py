'''

Variable argument dictionary:
Note:Once it finds something=something, it is mapped to kwargs

'''

def VarArgsDictionaryDemo(a, b, c, *args, **kwargs):
			print(a, b, c)
			print (type(args))
			for x in args:
				print x
			print(type(kwargs))
			
			#Two ways to print key value pair
			for key in kwargs:					'''(1)st way'''
				print ("{} = {}".format(key, kwargs[key]))
				
			for key,value in kwargs.items():	'''(2)nd way'''
				print key,value
				
def main():
	VarArgsDictionaryDemo(1, 2, 3, 45, 46, 47, name = "Supriya", hobby = "Reading")


if __name__ == '__main__':
	main()