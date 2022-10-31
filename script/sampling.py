#!/usr/bin/env python3
#
# https://imbalanced-learn.org/stable/over_sampling.html
#

import random
import sys
import pprint
from imblearn.over_sampling import RandomOverSampler

pp = pprint.PrettyPrinter()

features = []
for x in range(0, 10):
    random.seed(x)
    n = random.sample(range(1,101), k = 10)
    features.append(n)
labels = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

ros = RandomOverSampler(random_state=0)
features_bal, labels_bal = ros.fit_resample(features, labels)

print("features before sampling:")
pp.pprint(features)
print(f"labels before sampling:")
pp.pprint(labels)
print("\nfeatures after sampling:")
pp.pprint(features_bal)
print("labels after sampling:")
pp.pprint(labels_bal)

sys.exit()
