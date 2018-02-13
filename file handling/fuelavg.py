'''
 Assignment - go to Presentation
	- print average of fuel prices of 3 states(Maharashtra, goa, Karnatak).
	Jan 2015 81 67 84
	Feb 2015 79 66 82
	Mar 2015 78 65 81
	Apr 2015 77 64 80
'''
def FuelAvg(infnm):
	fp = open(infnm, "r")
	sumMaha = 0
	sumKar = 0
	sumGoa = 0
	total = 0
	lines = fp.readlines()
	for line in lines:
		fdata = line.split(None)
		sumMaha += int(fdata[2])
		sumKar += int(fdata[3])
		sumGoa += int(fdata[4])
		total += 1
	print("Average of state 1 is {}".format(sumMaha/total))
	print("Average of state 2 is {}".format(sumKar/total))
	print("Average of state 3 is {}".format(sumGoa/total))
	
def main():
	infnm = "petrol.txt"
	FuelAvg(infnm)

if __name__ == '__main__':
	main()
	