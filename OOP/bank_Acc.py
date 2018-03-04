'''
WA simple bank account class which generates account number automatically and then
implement method withdraw, deposit, check balance.
'''
class BankAccount:
	AccountNumber = 1200
	dict of card respective to one user(accntnumber, cardobject)
	def __init__(self, balance = 0, bOpen = True):
		self.accnum = BankAccount.AccountNumber
		BankAccount.AccountNumber += 1
		self.balance = balance
		self.bOpen = bOpen
		
	def CloseAccount(self):
		self.bOpen = False
	
	def getBalance(self):
		if True == self.bOpen:
			return self.balance

	def getAccountNumber(self):
		if True == self.bOpen:
			return self.accnum

	def Deposit(self, amount):
		if True == self.bOpen:
			if amount > 0:
				self.balance += amount
	
	def Withdraw(self, amount):
		if True == self.bOpen:
			if amount > 0 and self.balance > 0:
				self.balance -= amount

class BankBranch:
	dctBankAccount = {}
	def __init__(atmobj):
		self.atmobj = atmobj
		
	def CreateAccount(self):
		obj = BankAccount(500)
		BankBranch.dctBankAccount[obj.getAccountNumber()] = obj
		return obj.getAccountNumber()
	
	def CloseAccount(self, iAccntNum):
		if iAccntNum in BankBranch.dctBankAccount:
			BankBranch.dctBankAccount[iAccntNum].CloseAccount()
			
	def DepostAmt(self, iAccntNum, iBal):
		if iAccntNum in BankBranch.dctBankAccount:
			BankBranch.dctBankAccount[iAccntNum].Deposit(iBal)
	
	def WithdrawAmt(self, iAccntNum, iBal):
		if iAccntNum in BankBranch.dctBankAccount:
			BankBranch.dctBankAccount[iAccntNum].Withdraw(iBal)
			
	def CheckBalance(self, iAccntNum):
		if iAccntNum in BankBranch.dctBankAccount:
			return BankBranch.dctBankAccount[iAccntNum].getBalance()

	#def Tranfer()
	
class ATM:
	def deposit()
	def withdraw()
	def checkbalance()
	def ministmt()
	def retruncardaccountobj()
	def adcard(cardobj,acountobj)
class Card:
	
	
def main():
	lstObj = {}
	print("1.Create Account.")
	print("2.Deposit Amount.")
	print("3.Withdraw Amount.")
	print("4.Check Balance.")
	print("5.EXIT.")
	ch = input("Enter choice:")
	while 5 != ch:
		if 1 == ch:
			obj = BankBranch()
			iAccnt = obj.CreateAccount()
			lstObj[iAccnt] = obj
			print("Your account number is:{}".format(iAccnt))
		elif 2 == ch:
			iAccountNum = input("Please enter account number:")
			if iAccountNum in lstObj:
				lstObj[iAccountNum].DepostAmt(iAccountNum, 10)
		elif 3 == ch:
			iAccountNum = input("Please enter account number:")
			if iAccountNum in lstObj:
				lstObj[iAccountNum].WithdrawAmt(iAccountNum, 10)
		elif 4 == ch:
			iAccountNum = input("Please enter account number:")
			if iAccountNum in lstObj:
				print lstObj[iAccountNum].CheckBalance(iAccountNum)
		elif 5 == ch:
			break
		ch = input("Enter choice:")

if __name__ == '__main__':
	main()
