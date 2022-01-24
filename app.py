from flask import Flask,render_template,request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl','rb'))

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET'])
def predict():

    area = int(request.form['AREA_name'])
    bkh = int(request.form['BHK_name'])
    bath = int(request.form['BATH_name'])
    balcony = int(request.form['BALCONY_name'])

    features =[[bkh,area,bath,balcony]]
    price = model.predict(features)
    output = "{:.2f}".format(price[0])

    return render_template('index.html',price='Price : {} Lakhs'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
