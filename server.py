import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secrets,secrets,secrets'

@app.route("/")
def display_guess_form():
    if "randnum" in session:
        session.clear()
    session["randnum"] = random.randint(1, 100)
    return render_template("index.html")

@app.route("/get_guess", methods = ['POST'])
def get_guess_form():
    session["randguess"] = int(request.form["randguess"])
    return redirect("/answer")

@app.route("/answer")
def show_answer():
    return render_template("answer.html")

if __name__ == "__main__":
    app.run(debug = True)