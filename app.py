from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load the model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        input_data = [float(request.form["input1"])]  # Adapt based on your model
        prediction = model.predict([input_data])
        return render_template("form.html", prediction=prediction[0])
    return render_template("form.html", prediction=None)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')