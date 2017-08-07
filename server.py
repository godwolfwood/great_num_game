from flask import Flask, request, render_template, session, redirect 
import random

app = Flask(__name__)
app.secret_key = "twinjuan"

@app.route('/')
def index():
    if not 'random' in session:
        session['random'] = random.randrange(0, 101)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    session["guess"] = int(request.form['guess'])
    print session
    return redirect("/")

@app.route('/reset', methods=['POST'])
def reset():
    session['random'] = str(random.randrange(0, 101))
    session["guess"] = None
    return redirect("/")

app.run(debug=True)
