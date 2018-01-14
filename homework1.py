import numpy as np
import pickle

with open('score_data.pickle','rb') as fp:
    score = pickle.load(fp)

#adding the data and its quantity for each subject
sum_data = {}
amount_data = {}
over_90 = {}
below_50 = {}
temp_add = 0
temp_amount = 0
over_90_count = 0
below_50_count = 0
average_data = {}
variance_data = {}
std_data = {}

for (key, value) in score.items():
    over_90_count = 0
    below_50_count = 0
    sum_data[key] = sum(value)
    amount_data[key] = len(value)
    average = sum_data[key] / amount_data[key]
    average_data[key] = average
    variance_sum = 0
    for j in value:
        variance_sum += (average - j) ** 2
        if(j >= 90):
            over_90_count += 1
        elif(j <= 50):
            below_50_count += 1
    variance = variance_sum / amount_data[key]
    variance_data[key] = variance
    std_data[key] = variance ** 0.5
    over_90[key] = over_90_count
    below_50[key] = below_50_count
    temp_add = 0
    temp_amount = 0




#printing everything
for key in score.keys():
    print("Subject %s Average:: %f" %(key, average_data[key]))
    print("Subject %s Variance:: %f" %(key, variance_data[key]))
    print("Subject %s STD:: %f" %(key, std_data[key]))
    print("%d students have scored above 90 in Subject %s." %(over_90[key], key))
    print("%d students have scored below 50 in Subject %s." %(below_50[key], key))
    print("\n")


#finding the sum and the quantity of every data
total_sum = 0
total_amount = 0

for key in sum_data.keys():
    total_sum += sum_data[key]

for key in amount_data.keys():
    total_amount += amount_data[key]


#finding the average of all datas
total_average = total_sum / total_amount

#finding the total variance
total_variance = 0
temp_total_variance = 0

#totalVariance is final variable, create another one
for (key, value) in score.items():
    for j in range(amount_data[key]):
        temp_total_variance += (score[key][j] - total_average) ** 2


total_variance = temp_total_variance / total_amount
total_std = total_variance ** 0.5

print("Total Average:: %f" %(total_average))
print("Total Variance:: %f" %(total_variance))
print("Total STD: %f" %(total_std))
