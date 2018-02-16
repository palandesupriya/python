'''
Implement set function on list. For example, take 2 list as input &
return union,intersection,symmetric_difference,difference,ISdisjoint of them.
'''
def isuperset(l1, l2):
	for i in l2:
		if i not in l1:
			return False
	return True
	
def isdisjoint(l1, l2):
	for i in l1:
		if i in l2:
			return False
	return True
	
def difflst(l1, l2):
	l3 = []
	for i in l1:
		if i not in l2:
			l3.append(i)
	l3.sort()
	return l3
				
def symmetric_diff(l1,l2):
				l3 = []
				unilst = unionlst(l1, l2)
				intrlst = intersectlst(l1, l2)
				for i in unilst:
					if i not in intrlst:
						l3.append(i)
				l3.sort()
				return l3
				
def intersectlst(l1,l2):
	l3 = []
	for i in l1:
		if i in l2:
			l3.append(i)
	l3.sort()
	return l3
def removeduplicates(lst):
	templst = []
	for i in lst:
		if i not in templst:
			templst.append(i)
	return templst
def unionlst(l1, l2):
	l3 = l1+l2
	l3.sort()
	l3 = removeduplicates(l3)
	return l3
def main():
	#l1 = [1,2,3,4,5]
	#l2 = [2,4,5,3,6]
	l1 = []
	l2 = []
	l1 = input("Enter list 1:")
	l2 = input("Enter list 2:")
	print("Lists are:{} and {}".format(l1,l2))
	print("Union of two list is:{}".format(unionlst(l1,l2)))
	print("Intersection of two list is:{}".format(intersectlst(l1,l2)))
	print("symmetric difference of two list is:{}".format(symmetric_diff(l1,l2)))
	print("difference of two list is:{}".format(difflst(l1,l2)))
	print("Are disjoint two list :{}".format(isdisjoint(l1,l2)))
	print("Is first list superset of second list :{}".format(isuperset(l1,l2)))
	
if __name__ == '__main__':
	main()