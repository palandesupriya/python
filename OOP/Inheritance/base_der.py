'''
Method Resolution Order(2.7 has it and fixed in 3.x)
'''
class Base():
	def foo(self):
		print "Base foo"
		
	def bar(self):
		print "Base Bar"
		
class Derived1(Base):
	def bar(self):
		print "Derived1 bar"
		
class Derived2(Base):
	def foo(self):
		print "Derived2 foo"
		
class Child(Derived1, Derived2):
	pass
	
def main():
	x  = Child()
	x.bar()		#Derived1 bar
	x.foo()		#Base foo
	
if __name__ == '__main__':
	main()
	
'''
class Base(object):
	def foo(self):
		print "Base foo"
		
	def bar(self):
		print "Base Bar"
		
class Derived1(Base):
	def bar(self):
		print "Derived1 bar"
		
class Derived2(Base):
	def foo(self):
		print "Derived2 foo"
		
class Child(Derived1, Derived2):
	pass
	
def main():
	x  = Child()
	x.bar()		#Derived1 bar
	x.foo()		#Derived2 foo
	
if __name__ == '__main__':
	main()
'''
