#WAP to find intersection of two lists
def GetTable(Lis1, List2):
	result = []
	result = [x for x in List1 if x in List2]
	return result

def main():
	List1 = [1, 2, 3 ,4 ,5]
	List2 = [2, 4]
	print(GetTable(List1, List2)
	
if __name__ == '__main__':
	main()