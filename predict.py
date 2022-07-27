import pickle

from flask import Flask, render_template, request, jsonify

model_file = 'model_C=1.0.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask(__name__, template_folder='templates')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
   # for API request
   #  =request.get_json()
   '''
   For rendering results on HTML GUI
   '''
   customer_features = [x for x in request.form.values()]

   customer = {

        "marriage": "",
        "age": "",
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

   pos = 1
   for key, value in customer.items():
      if pos == len(customer_features):
         break
      value = customer_features[pos]
      if value.isnumeric():
         value = int(value)
      customer[key] = value
      pos += 1

   # return jsonify(customer)

   X= dv.transform([customer])
   y_pred = model.predict_proba(X)[0,1]
   print('y_pred  = ', y_pred)   
   default = y_pred > 0.5
   prediction_text = ''
   if bool(default):
      prediction_text = 'This customer WILL default on next payment'
   else:
      prediction_text = 'This customer will NOT default on next payment'

   result = jsonify( {
      'default_probabilty': float(y_pred),
      'default': bool(default),
      'prediction_text': prediction_text,
   })

   return render_template('index.html', prediction_text=prediction_text)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
