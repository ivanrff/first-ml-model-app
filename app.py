# this is a basic Flask app to gather data from the form.html and predict a new value
# the new value uses model.pkl as a pre-trained model

# Importing flask to create the app, request to grab the data and render_template to display the html page
from flask import Flask, request, render_template
# Importing picke to load the saved machine learning model (model.pkl)
import pickle

app = Flask(__name__) # Creates a new Flask app instance, __name__ tells Flask where to find the files

# Load the model
with open("model.pkl", "rb") as f: # this opens the model in read binary mode ("rb")
    model = pickle.load(f) # adds the model to the variable model

@app.route("/", methods=["GET", "POST"]) # this is allowing GET and POST methods on the homepage ('/')
# GET works when a user visits the page (load the page)
# POST happens when a user submits a form (send the data)
def index(): # this function will run when the '/' homepage is accessed
    if request.method == "POST": # if the form is submitted, proceed:
        input_data = [float(request.form["input1"])]  # grabs the form field called "input1" in the form.html, float to change it to numeric input, and wrapped in a list so to expect more than 1 input
        prediction = model.predict([input_data]) # this gets the prediction from the model
        return render_template("form.html", prediction=prediction[0]) # this returns the form and shows the prediction
    return render_template("form.html", prediction=None) # if it's a GET request, it only shows the homepage without a prediction

if __name__ == "__main__": # this is run if this file is run directly as opposed to being imported
    app.run(  # starts the Flask app
        debug=True, # shows errors in the browser if something goes wrong (remove for deployment)
        host='0.0.0.0' # this makes the app accessible from outside of the container which is important for Docker
    )