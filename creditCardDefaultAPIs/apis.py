import flask
from flask import Flask, render_template, request
from keras.models import load_model
from sklearn import preprocessing
import numpy as np

app = Flask(__name__)

standardizer = preprocessing.StandardScaler()

model = load_model('model/creditCardDefault.h5')
print("[Model loaded]")

@app.route("/", methods=['GET', 'POST'])
def home():
    data =[]
    if flask.request.method == 'GET':
        return render_template("home.html")
    if flask.request.method == 'POST':
        balance = request.form['balance']
        data.append(int(balance))
        gender = request.form['gender']
        if gender == 'Male':
            gender = 1
        else:
            gender = 0
        data.append(gender)
        marital_status = request.form['marital_status']
        if marital_status == 'Single':
            marital_status = 1
        else:
            marital_status = 0
        data.append(marital_status)
        age = request.form['age']
        if age == 'Less than 30':
            age = 1
        elif age == '31-45':
            age = 2
        elif age == '46-65':
            age = 3
        else:
            age = 4
        data.append(age)
        pay = request.form['pay']
        data.append(int(pay))
        due = request.form['due']
        data.append(int(due))
        paid = request.form['paid']
        data.append(int(paid))
        education_status = request.form['education_status']
        if education_status == 'Graduate':
            data.append(1)
            data.append(0)
            data.append(0)
        elif education_status == 'High School':
            data.append(0)
            data.append(1)
            data.append(0)
        else:
            data.append(0)
            data.append(0)
            data.append(1)
        print(data)
        prediction = model.predict(standardizer.fit_transform(np.array([data])))
        prediction = (prediction > 0.5)
        print(prediction)
        return render_template("home.html", result=prediction,)
    
if __name__ == "__main__":
    app.run(debug=True)