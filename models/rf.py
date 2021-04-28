# A random forest model for prediciting the fatality of a Norwood procedure

import numpy as np
import pandas as pd
import sklearn as sk
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('data.csv', header=0)

# Dependent values vector
X = df[['BWT', 'PNUMSURG', 'SANATDX', 'ICUDAYS', 'SO2SAT']]
Y = df['fatal']

# Train the data
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)

RF = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)
RF.fit(x_train, y_train)
y_pred = RF.predict(x_test)

# Evaluation
cm = confusion_matrix(y_test, y_pred)

TP = cm[1][1]
TN = cm[0][0]
FP = cm[0][1]
FN = cm[1][0]

# Calculating accuracy, misclassification, sensitivity, specificity, precision, and f1 score
accuracy = (float (TP+TN) / float(TP + TN + FP + FN))
misclassification = 1 - accuracy
sensitivity = (TP / float(TP + FN))
specificity = (TN / float(TN + FP))
precision = (TN / float(TN + FP))
f1 = 2 * ((precision * sensitivity) / (precision + sensitivity))

print('Accuracy:', round(accuracy, 4))
print('Misclassification:', misclassification)
print('Sensitivity', sensitivity)
print('Specificity', specificity)
print('Precision', precision)
print('F1 score:', f1)