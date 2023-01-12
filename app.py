from flask import Flask # Flask is the class
from flask import render_template #Jinja2 template engine that speeds up web development

app = Flask(__name__) # app is an instance of the Flask class; first argument __name__ is the name of the app's module or package

@app.route("/") # route decorator tells Flask what url should trigger our function
def home(): # Function returns the message we want to dispaly in the user's browser (default is HTML)
    return render_template("index.html")


@app.route('/new-workout') # page designed to obtain all the relevant workout information from user
def log_workout():
    return render_template("new-workout.html")

@app.route("/history") # pages that shows user their workout history
def workout_history():
    return render_template

if __name__ == "__main__":
    app.run(debug=True)