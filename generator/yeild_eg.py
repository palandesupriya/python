'''
Lazy evaluation or late late evaluation: yield()
'''

import threading
def square(n):
	for i in range(1,n):
		yield i*i			#Generating data for next evaluation;it is generator
							#Here WE are generating data.
							
							'''
								x = [32,34,56]
								y = iter(x)		#here it is iterator since data has been generated BEFOREHAND
								next(y) gives 32 
								next(y) gives 34
								next(y) gives 56
							'''
def main():
	x = square(5)
	print next(x)
	print next(x)
	print next(x)
	print next(x)
	print next(x)
	print next(x)
	'''
	for i in x:
		print i
	'''
if __name__ == '__main__':
	main()
