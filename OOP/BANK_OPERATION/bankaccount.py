import datetime
from transaction import Transaction
class BankAccount:
	AccountNumber = 1200

	def __init__(self, balance = 0, bOpen = True):
		self.accnum = BankAccount.AccountNumber
		BankAccount.AccountNumber += 1
		objTranns = Transaction()
		self.objTransaction = objTranns
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
				(self.objTransaction).setactivity("Deposit", amount, self.balance, datetime.datetime.now())
				
	def Withdraw(self, amount):
		if True == self.bOpen:
			if amount > 0 and self.balance > 0 and (self.balance - amount) > 30:
				self.balance -= amount
				(self.objTransaction).setactivity("Withdraw", amount, self.balance, datetime.datetime.now())
				
	def gettransactionhistory(self):
		return (self.objTransaction).getactivity()