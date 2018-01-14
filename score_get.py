#!/usr/bin/python3

import numpy as np
import pickle

with open('score_data.pickle','rb') as fp:
    score = pickle.load(fp)

for (subj,data) in score.items():
    print("%s: mean: %f, std: %f" % (subj, np.mean(data),np.std(data)))

sum = 0
num = 0 

for i in score['subj1']:
    sum += i
    num += 1

print(num)
print(sum)
print(sum/num)
