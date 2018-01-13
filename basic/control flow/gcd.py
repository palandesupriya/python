'''

WAP to find GCD of two numbers-recursive function

'''
def GCD(a, b):
	if b == a:
		return b
	if a > b:
		return GCD(a-b, b)
	else:
		return GCD(b-a, a)

def LCM(a, b):
	return (a*b) / (GCD(a,b))
	
def main():
	a = input("Enter num:")
	b = input("Enter num:")
	print("GCD of two numbers:{}".format(GCD(a, b)))
	print("LCM of two numbers:{}".format(LCM(a, b)))
	
if __name__ == '__main__':
	main()