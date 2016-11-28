import flask as fl
from flask import render_template, redirect, url_for, request, session, flash, g
from functools import wraps
import sqlite3


DATABASE = 'blog.db'

app = fl.Flask(__name__)

app.secret_key = "Abelkyte"

def get_db():
    db = getattr(fl.g, '_database', None)
    if db is None:
        db = fl.g._database = sqlite3.connect(DATABASE)
        return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(fl.g, '_database', None)
    if db is not None:
        db.close()
#found a tutorial of login_required on stackoverflow-------->  http://stackoverflow.com/questions/19797709/what-is-a-self-written-decorator-like-login-required-actually-doing
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrap
#decorater
@app.route("/")
@login_required
#function
def home():
    cur = get_db().cursor()
    cur.execute("Select * from posts")
    posts = [dict(title=post[0], blog = post[1]) for post in cur.fetchall()]
    return render_template('index.html', posts=posts)

@app.route("/newpost")
def newpost():
    return render_template('newpost.html')
#adding arguments to HTTP methods
@app.route("/posting", methods = ['POST', 'GET'])
def posting():
    cur = get_db().cursor()
    conn = sqlite3.connect(DATABASE)
    curCon = conn.cursor()
    title = fl.request.form['title']
    blog = fl.request.form['blog']
    curCon.execute('INSERT INTO posts(title, blog) VALUES(?,?)',(title, blog))
    conn.commit()
    conn.close()

    cur.execute("Select * from posts")
    posts = [dict(title=post[0], blog = post[1]) for post in cur.fetchall()]
    return render_template('index.html', posts=posts)


@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        #setting up the username and pssord and error message
        if request.form['username'] != 'user' or request.form['password'] != 'user':
            error = 'Invalid! Please try again'
        else:
            session['logged_in'] = True
            #if password is correct it is assigned to the logged_in key and goes to home page, if incorrect the error message pops up and it stays in the same log in page
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

def connect_db():
    return sqlite3.connect(app.database)


if __name__ == '__main__':
    app.run(debug=True)
