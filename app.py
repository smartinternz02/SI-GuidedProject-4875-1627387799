# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 17:30:19 2021

@author: Lenovo
"""

from flask import Flask,reuest,render_template
import joblib
model=joblib.load('model.save')
trans=joblib.load('scalar.save')

app= Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/y_predict',methods=['POST'])
def y_predict():
    x_test=[[x for x in request.form.values()]]
    print(x_test)
    if x_test[0][0]:=='Male':
        x_test[0][0]=1
    else:x_test[0][0]=0  
    print(x_test)
    x_test=trans.transform(x_test)
    print(x_test)
    prediction=model.predict(x_test)
    output=prediction[0]
    if output==0:
        pred="Will not purchase"
    else:pred="Will Purchase"
    return render_template('index.html', prediction_text='Output {}'.format(pred))    
        
if __name__=='__main__':
    app.run(debug=True)
  