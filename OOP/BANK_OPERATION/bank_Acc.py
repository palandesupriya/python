'''
WA simple bank account class which generates account number automatically and then
implement method withdraw, deposit, check balance.


Bank account add ATM class->Link card number to account number
create three different files
implement transfer
accept account holder name, branch name, bank name,blah blah blah
ATM class->Type,Card number, date expiry and issued, cvv, atm pin
In bank branch, 
'''
from bankbranch import BankBranch
from bankaccount import BankAccount
from ATM import ATM
from atmcard import Card
from transaction import Transaction

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
			print("4.Mini Statement.")
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
						print ("Balance is:{}".format(lstATMObj[iCardNumber].BalanceATM(iCardNumber)))
					else:
						print("Invalid card number.")
				elif 4 == ch:
					iCardNumber = input("Please enter card number:")
					if iCardNumber in lstATMObj:
						print ("Mini Stmt:{}".format(lstATMObj[iCardNumber].ministmt(iCardNumber)))
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