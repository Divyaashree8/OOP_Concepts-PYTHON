from abc import ABC, abstractmethod
class Account(ABC):#abtract base class
  def __init__(self,account_holder,account_number,balance):
    self.account_holder=account_holder
    self.account_number=account_number
    self._balance=balance #private variable

  def deposite(self,amount):
     if amount>0:
        self.__balance +=amount
        print(f"${amount} deposited successfully.")
     else:
       print("Invaild amount! Deposite must be positive.")
  def display_details(self):
     print("\n---Account Details---)
     print(f"Account Holder:{self.account_holder}")
     print(f"Account Number:{self.account_number}")
     print(f"Balance:${self._balance}")
  @abstractmethod
  def withdraw(self,amount):
    pass
  # child class
  class SavingsAccount(Account):
    MIN_Balance=1000
    def withdraw(self,amount):
    if amount <=0:
      print("Invalid amount! withdrawal must be positive")
    elif amount> self._balance:
      print("Insufficient balance")
    elif self._balance - amount<self.MIM_Balance:
      print("Cannot withdraw, minimum balance must be maintained.") 
    else:
      self._balance-=amount
      print(f"${amount}withdrawn successfully from savings ac.")
# child class 2
class CurrentAccount(Account):
    Overdraft_limit=5000
    def withdraw(self,amount):
    if amount <=0:
      print("Invalid amount! withdrawal must be positive")
    elif amount> self.__balance + self.Overdraft_limit:
      print("Overdraft limit exceeded!")  
    else:
      self.__balance-=amount
      print(f"${amount}withdrawn successfully from current ac.")

s=SavingsAccount("Divya",12345,500000),
c=CurrentAccount("Shree",67895,500000)
s.display_details()
s.withdraw(2000)
c.diplay_details()
c.withdraw(5000)

