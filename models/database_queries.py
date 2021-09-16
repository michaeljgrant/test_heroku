import os
import bcrypt
from models.database import sql_select, sql_write
import psycopg2

DB_URL = os.environ.get("DATABASE_URL", "dbname=projectheroku")

def create_user(email, first_name, last_name, username, password):
    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    sql_write("INSERT INTO users (email, first_name, last_name, username, password_hash) VALUES (%s, %s, %s, %s, %s)", [email, first_name, last_name, username, password_hash])
    return

def new_post(user_id, post_content, post_title, username, uploading_image):
    sql_write("INSERT INTO posts (poster_id, post_content, post_title, username, imageurl) VALUES (%s, %s, %s, %s, %s)", [user_id, post_content, post_title, username, uploading_image])
    return

def get_posts():
    results = sql_select("SELECT * FROM posts", [])
    return results

def post_editor(post_id):
    results = sql_select("SELECT * FROM posts WHERE id = %s", [post_id])
    return results

def update_post(post_id, title, content):
    sql_write("UPDATE posts SET post_title = %s, post_content = %s WHERE id = %s", [title, content, post_id])
    return 

def delete_post(id_to_delete):
    sql_write("DELETE FROM posts WHERE id = (%s)", [id_to_delete])
    return

def getusername(user_id):
    results = sql_select("SELECT username FROM users WHERE id = %s", [user_id])
    return results