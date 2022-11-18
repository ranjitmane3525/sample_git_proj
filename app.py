
import pickle

import numpy as np
import pandas as pd
#import os
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods = ['GET','POST'])
def predict():
    
    #data = request.form

    #print(data)
    #u_data=np.array()
    name1 = request.form['name']
    u_data=float(request.form['experience'])
        
    
    print(u_data)  

    with open(r'model_lr.pkl','rb') as file:
         model1 = pickle.load(file)
         result1 =model1.predict([[u_data]])
         print(result1)
         var =int(result1[0][0])
   
    print(var)
    return render_template('index.html',nm =name1,result=var)

if __name__ == '__main__':
    app.run(host= "0.0.0.0",port=8080,debug=True)

