class mgm:
 def walm(self):
  print("walk - mgf")

class mgf:
 def walk3(self):
  print("walk - mgf")

class pgm:
 def walk5(self):
  print("walk - pgm")

class pgf:
 def walk6(self):
  print("walk - pgf")

class  mom(mgm,mgf):
 def walk2(self):
  print("walk - mom", id(self))
 
 def __init__(self):
  print("object created sucessfully")

 def __del__(self):
  print("object destroyed")

class dad(pgm,pgf):
 def walk4(self):
  print("walk - dad")

class infant(mom,dad):
 "Help on infant class - docstring"

 def walk1(self):
  #print(type(self))
  print("walk - infant")


#mother = mom()
#mother.walk()
#print("id of mother is " , id(mother))
#del(mother)
#print("This is the last statement")

baby = infant()
#baby.walk()