'''
WA simple bank account class which generates account number automatically and then
implement method withdraw, deposit, check balance.
'''
class BankAccount:
	AccountNumber = 1200
	
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
			if amount > 0 and self.balance > 0 and (self.balance - self.amount) > 30:
				self.balance -= amount
		
	
class BankBranch:
	dctBankAccount = {}
	
	def __init__(self):
		pass
		
	def CreateAccount(self, bWantCard):
		obj = BankAccount(500)
		BankBranch.dctBankAccount[obj.getAccountNumber()] = obj
		
		objATM = ATM()
		objATM.ApplyCard(obj.getAccountNumber(), bWantCard)
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
	
class ATM:

	dctATMCard = {}
	def __init__(self):
		pass
	
	def ApplyCard(self, iAccountNum, bWantCard = True):
		objCard = Card()
		iCardNumber = objCard.applyforcard(iAccountNum, bWantCard)
		ATM.dctATMCard[iCardNumber] = objCard 
		return iCardNumber
		
	def DepositATM(self, iCardNumber, iAmount):
		if iCardNumber in ATM.dctATMCard:
			obj = BankBranch()
			AccntObj = obj.getAccontObj((ATM.dctATMCard[iCardNumber]).getAccountNumber(iCardNumber))
			AccntObj.Deposit(iAmount)
	
	def WithdrawATM(self, iCardNumber, iAmount):
		if iCardNumber in ATM.dctATMCard:
			obj = BankBranch()
			AccntObj = obj.getAccontObj((ATM.dctATMCard[iCardNumber]).getAccountNumber(iCardNumber))
			AccntObj.Withdraw(iAmount)
			
	def BalanceATM(self, iCardNumber):
		if iCardNumber in ATM.dctATMCard:
			obj = BankBranch()
			AccntObj = obj.getAccontObj((ATM.dctATMCard[iCardNumber]).getAccountNumber(iCardNumber))
			return AccntObj.getBalance()

	#def ministmt()
	
class Card:
	cardnumber = 1900
	dctCardAccount = {}
	
	def __init__(self):
		pass
		
	def applyforcard(self, iAccountNum, bWantCard):
		if True == bWantCard:
			Card.cardnumber += 1
			Card.dctCardAccount[Card.cardnumber] = iAccountNum
			return Card.cardnumber
			
	def getAccountNumber(self, iCardNumber):
		if iCardNumber in Card.dctCardAccount:
			return Card.dctCardAccount[iCardNumber]
	
def main():
	lstObj = {}
	lstATMObj = {}
	print("1.Account Related transactions.")
	print("2.ATM related transactions.")
	print("3.EXIT.")
	ch = input("Enter choice:")
	while 3 != ch:
		if 1 == ch:
			print("1.Create Account.")
			print("2.Deposit Amount.")
			print("3.Withdraw Amount.")
			print("4.Check Balance.")
			print("5.EXIT.")
			ch = input("Enter choice:")
			while 5 != ch:
				if 1 == ch:
					iWantCard = input("Do you want card(0/1)??:")
					obj = BankBranch()
					iAccnt = obj.CreateAccount(iWantCard)
					lstObj[iAccnt] = obj
					print("Your account number is:{}".format(iAccnt))
					bWantCard = True
					if 0 == iWantCard:
						bWantCard = False
					objATM = ATM()
					iCardnum = objATM.ApplyCard(iAccnt, bWantCard)
					if True == bWantCard:
						lstATMObj[iCardnum] = objATM
					else:
						lstATMObj[iCardnum] = False
					print("Your card number is:{}".format(iCardnum))
				elif 2 == ch:
					iAccountNum = input("Please enter account number:")
					if iAccountNum in lstObj:
						lstObj[iAccountNum].DepostAmt(iAccountNum, 10)
					else:
						print("Invalid account number.")
				elif 3 == ch:
					iAccountNum = input("Please enter account number:")
					if iAccountNum in lstObj:
						lstObj[iAccountNum].WithdrawAmt(iAccountNum, 10)
					else:
						print("Invalid account number.")
				elif 4 == ch:
					iAccountNum = input("Please enter account number:")
					if iAccountNum in lstObj:
						print lstObj[iAccountNum].CheckBalance(iAccountNum)
					else:
						print("Invalid account number.")
				elif 5 == ch:
					break
				ch = input("Enter choice:")
		elif 2 == ch:
			print("1.Deposit Amount.")
			print("2.Withdraw Amount.")
			print("3.Check Balance.")
			print("5.EXIT.")
			ch = input("Enter choice:")
			while 5 != ch:
				if 1 == ch:
					iCardNumber = input("Please enter card number:")
					if iCardNumber in lstATMObj:
						lstATMObj[iCardNumber].DepositATM(iCardNumber, 100)
					else:
						print("Invalid card number.")
				elif 2 == ch:
					iCardNumber = input("Please enter card number:")
					if iCardNumber in lstATMObj:
						lstATMObj[iCardNumber].WithdrawATM(iCardNumber, 100)
					else:
						print("Invalid card number.")
				elif 3 == ch:
					iCardNumber = input("Please enter card number:")
					if iCardNumber in lstATMObj:
						print ("Balance is:".format(lstATMObj[iCardNumber].BalanceATM(iCardNumber)))
					else:
						print("Invalid card number.")
				elif 5 == ch:
					break
				ch = input("Enter choice:")
		elif 3 == ch:
			break
		print("1.Account Related transactions.")
		print("2.ATM related transactions.")
		print("3.EXIT.")
		ch = input("Enter choice:")

if __name__ == '__main__':
	main()
