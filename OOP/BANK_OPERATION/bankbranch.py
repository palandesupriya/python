#from ATM import ATM
from bankaccount import BankAccount
from atmcard import Card
class BankBranch:
	dctBankAccount = {}
	
	def __init__(self):
		pass
		
	def CreateAccount(self, bWantCard):
		obj = BankAccount(500)
		BankBranch.dctBankAccount[obj.getAccountNumber()] = obj
		
		#objATM = ATM()
		#objATM.ApplyCard(obj.getAccountNumber(), bWantCard)
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

	def getAccontObj(self, iAccntNum):
		if iAccntNum in BankBranch.dctBankAccount:
			return BankBranch.dctBankAccount[iAccntNum]
	