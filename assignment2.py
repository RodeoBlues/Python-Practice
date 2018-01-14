numofstudents = int(input("# of Students:: "))

addedvalue = 0

for i in range(numofstudents):
    addedvalue += int(input("Enter Score:: "))
    #addedvalue = addedvalue + int(input("Enter Score:: "))

print("%d" %(addedvalue/numofstudents))
