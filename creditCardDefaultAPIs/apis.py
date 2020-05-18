from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict")
def predict():
    name = request.form['name']
    text = "Hello! "+name
    return render_template("results.html", result = text)
    
if __name__ == "__main__":
    app.run(debug=True)