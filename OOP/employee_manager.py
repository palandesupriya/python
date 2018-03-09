'''
WAP to design and implement employee mgmt system
	add
	remove
	search by name or salary
	promote employee/demote
	change designation
	change address
	change marital status
	HUMAN,
	EMPLOYEE,
	EMPLOYEEMANAGER
'''
lstDesignation = ["Associate SE", "Software Engg", "Associate Team Lead", "Team Lead"]
class Human:
	iAadharNum = 1234
	def __init__(self, szName, szAddress, szMaritalStatus):
		self.szName = szName
		self.szAddress = szAddress
		self.szMaritalStatus = szMaritalStatus
		self.iAadharNum = Human.iAadharNum
		Human.iAadharNum += 1
		
	def getDetails(self):
		return self.szName, self.szAddress, self.szMaritalStatus

class Employee:
	iEmployeeID = 1092
	dctEmployeeHuman = {}	
	def __init__(self, szName, szAddress, szMaritalStatus, szDesignation):
			self.szDesignation = szDesignation
			self.iEmployeeID = Employee.iEmployeeID
			Employee.iEmployeeID += 1
			self.salary = 1000
			obj = Human(szName, szAddress, szMaritalStatus)
			Employee.dctEmployeeHuman[self.iEmployeeID] = obj

	def getEmployee(self, iEmployeID):
		if iEmployeID in Employee.dctEmployeeHuman:
			return Employee.dctEmployeeHuman[iEmployeID].getDetails(), self.szDesignation, self.salary
		else:
			return False
			
	def getDesignation(self):
		return lstDesignation.index(self.szDesignation)
		
	def setDesignation(self, szdesig):
		self.szDesignation = szdesig
		self.salary += 1000
			
	def getEmployeeID(self):
		return self.iEmployeeID
		
class EmployeeManager:
	def Promote(self, obj):
		indx = obj.getDesignation()
		obj.setDesignation(lstDesignation[indx + 1])
		
	def Demote(self, obj):
		indx = obj.getDesignation()
		obj.setDesignation(lstDesignation[indx - 1])
	
def main():
	dctEmployee = {}
	print("1.Accept")
	print("2.Display")
	print("3.Promote")
	print("4.Demote")
	print("5.EXIT")
	ch = input("Enter choice:")
	while 5 != ch:
		if 1 == ch:
			szName, szAddress, szMaritalStatus, szDesignation = input("Enter name,address,marital status, desgination")
			obj = Employee(szName, szAddress, szMaritalStatus, szDesignation)
			dctEmployee[obj.getEmployeeID()] = obj
			print ("Employee ID:{}".format(obj.getEmployeeID()))
		elif 2 == ch:
			iEmpID = input("Enter employee ID:")
			if iEmpID in dctEmployee:
				print dctEmployee[iEmpID].getEmployee(iEmpID)
			else:
				print ("Employee not found")
		elif 3 == ch:
			iEmpID = input("Enter employee ID:")
			if iEmpID in dctEmployee:
				obj = EmployeeManager()
				obj.Promote(dctEmployee[iEmpID])
			else:
				print ("Employee not found")
		elif 4 == ch:
			iEmpID = input("Enter employee ID:")
			if iEmpID in dctEmployee:
				obj = EmployeeManager()
				obj.Demote(dctEmployee[iEmpID])
			else:
				print ("Employee not found")
		else:
			break
		ch = input("Enter choice:")
	
if __name__ == '__main__':
	main()
			
			
		
