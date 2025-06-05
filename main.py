from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    user_input = request.form["user_input"]
    result = "positif" if "senang" in user_input.lower() else "negatif"
    return render_template("index.html", prediction=result, user_input=user_input)

if __name__ == "__main__":
    app.run(debug=True)
