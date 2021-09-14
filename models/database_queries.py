import os
from test_heroku.models.verify_user import user_id
import bcrypt
from test_heroku.models.database import sql_select, sql_write
from models import database
import psycopg2

DB_URL = os.environ.get("DATABASE_URL", "dbname=projectheroku")

def create_user(email, first_name, last_name, username, password):
    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    sql_write("INSERT INTO users (email, first_name, last_name, username, password_hash) VALUES (%s, %s, %s, %s, %s)", [email, first_name, last_name, username, password_hash])
    return

def new_post(user_id, post_content, post_title):
    sql_write("INSERT INTO posts (poster_id, post_content, post_title) VALUES (%s, %s)", [user_id, post_content, post_title])
    return

def get_posts():
    sql_select("SELECT * FROM posts ORDER BY ASC")
    return
