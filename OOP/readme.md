Pillars of OOP:
(1)Abstraction
(2)Encapsulation
(3)Polymorphism
(4)Inheritance

Object: An instance of a template.

For python, class is also an object, but in other languages class is template.

Every object has :
  (1)Identity(for ex Adhar number)
  (2)State(fixed or dynamic) - values of the attributes at given point of time. Some attributes do not change and some attributes change.
  (3)Responsibility
  (4)Behaviour - Every object has responsibility and they achieve it through behaviour.
  
Class contains:
	(1) Manager methods:
      Constuctor  : __init__ or __new__
	  	destructor  : __del__
      
  (2) Accessor methods / getter methods:
      Accessing the state of object using getter.
      Ex: getStudentName()
      
  (3) Mutator / setter methods:
      Changing the state of object using setter.
      Ex: setStudentName()
      
  (4) Attributes:
      4.1 Object Attributes(Present per object)
      4.2 Class attributes(Common for all objects like a static member variable in c++)
      
Example :
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
	
	#print x.__getPrivateAttribute() #Throws error as it has name mangled __getPrivateAttribute to _SimpleClass____getPrivateAttribute
	
	x._SimpleClass__setPrivateAttribute(10)
	
	print("Private member value:{}".format(x._SimpleClass__getPrivateAttribute()))
	
if __name__ == '__main__':
	main()

#<Here self is reference to calling object but it is not a keyword.>
OUTPUT:  
E:\pyprograms>python demo_class.py
Constructor
Constructor
id of self is:37677336
x = 10 with id = 37677336
******************************************************
id of self is:37677376
y = 20 with id = 37677376
******************************************************
x.__dict__ = {'_SimpleClass__private_attribute': 100, 'object_attribute': 10}
y.__dict__ = {'_SimpleClass__private_attribute': 100, 'object_attribute': 20}
******************************************************
SimpleClass.__dict__ = {'__module__': '__main__', '__del__': <function __del__ a
t 0x023E47F0>, 'institute_name': 'Trinaha Solutions', 'setAttribute': <function
setAttribute at 0x023E47B0>, '__doc__': None, 'getAttribute': <function getAttri
bute at 0x023E4A70>, '_SimpleClass__getPrivateAttribute': <function __getPrivate
Attribute at 0x023E4B30>, '_SimpleClass__setPrivateAttribute': <function __setPr
ivateAttribute at 0x023E4AB0>, '__init__': <function __init__ at 0x023E4830>}
******************************************************
institute_name = Trinaha Solutions
******************************************************
x.__dict__ = {'_SimpleClass__private_attribute': 100, 'object_attribute': 10, 't
each': True}
y.__dict__ = {'_SimpleClass__private_attribute': 100, 'object_attribute': 20}
******************************************************
Private member value:10
Destructor
Destructor
