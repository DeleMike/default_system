c = [
  "Akindele Michael Olawole", 
  "single", 
  "22", 
  "male", 
  "university", 
  "100000", 
  "five_month_late", 
  "three_month_late", 
  "four_month_late", 
  "five_month_late", 
  "duly", 
  "one_month_early", 
  "3000", 
  "5000", 
  "2000", 
  "20000", 
  "17000", 
  "100", 
  "300", 
  "500", 
  "200", 
  "2000", 
  "1700", 
  "10"
]

customer = {

"marriage": "",
"age":"",
"sex": "",
"education": "",
"limit_bal": 0,
 "pay_0": "",
 "pay_2": "",
 "pay_3": "",
 "pay_4": "",
 "pay_5": "",
 "pay_6": "",
 "bill_amt1": 0,
 "bill_amt2": 0,
 "bill_amt3": 0,
 "bill_amt4": 0,
 "bill_amt5": 0,
 "bill_amt6": 0,
 "pay_amt1": 0,
 "pay_amt2": 0,
 "pay_amt3": 0,
 "pay_amt4": 0,
 "pay_amt5": 0,
 "pay_amt6": 0
}

# c = ['a', '2', '3']
# customer = {
#    '1':'',
#    '2':'',
#    '3':'',
# }

pos = 1
for key, value in customer.items():
   print('Pos is = ', pos)
   if pos == len(c): break
   value = c[pos]
   if value.isnumeric():
      value = int(value) 
   customer[key] = value
   pos += 1
print(customer)