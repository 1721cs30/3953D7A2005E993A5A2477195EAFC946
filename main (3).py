#implementation of the bank account class
class BankAccount:
  def __init__(self,  account_number, account_holder_name, initial_balance=0):
       self.__account_number =account_number
       self.__account_holder_name =account_holder_name
       self.__account_balance =initial_balance

def deposit(self, amount):
       if amount > 0:
           self.__account_balance +=amount 
           print(f"Deposited ${amount}.New balance: ${self.__account_balance}")
       else:
          print("Invalid deposit amount. Amount must be greater than zero.")
 
       def withdraw (self, amount):
        if 0 < amount <= self.__account_balance:
           self.__account_balance -=amount
           print (f"withdraw ${amount}.New balance: ${self.__account_balance}")
        else:
         print("Insufficient funds or invalid withdrawal amount.")
         