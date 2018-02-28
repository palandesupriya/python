class SimpleClass:
  institute_name = "Trinaha Solutions"
  
  def __init__(self, value):
	self.__private_attribute = 100
	self.object_attribute  = value
	print("Constructor")
	
  def __del__(self):
	print("Destructor")
	
  def setAttribute(self, value):
	self.object_attribute = value
	
  def getAttribute(self):
	print("id of self is:{}".format(id(self)))
	return self.object_attribute

  def __setPrivateAttribute(self, value):
	self.__private_attribute = value

  def __getPrivateAttribute(self):
	return self.__private_attribute
	
def main():
	x = SimpleClass(10)
	y = SimpleClass(20)
	print ("x = {} with id = {}".format(x.getAttribute(), id(x)))
	print("******************************************************")
	print ("y = {} with id = {}".format(y.getAttribute(), id(y)))
	print("******************************************************")
	print("x.__dict__ = {}".format(x.__dict__))
	print("y.__dict__ = {}".format(y.__dict__))
	print("******************************************************")
	print("SimpleClass.__dict__ = {}".format(SimpleClass.__dict__))
	print("******************************************************")
	print("institute_name = {}".format(SimpleClass.institute_name))
	print("******************************************************")
	x.teach = True
	print("x.__dict__ = {}".format(x.__dict__))
	print("y.__dict__ = {}".format(y.__dict__))
	print("******************************************************")
	#print(x.__private_attribute)	#Throws error as it has name mangled __private_attribute to _SimpleClass__privateAttribute
	#print(y.__private_attribute)	#Throws error as it has name mangled __private_attribute to _SimpleClass__privateAttribute
	#x.__setPrivateAttribute(10)	#Throws error as it has name mangled __setPrivateAttribute to _SimpleClass__setPrivateAttribute
	#print x.__getPrivateAttribute()		#Throws error as it has name mangled __getPrivateAttribute to _SimpleClass____getPrivateAttribute
	x._SimpleClass__setPrivateAttribute(10)
	print("Private member value:{}".format(x._SimpleClass__getPrivateAttribute()))
	
if __name__ == '__main__':
	main()