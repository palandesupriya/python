class Transaction:

	def __init__(self):
		self.lsttransact = []
	
	def setactivity(self, szActivity, iAmount, iBal, currtime):
		self.lsttransact.append(szActivity)
		self.lsttransact.append(iAmount)
		self.lsttransact.append(iBal)
		self.lsttransact.append(currtime)
			
	def getactivity(self):
		return self.lsttransact
