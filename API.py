import flask
from flask import Flask
from flask import request
from sklearn.externals import joblib
from flask import Flask, redirect, url_for, request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

from flask_cors import CORS 

@app.route('/')

def defm():
    return '<h1>Sales Prediction</h1>' 


@app.route('/predict',methods=['GET'])

def prediction():
    from sklearn.externals import joblib
    import numpy as np
    model = joblib.load('Predict Sales.ml')

    input_retail = float(request.args.get('retail_price'))
    

    #input_retail = int(request.args['retail_price'])

    prediction = model.predict(np.array(input_retail).reshape(-1,1))
    prediction = prediction[0]

    return str(prediction)

    '''return str(model.predict(
        np.array(request.args['retail_price']).reshape(-1,1)))'''



if __name__ == "__main__":
    app.run(debug=True)
    
