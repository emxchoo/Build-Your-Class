#Emily Ming Li Choo
#Assignment 10.1 Your Own Class

#Used pythonguides.com to find out how to get 2 decimal places
#https://pythonguides.com/python-print-2-decimal-places/

#Used geeksforgeeks to find out how to create an account class with deposit and withdraw function
#https://www.geeksforgeeks.org/python-program-to-create-bankaccount-class-with-deposit-withdraw-function/

#Used W3school to find out how to use random.randit() method 
#https://www.w3schools.com/python/ref_random_randint.asp

#Used geeksforgeeks to find out more about get and set method
#https://www.geeksforgeeks.org/getter-and-setter-in-python/

#Importing random to have random numbers
import random
#Constructing class variable 
class AutomatedTellerMachine:
    #Initialize name and balance, these are the data variables 
    def __init__(self,name,balance):
        #setting both name and balance as private data varaibles
        self.__username = name
        self.__balance = balance

   #To set name
    def set_name(self,name):
        self.__username = name
    
    #To access private varaible self.__username
    def get_name(self):
        return self.__username
    
   #To set balance
    def set_balance(self,balance):
        self.__balance = balance
    
    #To access private variable self.__balance
    def get_balance(self):
        print(f"User {self.__username} has a balance of ${self.__balance:.2f}.")
         
    #Find out how much user deposited and the total of their account 
    def deposit_money(self,amount):
        total = self.__balance + amount
        self.__balance += amount
        print(f"User {self.__username} has deposited ${amount:.2f}.")
        print(f"Total Balance: ${total:.2f}")

    #Find out how much user withdrew and the remaining balance of their account
    def withdraw_money(self,amount):
        if amount > self.__balance:
            print("You do not have sufficient funds in your account. Please top up your balance.")
        else:
            remaining = self.__balance - amount 
            self.__balance -= amount
            print(f"User {self.__username} has withdrawn ${amount:.2f}.")
            print(f"Remaining Balance: ${remaining:.2f}.")
        
        
def main():
    print("Welcome to Emily's ATM!")
    
    #making a list of accounts 
    accounts = []
    #user can only choose from range 1000 to 9999 for their ID number
    for name in range(1000,9999):
        #calling class 
        account = AutomatedTellerMachine(name,2000)
        #appending the accounts
        accounts.append(account)

    #Using while loop method to run this program 
    while True:
        #asking user to input their ID number 
        id = int(input("Enter your ID number: "))

        #Not accepting any ID number below 1000 and over 9999
        while id < 1000 or id > 9999:
            id = int(input("Invalid ID. Please re-enter: "))
        while True:
            #ATM menu 
            print("1 - View Balance\t2 - Withdraw\t3 - Deposit\t4 - Exit")
            #User should choose whether they want to view balance, withdraw, deposit or exit the program
            selection = int(input("Enter your selection: "))
            
            #using for loop method to get account 
            for account in accounts:
                #using if,elif and else for selections
                if account.get_name() == id:
                    account_num = account

            #if user choose 1:view balance, they will be able to view their balance  
            if selection == 1:
                account_num.get_balance()

            #if user choose 2: withdraw, the program will deduct from balance 
            elif selection == 2:
                #user should input how much they want to withdraw
                amount = float(input("Enter amount to withdraw: "))
                amt = amount
                #program will ask to verify the withdrawal amount to be safe
                verify_withdrawal = input("Is this the correct amount, Yes or No?" + " "+ "$" + str(amount) + " ")
                #if answer is "Yes" or "yes" and the amount is sufficient to be withdrawn, it will proceed.
                if verify_withdrawal == "Yes" or verify_withdrawal == "yes" and amount <= 2000:
                    print("Withdrawal Verified. Please take your cash.")
                    account_num.withdraw_money(amount)
                
                else:
                    #if amount are insufficient to be withdrawn, program will ask user to top up their balance
                    #if amount are not correct, program will also ask user to input their amount again. 
                    print("Withdrawal Unsuccessful. Please top up your balance or re-enter your amount.")
                    print("Thank you for banking with us!")
                    break

            #if user choose 3: deposit, program will verify amount,add up the total and show the amount that are deposited
            elif selection == 3:
                amount = float(input("Enter amount to deposit: "))
                verify_deposit = input("Is this the correct amount? Yes or No?" + " " + str(amount) + " ")
                if verify_deposit == "Yes" or verify_deposit == "yes":
                    account_num.deposit_money(amount)
                    
                else:
                    #Program will end if user key in incorrect amount or would like to change their amount 
                    print("Deposit Unsuccessful. Please try again. Thank you for banking with us!")
                    break
            
            #if user choose 4: exit, program will print our their transaction number and end the program. 
            elif selection == 4:
                print("Transaction is now complete.")
                #using random.randint to generate the transaction number 
                print("Transaction number:", random.randint(0,1000000))
                #Farewell note
                print("Thank you for banking with us. Hope to see you soon!")
                print("Program Ended.")
                exit()
            
            else: 
                #if user chose other numbers, program will ask user to choose between 1 to 4
                print("That's invalid. Please choose options between 1 to 4.")
                break
                
if __name__ == "__main__":
    main()





