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