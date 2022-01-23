from flask import Flask,render_template,request
import pickle
import numpy as np

app = Flask(__name__)                       # Used to initialize app

model = pickle.load(open('model.pkl','rb'))

@app.route("/")                             # For making multiple pages
def hello_world():
    return render_template("index.html")
    # return "<p>Hello, World!</p>"

@app.route('/predict',methods=['POST','GET'])
def predict():

    area = int(request.form['AREA_name'])
    bkh = int(request.form['BHK_name'])
    bath = int(request.form['BATH_name'])
    balcony = int(request.form['BALCONY_name'])

    features =[[bkh,area,bath,balcony]]
    price = model.predict(features)
    output = "{:.2f}".format(price[0])

    return render_template('index.html',price='Price : {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)                     # if any error then it will be visible in the browser itself
    # app.run(debug=True,port = 8000)       # If you want to change the port

    # predict()
