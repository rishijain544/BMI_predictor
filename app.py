from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# load model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    age = float(request.form["age"])

    children = float(request.form["children"])

    charges = float(request.form["charges"])

    sex = request.form["sex"]

    # encoding
    if sex == "male":
        sex = 1
    else:
        sex = 0

    # prediction
    features = np.array([[age, children, charges, sex]])

    prediction = model.predict(features)

    output = round(prediction[0], 2)

    # BMI category
    if output < 18.5:
        category = "Underweight"

    elif output < 25:
        category = "Normal"

    elif output < 30:
        category = "Overweight"

    else:
        category = "Obesity"

    return render_template(
        "index.html",
        prediction_text=f"Predicted BMI : {output}",
        category=category
    )

if __name__ == "__main__":
    app.run(debug=True)