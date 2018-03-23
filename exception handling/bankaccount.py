'''
Simple bank account class which generates account number automaticaly then implement method Withdraw deposite , CheckBalance
Menu driven program to simulate the bank account operation.
'''
class BankException(Exception):
	def __init__(self,amount):
		self.amount = amount
		
	def __str__(self):
		return "Not sufficient amount in account "+ str(self.amount)
		
class Bank():
	acc_no = 0
	def __init__(self, balance=0):
		Bank.acc_no += 1
		self.account_no = Bank.acc_no
		self.balance = balance
		
	def Withdarw(self, amount):
		if (self.balance < amount):
			#print "not sufficient amount in account."
			x = BankException(amount)
			raise x

		self.balance -= amount
		
	def Deposite(self, amount):
		self.balance += amount
		
	def CheckBalance(self):
		return self.balance
		
	def __repr__(self):
		return "Account No : " + str(self.account_no)+ "\n" + "Balance : " + str(self.balance)
		

def Menu():
	ch = input("1. Check Balance \n2. Deposite \n3. Withdraw \n0. Exit \nEnter operation : ")
	return ch

def main():
	
	acc1 = Bank(500)
	acc2 = Bank(1000)
	print acc1
	print acc2
	choice = Menu()
	
	while choice != 0:
		if choice == 1:
			print acc1
		elif choice == 2:
			amount = input("Enter amount to deposite : ")
			acc1.Deposite(amount)
			#print acc1
		elif choice == 3:
			amount = input("Enter amount to Withdraw : ")
			try:
				acc1.Withdarw(amount)
			except BankException as e:
				print e
			#print acc1
		else:
			print("Invalid choice ")
		choice = Menu()
		
if __name__=="__main__":
	main()
