def total(a=0,b=0,c=0,*d,**e):
 #print(type(d))
 #print(type(e))
 total = a+b+c
 total+=sum(d)
 for key in e.keys():
  total += e[key]

 return total

def total1(a=0,b=0,c=0,*d,**e):
 #print(type(d))
 #print(type(e))
 total = a+b+c
 total+=sum(d)
 for key in e.keys():
  total += e[key]

 return total

#print(total(10,20,30))
#print(total())
#print(total(10,20,30,40,50))

#print(total(10,20,30,40,50, x=10,y=20,z=30))

if __name__ == '__main__':
 print(total(0))
else:
 print(total(10))
