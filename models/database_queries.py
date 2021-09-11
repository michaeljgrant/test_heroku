import os
import bcrypt
from test_heroku.models.database import sql_select, sql_write
from models import database
import psycopg2

DB_URL = os.environ.get("DATABASE_URL", "dbname=projectheroku")

def create_user(email, first_name, last_name, username, password):
    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    sql_write("INSERT INTO users (email, first_name, last_name, username, password_hash) VALUES (%s, %s, %s, %s, %s)", [email, first_name, last_name, username, password_hash])
    return

def new_post():
    return
