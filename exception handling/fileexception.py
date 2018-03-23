def FileException(inFile):
	try:
		fd= open(inFile,"w+")
		try:
			fd.write("Hello")
		finally:
			fd.close()
	except Exception as e:
		print e.errno
		print e.args
		print type(e).__name__
		
def main():
	inFile = input("Enter file name : ")
	FileException(inFile)
	
if __name__=="__main__":
	main()
