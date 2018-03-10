from bankbranch import BankBranch
from atmcard import Card
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

	def ministmt(self, iCardNumber):
		if iCardNumber in ATM.dctATMCard:
			obj = BankBranch()
			AccntObj = obj.getAccontObj((ATM.dctATMCard[iCardNumber]).getAccountNumber(iCardNumber))
			return AccntObj.gettransactionhistory()