#WAP to generate the table.
def GetTable(lb, ub):
	result = []
	result = [[x * i for i in range(1, 11)] for x in  range(lb, ub)]
	return result

def main():
	lb = eval(input("Enter the lower range: "))
	ub = eval(input("Enter the upper range: "))
	print(GetTable(lb, ub + 1))
	
if __name__ == '__main__':
	main()