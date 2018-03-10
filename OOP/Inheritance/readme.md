1)Explicitely call base class contructor irrespective of number of arguments.
2)Call base class constructor :
  BaseClassName.__init__(self, <paramter of base if any>)
  
  '''
Implement inheritance of Human Employee.
'''

class Human(object):
	def __init__(self, name, gender):
		self.name = name
		self.gender = gender
		
	def getDetails(self):
		return self.name, self.gender
		
class Employee(Human):
	def __init__(self, name, gender, experience, salary, desig):
		Human.__init__(self, name, gender)
		self.experience = experience
		self.salary = salary
		self.desig = desig
		
	def getDetails(self):
		return Human.getDetails(self), self.experience,self.salary,self.desig
	
def main():
	name,gender,experience,salary,desig = input("Enter name, gender, experience, salary, desig:")
	emp = Employee(name,gender,experience,salary,desig)
	#print emp.getDetails()
	print emp.__dict__

if __name__ == '__main__':
	main()
