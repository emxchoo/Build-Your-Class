Emily Ming Li Choo
README file 

CLASS DOCUMENTATION
Description of the class: Automated Teller Machine (ATM)
Class AutomatedTellerMachine contains data variables name and balance. 
User are able to deposit,withdraw, view the account balance. 

Description of the data variables:
- name are set to private variable self.__username
- balance are set to private variable self.__balance

Description of each methods:
set_name: This is to set the name of the private variable.
get_name: This is to access private variable self.__username and return it. 

set_balance: This is to set the balance of the private variable.
get_balance: This is to access private variable self.__balance and it will print out the balance of the user. 

deposit_money: 
- The user specified amount will be added to the existing balance. 
- It will show the balance deposited and the total balance after deposit. 

withdraw_money: 
- The user specified amount will be compared to the existing balance. 
- If the withdrawal amount is more than the existing balance, 
it will print out an error message to remind user to top up their balance.
- Else, it will show the withdrawal amount and remaining balance of the user. 

DEMO PROGRAM DOCUMENTATION
Description of the demo program:
The program allows user to access their bank account with their ID number.
They will be able to withdraw, deposit, view balance and exit the program. 
Each selection will lead to different output.

Instructions on how to run the demo program:
First, program will ask user to input their ID number. It can be any ID number between 1000 to 9999. 
If the ID number is out of range, it will ask user to re-enter their ID number again.

Secondly, program will show a list of selection. 
User can enter their selection depending on what they intend to do. 
The selections are 1 - View Balance, 2 - Withdraw, 3 - Deposit and 4 - Exit.

If user choose 1 - View Balance:
Program wil show the user's balance. 

If user choose 2 - Withdraw:
Program will ask how much they want to withdraw.
It will ask to verify the withdrawal amount. 
If the withdrawal amount is greater than the balance they have in their account, it will pop out an error message. 
If not, user will be able to withdraw the amount smoothly and show the remaining balance. 

If user choose 3 - Deposit:
Program will ask how much they want to deposit.
It will ask to verify the deposit amount. 
It will show the deposit money and the total balance. 

If user choose 4 - Exit:
Program will have a farewell note, show their transaction number and exit the program. 

If user choose other options, other than 1 to 4, it will have an error message. 









