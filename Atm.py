class Atm:
    def __init__(self,cardnumber,pin,amount):
        self.cardnumber = cardnumber
        self.pin = pin
        self.amount = amount

    def deposit(self,amountDeposit):
        amountDeposit = int(input("enter the money to be deposited - "))
        print("Your new balance is - " + amountDeposit)
        print("Thank you for your deposit")

    def check_balance(self, amount):
        print("Your balance is " + amount)

    def withdrawl(self,amount):
        amountWithdrwal = int(input("enter amount to be withdrawn"))
        new_amount =  amount - amountWithdrwal 
        print("you have withdrawn amount "+str(amountWithdrwal) +". Your remaining balance is "+ str(new_amount))

   
def main():
    Card_number = int(input("enter your card number:- "))
    pin_number  = int(input("enter your pin number:- "))

    new_user =  Atm(Card_number ,pin_number)

    print("Choose your activity ")
    print("1. Balance Enquriy \n   2. Withdrawl \n 3. Deposit")
    activity = int(input("enter activity number :- "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        amount = int(input("enter the amount:- "))
        new_user.withdrawl(amount)
    elif (activity == 3):
        amountD = int(input("enter the amount:- "))
        new_user.deposit(amountD)
    else:
        print("enter a valid number")
