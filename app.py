
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__, template_folder='template', static_folder='static')
app.secret_key = 'your_secret_key'

# Simulated user storage
users = {}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/membership')
def membership():
    return render_template('membership.html')


@app.route('/registration', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confpassword = request.form['confpassword']
        terms = request.form.get('terms')

        # Simple validation (you can expand this)
        if password != confpassword:
            flash('Passwords do not match!', 'error')
            return redirect(url_for('register'))

        if not terms:
            flash('You must accept the terms and conditions!', 'error')
            return redirect(url_for('register'))

        # Simulate storing the user
        users[username] = {'email': email, 'password': password}

        flash('Registration successful!', 'success')
        return redirect(url_for('home'))

    return render_template('registration.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')
if __name__ == '__main__':
    app.run(debug=True)

