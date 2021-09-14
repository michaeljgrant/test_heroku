from models.database_queries import create_user, get_posts, new_post, update_post, post_editor
from models.verify_user import user_id, validate_password
from flask import Flask, request, render_template, redirect, session

import psycopg2
import bcrypt
import os
SECRET_KEY = os.environ.get("SECRET_KEY", "Totally Secure Fallback Secret Key")
DB_URL = os.environ.get("DATABASE_URL", "dbname=projectheroku")
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
@app.route("/")
def index():
    user_id = session.get('user_id')
    user_name = session.get('user_name')
    results = get_posts()
    print(results)
    render_template("index.html", user_id=user_id, user_name=user_name, results = results)

@app.route("/login", methods=["GET"])
def login_landing():
    render_template("login.html")

@app.route("/login", methods=["POST"])
def login_action():
    email = request.form.get("email")
    password = request.form.get("password")
    if validate_password(email, password):
        session['user_id'] = user_id(email)[0][0]
        session['user_name'] = user_id(email)[0][3]
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
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    username = request.form.get("username")
    password = request.form.get("password1")
    create_user(email, first_name, last_name, username, password)
    return redirect("/")

@app.route("/addpost", methods=['GET'])
def create_screen():
    return render_template("addpost.html")

@app.route("/addpost", methods=['POST'])
def create_a_post():
    user_id = request.form.get("user_id")
    post_content = request.form.get("post_content")
    post_title = request.form.get("post_title")
    new_post(user_id, post_content, post_title)
    return redirect("/")

@app.route("/edit_post", methods=["GET"])
def edit_post_landing():
    post_id = request.args.get("id") 
    results = post_editor(post_id)
    return render_template("edit.html", post_id=post_id, results=results)

@app.route("/edit_post", methods=["POST"])
def edit_post_entry():
    post_id = request.form.get("id")
    title = request.form.get("title")
    content = request.form.get("content")
    update_post(post_id, title, content)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)