class Atm(object):
    def __init__(self, cardnumber, pinnumber):
        self.cardnumber = cardnumber
        self.pinnumber = pinnumber
        self.balance = 100000
    def CashWithDraw(self):
        withdraw = int(input("How much cash do you want to withdraw from your bank account: "))
        self.balance = self.balance - withdraw
        print("You have ", self.balance, "left")

    def BalanceEnquiry(self):
        print("You have " ,self.balance ,  "in your account")

atm = Atm(123456789101213, "0824")
check = int(input("Enter 1 if you want to withdraw cash or Enter 2 if u want to check you balance: "))

if(check == 1):
    atm.CashWithDraw()
elif(check == 2):
    atm.BalanceEnquiry()
else:
    print("Error, please check your input or try again later")