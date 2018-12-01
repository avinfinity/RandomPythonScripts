keepChecking = True
exitWord = {"X","QUIT"}

print("This programs checks if number is odd or even")
print("You may enter 'X', 'Quit' to exit any time")
print('\n')

while keepChecking:

    enterdNum = input ("Please enter any number : ")

    #One mthod to check if set contains a word
    if(exitWord.__contains__(enterdNum.upper())):
        break
    #using in keyword to check same 
    if(enterdNum.upper() in exitWord):
        break

    try:
        enteredVal = int(enterdNum)
        if(enteredVal % 2 == 0):
            print("Entered value " + enterdNum + " is EVEN number" )
        else:
            print("Entered value " + enterdNum + " is ODD number" )
    except(ValueError):
        print("Entered value was not a valid number. Please try again.")
