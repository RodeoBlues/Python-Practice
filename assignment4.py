print("\n")
stuQ = int(input("# of students:: ")) #student Quantatity
subQ = int(input("# of subjects:: ")) #subject Quantatity


tempList = []
finalList = []
add = 0
averages = []
variances = []

for i in range(subQ):

    add = 0
    tempList = []
    print("\n")
    for j in range(stuQ):
        inputter = int(input("subject #%d/student #%d:: " %(i+1, j+1)))
        tempList.append(inputter)
        add += inputter
    tempAverage = add/stuQ

    averages.append(tempAverage)

    add = 0

    for j in range(stuQ):
        add += (tempList[j] - tempAverage) ** 2

    variances.append(add/stuQ)

    finalList.extend(tempList)



print("\n")

for i in range(subQ):
    print("Subject #%d Average: %f" %(i+1,averages[i]))
    print("Subject #%d Variance: %f" %(i+1, variances[i]))
    print("Subject #%d Standard Deviation: %f" %(i+1, (variances[i])**(1/2)))
    print("\n")



limit = len(finalList)


add = 0
for i in range(limit):

    add += finalList[i]



finalAverage  = add / (stuQ * subQ)
print("Final Average: %f" %(finalAverage))

add = 0

for i in range(limit):
    add += (finalList[i] - finalAverage) ** 2

print("Final Variance: %f\n" %(add / (stuQ*subQ)))
