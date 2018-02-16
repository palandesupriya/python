'''
 WAP to create an archieve file of the specified folder using shutil module.
'''
from shutil import make_archive

def main():
	archive_name = input("Enter name of archive: ")
	Folder_path = input("Enter Folder path(can be relative) : ")
	make_archive(archive_name,'zip', Folder_path)
	
if __name__=="__main__":
	main()