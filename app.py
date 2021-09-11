from test_heroku.models.database import sql_select
from test_heroku.models.verify_user import user_id, validate_password
from flask import Flask, request, render_template, redirect, session
import psycopg2
import bcrypt
from models import verify_user, database, database_queries

app = Flask(__name__)

@app.route("/")
def index():
    render_template("index.html")

@app.route("/login", methods=["GET"])
def login_landing():
    render_template("login.html")

@app.route("/login", methods=["POST"])
def login_action():
    email = request.form.get("email")
    password = request.form.get("password")
    if validate_password(email, password):
        session['user_id'] = user_id(email)[0][0]
        redirect("/")
    else:
       redirect("/login")



@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route("/signup_action", methods=["POST"])
def signup_action():
    email = request.form.get("email")
    name = request.form.get("name")
    password = request.form.get("password")
    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    conn = psycopg2.connect("DB_URL")
    cur = conn.cursor()
    cur.execute("INSERT INTO users (email, name, password_hash) VALUES (%s, %s, %s)", [email, name, password_hash])
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)