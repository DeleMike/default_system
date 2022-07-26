#!/usr/bin/env python
# coding: utf-8

# # Default Payment System
# to check if a customer will pay her bills next month
# 
# 
# This is a practice project. I peformed some ml learing tecniques with the knowledge
# I have gained over the three chapters of ML Zoomcamp. Everything here is my opinion and I am very open to corrections.

# import necessary libraries
# get_ipython().run_line_magic('matplotlib', 'inline')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle
 
# !pip install xlrd -- install this library if not on machine! then you can comment it out again
df = pd.read_excel('default_of_credit_card_clients.xls', header=1)

print('Start data pre-processing')
# data pre-processing
df.columns = df.columns.str.lower().str.replace(' ', '_')

default_payment_next_month_values = {
    0: 'ok',
    1: 'default'
}
df.default_payment_next_month = df.default_payment_next_month.map(default_payment_next_month_values)

sex_values = {
    1: 'female',
    2: 'male',
    0: 'unk'
}
df.sex = df.sex.map(sex_values)

education_values = {
    1: 'graduate_school',
    2: 'university',
    3: 'secondary',
    4: 'primary',
    5: 'vocational',
    6: 'others',
    0: 'unk'
}
df.education = df.education.map(education_values)

marital_values = {
    1: 'married',
    2: 'single',
    3: 'others',
    0: 'unk'
}
df.marriage = df.marriage.map(marital_values)

pay_0_values = {
    -2: 'one_month_early',
    -1: 'duly',
    1: 'one_month_late',
    2: 'two_month_late',
    3: 'three_month_late',
    4: 'four_month_late',
    5: 'five_month_late',
    6: 'six_month_late',
    7: 'seven_month_late',
    0: 'unk'
}
df.pay_0 = df.pay_0.map(pay_0_values)

pay_2_values = {
    -2: 'one_month_early',
    -1: 'duly',
    1: 'one_month_late',
    2: 'two_month_late',
    3: 'three_month_late',
    4: 'four_month_late',
    5: 'five_month_late',
    6: 'six_month_late',
    7: 'seven_month_late',
    0: 'unk'
}
df.pay_2 = df.pay_2.map(pay_2_values)

pay_3_values = {
    -2: 'one_month_early',
    -1: 'duly',
    1: 'one_month_late',
    2: 'two_month_late',
    3: 'three_month_late',
    4: 'four_month_late',
    5: 'five_month_late',
    6: 'six_month_late',
    7: 'seven_month_late',
    0: 'unk'
}
df.pay_3 = df.pay_3.map(pay_3_values)

pay_4_values = {
    -2: 'one_month_early',
    -1: 'duly',
    1: 'one_month_late',
    2: 'two_month_late',
    3: 'three_month_late',
    4: 'four_month_late',
    5: 'five_month_late',
    6: 'six_month_late',
    7: 'seven_month_late',
    0: 'unk'
}
df.pay_4 = df.pay_4.map(pay_4_values)

pay_5_values = {
    -2: 'one_month_early',
    -1: 'duly',
    1: 'one_month_late',
    2: 'two_month_late',
    3: 'three_month_late',
    4: 'four_month_late',
    5: 'five_month_late',
    6: 'six_month_late',
    7: 'seven_month_late',
    0: 'unk'
}
df.pay_5 = df.pay_5.map(pay_5_values)

pay_6_values = {
    -2: 'one_month_early',
    -1: 'duly',
    1: 'one_month_late',
    2: 'two_month_late',
    3: 'three_month_late',
    4: 'four_month_late',
    5: 'five_month_late',
    6: 'six_month_late',
    7: 'seven_month_late',
    0: 'unk'
}
df.pay_6 = df.pay_6.map(pay_6_values)

df = df[df.default_payment_next_month != 'unk'].reset_index(drop=True)


df['default'] = (df.default_payment_next_month == 'default').astype(int)
del df['default_payment_next_month']
del df['id']
df = df[df.default != 'unk'].reset_index(drop=True)

categorical = ['sex', 'education', 'marriage', 'pay_0', 'pay_2', 'pay_3', 'pay_4', 'pay_5', 'pay_6']
numerical = ['limit_bal', 'age', 'bill_amt1', 'bill_amt2', 'bill_amt3', 'bill_amt4', 'bill_amt5', 'bill_amt6', 'pay_amt1',
             'pay_amt2', 'pay_amt3', 'pay_amt4', 'pay_amt5', 'pay_amt6']

df = df.fillna(0)
df.corr() # correlation table 

# this plot helps me to spot highest correlation
# plt.figure(figsize=(15,10))  
# sns.heatmap(df.corr(),annot=True,linewidths=.5, cmap="Blues")
# plt.title('Heatmap showing correlations between numerical data')
# plt.show()

# from here, we can see that bill_amt5 & bill_amt4 have the highest correlation
df.corr().unstack().sort_values(ascending = False)[20:30]

print('End data pre-processing')

# Setting up the Validation Framework
print('create validation framework')

df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)

df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=1)

df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

df_val.head()

y_train = df_train.default.values
y_val = df_val.default.values
y_test = df_test.default.values

df_train = df_train.drop('default', axis=1)
df_val = df_val.drop('default', axis=1)
df_test = df_test.drop('default', axis=1)

# ROC AUC could also be used to evaluate feature importance of numerical variables
print('finish validation framework')

# begin training
print('start training...')

train_dict = df_train[categorical + numerical].to_dict(orient='records')
dv = DictVectorizer(sparse=False)
X_train = dv.fit_transform(train_dict)

model = LogisticRegression(solver='liblinear', C=1.0, max_iter=1000)
model.fit(X_train, y_train)


val_dicts = df_val[categorical + numerical].to_dict(orient='records')
X_val = dv.transform(val_dicts)

y_pred = model.predict_proba(X_val)[:, 1]

accuracy_score(y_val, y_pred >= 0.5).round(3)

print('end training')

# saving the model
print('saving model...')
output_file = 'model_C=1.0.bin'

with open(output_file, 'wb') as f_out:
    pickle.dump((dv, model), f_out)

print('finished saving model...')