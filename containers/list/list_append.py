'''
WAP which accepts a list and an element to be appended to the list.
If the element to be appended is a container then list should be extended
else element should be appended.
'''

def appendlist(lstMain, lstAdd):
	if (list == type(lstAdd)):
		lstMain.extend(lstAdd)
	else:
		lstMain.append(lstAdd)
	
def main():
	lstMain = input("Enter list:")
	lstAdd = input("Enter element to append:")
	appendlist(lstMain, lstAdd)
	print lstMain
	
if __name__ == '__main__':
	main()
