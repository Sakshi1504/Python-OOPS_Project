class DFinances:
    def __init__(self,AccountHolders, Balance):
        self.AccountHolders=AccountHolders
        self.Balance=Balance

    def AccountOpen(self,AccountHolders):
        print("All the account holders: ", self.AccountHolders)
        name=input("Enter your name")
        adhar=input("Enter your adhar id")
        dObj.AlreadyACustomer(AccountHolders, adhar)
        self.AccountHolders.update({adhar:name})

    def AlreadyACustomer(self, AccountHolders, adhar):
        if adhar in self.AccountHolders.keys():
            print(f"{adhar} is already an Account an account holder in the bank.")
        else:
            print("Account has been opened in DFinances.")

    def displayBalance(self, Balance):
        print("Your Balance is: ", self.Balance)

    def WithdrawMoney(self, Amount, Balance):
        self.Balance-=Amount
        print("Your account balance is: ", self.Balance)

    def AddMoney(self, Balance, Amount):
        print("Current balance is: ", Balance)
        self.Balance=self.Balance+Amount
        print("Your Amount has been added successfully. Balance is :", self.Balance)

    def DeleteAccount(self, adhar):
        #AccountHolders.remove(adhar)
        self.AccountHolders.pop(adhar)
        print("All the account holders after deletion: ", self.AccountHolders)
        print("Your Account has been deleted successfully.")

if __name__=='__main__':
    AccountHolders={}
    Balance=0;
    dObj=DFinances(AccountHolders,Balance)
    while(True):
        print("Welcome to Dolli Finances. How may we help you?")
        print("1. Account Open")
        print("2. Check Balance")
        print("3. Add Money")
        print("4. Withdraw Money")
        print("5. Close my account")
        userchoice=input()

        if userchoice in ['1', '2', '3', '4', '5']:
            userchoice=int(userchoice)

        else:
            print("Please enter valid input.")

        if(userchoice==1):
            dObj.AccountOpen(AccountHolders)
        elif(userchoice==2):
            dObj.displayBalance(Balance)
        elif(userchoice==3):
            Amount=int(input("Enter the amount you want to add:"))
            dObj.AddMoney(Balance, Amount)
        elif(userchoice==4):
            Amount=int(input("Enter the amount you wish to Withdraw:"))
            dObj.WithdrawMoney(Amount, Balance)
        elif(userchoice==5):
            adhar=input("As you choose to delete your account with us, please enter your adhar id: ")
            dObj.DeleteAccount(adhar)

        choice=input("If you want to continue, press C, else to quit, press Q.")
        if choice=="Q" or choice=='q':
            quit()
        elif choice=="C" or choice=='c':
            continue
        else:
            print("Wrong Choice")

