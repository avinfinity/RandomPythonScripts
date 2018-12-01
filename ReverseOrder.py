items = [1,2,3,4,5,6,7,8,9,10]
reversedItems = list()

#using custom reverse logic 
for x in range(0,len(items)):
    reversedItems.append(items[len(items) - 1 - x])

for item in reversedItems:
    print(str(item))

#using built in reverse iterator class
for item in reversed(items):
    print(str(item))