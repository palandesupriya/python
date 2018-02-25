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
	self.object_Attribute  = value
	print("Constructor")
	
  def __del__(self):
	print("Destructor")
	
  def setAttribute(self, value):
	self.object_attribute = value
	
  def getAttribute(self):
	print("id of self is:{}".format(id(self)))
	return self.object_Attribute
	
def main():
	x = SimpleClass(10)
	y = SimpleClass(20)
	print ("x = {} with id = {}".format(x.getAttribute(), id(x)))
	print("******************************************************")
	print ("y = {} with id = {}".format(y.getAttribute(), id(y)))

if __name__ == '__main__':
	main()

#<Here self is reference to calling object but it is not a keyword.>
OUTPUT:  
Constructor
Constructor
id of self is:36562784
x = 10 with id = 36562784
******************************************************
id of self is:36562824
y = 20 with id = 36562824
Destructor
Destructor
