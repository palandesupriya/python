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
	x = SimpleClass(10)		#Constructor
	y = SimpleClass(20)		#Constructor
	
	print ("x = {} with id = {}".format(x.getAttribute(), id(x)))	#id of self is:39339752; x = 10 with id = 39339752
	print("******************************************************")
	
	print ("y = {} with id = {}".format(y.getAttribute(), id(y)))	#id of self is:39339672; y = 20 with id = 39339672
	print("******************************************************")
	
	print("x.__dict__ = {}".format(x.__dict__))	#x.__dict__ = {'_SimpleClass__private_attribute': 100, 'object_attribute': 10}
	print("y.__dict__ = {}".format(y.__dict__))	#y.__dict__ = {'_SimpleClass__private_attribute': 100, 'object_attribute': 20}
	
	print("******************************************************")
	
	print("SimpleClass.__dict__ = {}".format(SimpleClass.__dict__))
	'''
	SimpleClass.__dict__ = {'__module__': '__main__', '__del__': <function __del__ a
	t 0x0264CAF0>, 'institute_name': 'Trinaha Solutions', 'setAttribute': <function
	setAttribute at 0x0264CB30>, '__doc__': None, 'getAttribute': <function getAttri
	bute at 0x0264CC30>, '_SimpleClass__getPrivateAttribute': <function __getPrivate
	Attribute at 0x0264CC70>, '_SimpleClass__setPrivateAttribute': <function __setPr
	ivateAttribute at 0x0264CCB0>, '__init__': <function __init__ at 0x0264CAB0>}
	'''
	
	
	print("******************************************************")
	
	print("institute_name = {}".format(SimpleClass.institute_name))	 #institute_name = Trinaha Solutions
	
	
	print("******************************************************")
	
	x.teach = True
	print("x.__dict__ = {}".format(x.__dict__))#x.__dict__ = {'_SimpleClass__private_attribute': 100, 'object_attribute': 10, 'teach': True}
	print("y.__dict__ = {}".format(y.__dict__))#y.__dict__ = {'_SimpleClass__private_attribute': 100, 'object_attribute': 20}
	
	print("******************************************************")
	#print(x.__private_attribute)	#Throws error as it has name mangled __private_attribute to _SimpleClass__privateAttribute
	#print(y.__private_attribute)	#Throws error as it has name mangled __private_attribute to _SimpleClass__privateAttribute
	#x.__setPrivateAttribute(10)	#Throws error as it has name mangled __setPrivateAttribute to _SimpleClass__setPrivateAttribute
	#print x.__getPrivateAttribute()		#Throws error as it has name mangled __getPrivateAttribute to _SimpleClass____getPrivateAttribute
	x._SimpleClass__setPrivateAttribute(10)
	print("Private member value:{}".format(x._SimpleClass__getPrivateAttribute())) #Private member value:10
	
if __name__ == '__main__':
	main()
