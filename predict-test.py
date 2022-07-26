#!/usr/bin/env python
# coding: utf-8
import requests

url = 'http://localhost:9696/predict'

customer = {'sex': 'female',
 'education': 'secondary',
 'marriage': 'single',
 'pay_0': 'two_month_late',
 'pay_2': 'two_month_late',
 'pay_3': 'two_month_late',
 'pay_4': 'three_month_late',
 'pay_5': 'one_month_late',
 'pay_6': 'two_month_late',
 'limit_bal': 100000,
 'age': 26,
 'bill_amt1': 107643,
 'bill_amt2': 109895,
 'bill_amt3': 93420,
 'bill_amt4': 73119,
 'bill_amt5': 73642,
 'bill_amt6': 71579,
 'pay_amt1': 4048,
 'pay_amt2': 3105,
 'pay_amt3': 2700,
 'pay_amt4': 2510,
 'pay_amt5': 2703,
 'pay_amt6': 2700}

response = requests.post(url, json=customer).json()
print(response)

if response['default']:
   print('Customer will default')
else:
   print('Customer will not default')


