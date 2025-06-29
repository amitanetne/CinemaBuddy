from flask import Flask, render_template, request, redirect, url_for, session
from ml_model import make_prediction 
from functools import wraps

app = Flask(__name__)
app.secret_key = 'mysecret' #our secret key

# users
users = {
    'Kanishk': 'kanishk123',
    'Aditya': 'aditya123',
    'Rachit': 'rachit123',
    'Renuka': 'renuka123',
    'Anshika': 'anshika123',
    'Amita': 'amita123'
    }

#this is for required login
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function
#theme
@app.before_request
def ensure_theme():
    if 'theme' not in session:
        session['theme'] = 'light'  
#home route
@app.route('/')
def home():
    return redirect(url_for('login'))
#login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('welcome'))
        else:
            return render_template('login.html', error="Invalid credentials. Try again.")
    return render_template('login.html')
#signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm = request.form['confirm']

        if username in users:
            return render_template('signup.html', error="Username already exists.")
        if password != confirm:
            return render_template('signup.html', error="Passwords do not match.")

        users[username] = password
        session['username'] = username
        return redirect(url_for('welcome'))
    return render_template('signup.html')
#welcome route
@app.route('/welcome')
def welcome():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('welcome.html', username=session['username'])
#predict
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        director = request.form['director']
        actors = request.form['actors']
        censor = request.form['censor']
        genre = request.form['genre']
        runtime = int(request.form['runtime'])

        ratings, gross, success = make_prediction(director, actors, censor, genre, runtime)

     
        return redirect(url_for('result', rating=ratings, gross=gross, success=success))

    return render_template('predict.html', prediction=False, username=session['username'])
#predicted result route
@app.route('/result')
@login_required
def result():
    rating = request.args.get('rating', type=float)
    gross = request.args.get('gross', type=float)
    success = request.args.get('success')
    username = session.get('username', 'User') 
    return render_template('result.html',rating=rating,gross=gross,success=success,username=username)
                           
# logout route                        
@app.route('/logout')
def logout():
    session.clear()
    return render_template('logout.html')
#toggle theme route for theme
@app.route('/toggle_theme')
def toggle_theme():
    current = session.get('theme', 'light')
    session['theme'] = 'dark' if current == 'light' else 'light'
   
    return redirect(request.referrer or url_for('welcome'))
#main run fun
if __name__ == '__main__':
    app.run(debug=True)
