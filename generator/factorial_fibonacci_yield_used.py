'''
1)WAP to accept range from user and generate factorials of given range.
2)WAP to accpet lower bound and upper bound from user, and generate fibonacci numbers
	present in given range
	if 5, 15 then output(5,8,13)
'''
def Factorial(low, high):
	for iTemp in range(low, high + 1):
		fact = 1
		for i in range(2, iTemp + 1):
			fact = fact * i
		yield fact

def Fibonacci(low, high):
	f1 = 0
	f2 = 1
	f3 = 1
	while (f1 <= high):
		if (f1 >= low):
		   yield f1
		f1 = f2
		f2 = f3
		f3 = f1 + f2

def main():
	lb, ub = input("Enter range:")
	allfact = Factorial(lb, ub)
	for i in allfact:
		print i
	print "**********************************"
	allfib = Fibonacci(lb, ub)
	for i in allfib:
		print i

if __name__ == '__main__':
	main()
