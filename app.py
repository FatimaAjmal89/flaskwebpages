# app.py

from flask import Flask, render_template



app = Flask(__name__, template_folder='template',static_folder='static')  # Ye line ensure kare ke Flask ko templates folder mile

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/membership')
def membership():
    return render_template('membership.html')





if __name__ == '__main__':
    app.run(debug=True)

