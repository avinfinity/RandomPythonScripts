ctr = 1

while ctr != -1 :
 try:
  ctr = int(input('Enter a number ( -1 to exit) : '))
 except ValueError:
  print("That was not a number")
 else:
  #Only executed when no exception happens
  print("No exception happened")
 finally:
  print("finally executed")