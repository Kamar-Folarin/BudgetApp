#Instantiating class category for different categories of budget
class Budget:
  def __init__(self, category): 
        self.ledger =[]
        self.amount=0
        self.category = category 

#Function to check the amount of available balance 
  def check_funds(self,amount):
    if self.amount< amount:
      return False
    else:
      return True

#Function to deposit money with a description of what the money is for and add it to the initiaL balance
  def deposit(self,amount, description=""):
    self.ledger.append({"amount":amount,"description":description})
    self.amount += amount

#Function to withdraw money for a particular category of budget and remove it from available balance
  def withdraw(self,amount,description=""):
    if self.check_funds(amount) ==True:
      self.amount -=amount
      self.ledger.append({"amount":-amount,"description":description})
      return True
    else:
      return False

  # return balance of budget 
  def get_balance(self):
    return self.amount

#Function to transfer money between categories
  def transfer(self,amount,category):
    if self.check_funds(amount)==True:
      self.amount-=amount
      self.ledger.append({"amount": -amount,"description":"Transfer to "+category.category})
      category.ledger.append({"amount": amount,"description": "Transfer from "+self.category})
      return True
    else:
      return False








#A method that shows a sample output of the description of transactons performed in a particular category e.g. Food category of budget
  def __str__(self):
    result=""
    result+="*************Food*************"+"\n"
    for transaction in self.ledger:
      amount=0
      description=""
      for key,value in transaction.items():
          if key=="amount":
            amount = value
          elif key=="description":
            description=value
      if len(description)>23:
        description=description[:23]
      amount = str(format(float(amount),'.2f'))
      if len(amount)>7:
        amount= amount[:7] 
      result+= description + str(amount).rjust(30-len(description))+"\n"
    result+="Total: "+str(format(float(self.amount),'.2f'))
    return result


