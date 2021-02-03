from abc import ABCMeta, abstractmethod
from random import randint
class Account(metaclass = ABCMeta):
    @abstractmethod     # This is a decorator. We use an abstract method to inherit properties to the functions
    def createAccount():
        return 0
    def authenticate():
        return 0
    def Withdraw():
        return 0
    def Deposit():
        return 0
    def SeeBalance():
        return 0


class SavingsAccount(Account):  # the child class SavingsAccount inherents from the parent Account. 
        def __init__(self):
            self.savingsAccount= dict()
        def createAccount(self, name, deposit):
            self.accountNumber = randint(10000, 99999) # we put 5 numbers to generate a random 5-digit number 
            self.savingsAccount[self.accountNumber] = [name, deposit] # here we have created a key to store the account number
            print("Account creation has been successful. Your account number is:", self.accountNumber) # the account number displayed for a newly created account
        def authenticate(self, name, accountNumber):
            if accountNumber in self.savingsAccount.keys():  # return the key and the value of the dictionary --> check the self.savingsAccount=dict() we created on top
                if self.savingsAccount[accountNumber][0]==name:
                    print("Authentication is successful")
                    return True
                elif self.savingsAccount[accountNumber][0]!=name:
                    print("Authentication is not successful")
                    return False
        def Withdraw(self, withdrawalamount):
            if withdrawalamount > self.accountNumber[1]:
                print("Insufficient balance")
            else:
                self.savingsAccount[accountNumber][1] -= withdrawalamount # we substract the amount we withdraw by the total amount that exists in the account to get the new balance
                print("Withdrawal was successful")

        def Deposit(self, depositAmount):
            self.savingsAccount[accountNumber][1] += depositAmount # we add the deposit to the existing amount. 
            print("Deposit was successful")

        def SeeBalance(self, balanceAmount):
            print("Available balance in the account:", self.savingsAccount[self.accountNumber][1])

savingsAccount = SavingsAccount()
while True:        
   
    print("Enter 1 to create a new account")
    print('Enter 2 to enter your existing account')
    print("Enter 3 to exit the program")
    UserChoice= int(input())
    if UserChoice is 1:
        name = str(input())
        deposit = int(input())
        savingsAccount.createAccount(name, deposit)
    if UserChoice is 2:
        name=str(input())
        accountNumber=int(input())
        authenticationStatus = savingsAccount.authenticate(name, accountNumber) # this will yield a True or False statement
        if authenticationStatus is True:
            while True:
            print("Enter 1 to withdraw")
            print("Enter 2 to deposit")
            print("Enter 3 to see your balance")
            print("Enter 4 to go back to the initial screen")
            if UserChoice is 1:
                withdrawalamount=int(input())
                savingsAccount.Withdraw(withdrawalamount)
            elif UserChoice is 2:
                DepositAmount = int(input())
                savingsAccount.Deposit(depositAmount)
            elif UserChoice is 3:
                savingsAccount.SeeBalance()
            
            else:
                quit()
