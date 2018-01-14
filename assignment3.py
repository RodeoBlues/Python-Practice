numofstudents = int(input("# of Students:: "))
numofsubjects = int(input("# of Subjects:: "))

list = []
print("\n")
for i in range(numofsubjects):
    addedvalue = 0
    for j in range(numofstudents):
        addedvalue += int(input("subject #%d/student #%d:: " %(i+1, j+1)))
    list.append(addedvalue / numofstudents)

addedvalue = 0
print("\n")
for x in range(numofsubjects):
    print("The average of #%d:: %d" %(x+1,list[x]))
    addedvalue += list[x]
print("\n")
print("Final average is:: %d" %(addedvalue / numofsubjects))
