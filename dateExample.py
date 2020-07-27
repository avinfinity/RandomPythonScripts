import math

class Date:
 def __init__(self):
  self.dd = 25
  self.mm=11
  self.yy=2019

 def display(self):
  print(self.dd,self.mm,self.yy)

 def __add__(self,days):
  #validate days
  #inc = math.floor((days / 365))
  #self.yy += math.floor(inc)
  #self.dd = (days / 365) - 

  self.dd += days
  while (self.dd > 28):
   if self.dd > 31 and self.mm in (1,3,5,7,8,10,12):
    self.dd -= 31
    self.mm += 1
    if self.mm == 13:
     self.mm == 1
     self.yy += 1
   elif self.dd > 30 and self.mm in (4,6,9,11):
    self.dd -= 30
    self.mm += 1
    if self.mm == 13:
     self.mm == 1
     self.yy += 1
   elif self.dd == 30 or self.dd == 31 or self.dd < 28
    break
  return self

today = Date()
today.display()

tomorrow = today + 365
tomorrow .display()