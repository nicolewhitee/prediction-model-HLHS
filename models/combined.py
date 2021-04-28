# Combination of all the machine learning models

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn as sk
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

df = pd.read_csv('data.csv', header=0)

# Dependent values vector
X = df[['BWT', 'PNUMSURG', 'SANATDX', 'ICUDAYS', 'SO2SAT']]
Y = df['fatal']

# Train the data
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.75)

# Neural Network model
NN = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
NN.fit(x_train, y_train)
nnprob = NN.predict_proba(x_test)

# Random Forest model
RF = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)
RF.fit(x_train, y_train)
rfprob = RF.predict_proba(x_test)

# Support Vector Machine model
SVM = svm.SVC(kernel='linear', probability=True)
SVM.fit(x_train, y_train)
svmprob = SVM.predict_proba(x_test)

# Logistic Regression model
lr = LogisticRegression(random_state=0, solver='lbfgs', multi_class='ovr')
lr.fit(x_train, y_train)
lrprob = lr.predict_proba(x_test)

fpr1, tpr1, thresh1 = roc_curve(y_test, nnprob[:,1], pos_label=1)
fpr2, tpr2, thresh2 = roc_curve(y_test, rfprob[:,1], pos_label=1)
fpr3, tpr3, thresh3 = roc_curve(y_test, svmprob[:,1], pos_label=1)
fpr4, tpr4, thresh4 = roc_curve(y_test, lrprob[:,1], pos_label=1)

randomprobs = [0 for i in range(len(y_test))]
p_fpr, p_tpr, _ = roc_curve(y_test, randomprobs, pos_label=1)

nnscore = roc_auc_score(y_test, nnprob[:,1])
rfscore = roc_auc_score(y_test, rfprob[:,1])
svmscore = roc_auc_score(y_test, svmprob[:,1])
lrscore = roc_auc_score(y_test, lrprob[:,1])

print(nnscore, rfscore, svmscore, lrscore)

# plot roc curves
plt.plot(fpr1, tpr1, linestyle='--',color='orange', label='Neural Network')
plt.plot(fpr2, tpr2, linestyle='--',color='green', label='Random Forest')
plt.plot(fpr3, tpr3, linestyle='--',color='blue', label='Support Vector Machine')
plt.plot(fpr4, tpr4, linestyle='--',color='brown', label='Logistic Regression')
plt.plot(p_fpr, p_tpr, linestyle='--', color='purple')
# title
plt.title('ROC curve')
# x label
plt.xlabel('False Positive Rate')
# y label
plt.ylabel('True Positive rate')

plt.legend(loc='best')
plt.savefig('roc.png')