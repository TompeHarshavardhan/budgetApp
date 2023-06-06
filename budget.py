class Category:
  name=''
  def __init__(self,l):
    self.balance=0
    self.name=l
    self.ledger=list()
    self.totalwithdrawal=0
  def check_funds(self,amount:int):
    if amount>self.balance:
      return False
    else:
      return True
  def deposit(self,amount:int,description=""):
    self.balance+=amount
    self.ledger.append({'amount':amount,'description':description})
  def withdraw(self,amount:int,description=""):
    if self.check_funds(amount):
      self.balance-=amount
      self.totalwithdrawal+=amount
      self.ledger.append({'amount':-1*amount,'description':description})
      return True
    else:
      return False
  def transfer(self, amount:int,otherbudgetname=""):  
    if self.check_funds(amount):
      des1='Transfer to '+otherbudgetname.name
      self.withdraw(amount,des1)
      des2='Transfer from '+self.name
      otherbudgetname.deposit(amount,des2)
      return True
    else:
      return False
    
  def get_balance(self):
    return self.balance
  
  def __str__(self):
    fs='*' * int((30-len(self.name))/2) + self.name +'*' * int((30-len(self.name))/2)+'\n'
    for i in self.ledger:        
        fs+=str(i['description'])[0:23]
        fs+=' '*(23-len(i['description']))
        fs+=' '*(7-len("{:.2f}".format(i['amount'])))
        fs+=str("{:.2f}".format(i['amount']))
        fs+='\n'
    fs+="Total: "+str(self.balance)
    return fs
    
def create_spend_chart(categories:list()):
  string='Percentage spent by category\n'
  percentages=list()
  names=list()
  for i in categories:
    percentages.append(i.totalwithdrawal)
    names.append(i.name)
  tots=0
  for a in percentages:
    tots+=a

  for i in range(len(percentages)):
    percentages[i]=percentages[i]/tots
    percentages[i]=(percentages[i]*100)
    percentages[i]=int(percentages[i]/10)
  
  for i in reversed(range(11)):
    if(i==0):
        string+='  '+str(i*10)+'|'
    elif(i==10):
        string+=''+str(i*10)+'|'
    else:
        string+=' '+str(i*10)+'|'
    for j in percentages:
        if j>=i:
          string+=' o '
        else:
          string+='   '
    string+=' \n'
  string+='    '+'---'*len(percentages)+'-\n'
  m=0
  for i in names:
    if(len(i)>m):
      m=len(i)
  for i in range(m):
    string+='    '
    for j in range(len(percentages)):
      if i>=len(names[j]):
        string+='   '
      else:  
       string+=' '+names[j][i]+' '
    if(i==m-1):
        string+=' '
    else:
        string+=' \n'

  return string   


