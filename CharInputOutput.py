
# Validation of name which checks that no number should be there
def containsDigits(nameToBeValidated=""):
    ###Checks whether string is a digit or not
    # Input : any string value which nees to be validated
    # Output: bool indicating whether its digit or not 

    if(nameToBeValidated.isdigit()):
        return True
    else:
        return False

#Validation of age which checks that only numeric characters must be there
def IsNumber(numToBeValidated):
    try:
        int(numToBeValidated)
        return True
    except(ValueError):
        return False

name =  input("Please enter your name :")
print("You entered :" + name)

keepChecking = True

while(keepChecking):
    enterdVal = input("Enter any number : ")
    if(containsDigits(enterdVal)):
        print("You entered :" + enterdVal)
        keepChecking = False
    else:
        print("You did not entered a number. Please try again.")


