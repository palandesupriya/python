'''
WAP to accept a dictionary and another container, replace all the value pairs
in the dictionary with the values from the container. If the dictionary len	
is greater then the rest keys will have None value. If only single value is passed
then all the keys of dictionary will have that single value.
'''

def FromKeys(dc, lst):
	result_dict = {}
	k = 0
	if list == type(lst):
		for key in dc:
			if k != len(lst):
				result_dict[key] = lst[k] 
				k += 1
			else:
				result_dict[key] = None				
	else:
		result_dict = dict.fromkeys(dc, lst)
	return result_dict

def main():
	x1 = {1:3, 2:6, 3:8, 4:2}
	print(FromKeys(x1, [7, 8, 9]))
	
	x2 = {1:1, 2:2, 3:3}
	print(FromKeys(x2, [7, 8,9]))
	
	x3 = {1:1, 2:2, 3:3, 4:4}
	print(FromKeys(x3, 5))
	
if __name__ == '__main__':
	main()