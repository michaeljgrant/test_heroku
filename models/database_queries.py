import os
import bcrypt
from models.database import sql_select, sql_write

DB_URL = os.environ.get("DATABASE_URL", "dbname=projectheroku")

#All CRUD functions for application


# Create user - password is passed through encryption before being written to database to secure passwords
def create_user(email, first_name, last_name, username, password):
    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    sql_write("INSERT INTO users (email, first_name, last_name, username, password_hash) VALUES (%s, %s, %s, %s, %s)", [email, first_name, last_name, username, password_hash])
    return
# When a new post is made with an image - this function runs to create the post in the database for rendering
def new_post(user_id, post_content, post_title, username, uploading_image):
    sql_write("INSERT INTO posts (poster_id, post_content, post_title, username, imageurl) VALUES (%s, %s, %s, %s, %s)", [user_id, post_content, post_title, username, uploading_image])
    return

# If there is no image found in the upload then this function runs to create a post without an imageurl
def new_post_without_image(user_id, post_content, post_title, username):
    sql_write("INSERT INTO posts (poster_id, post_content, post_title, username) VALUES (%s, %s, %s, %s)", [user_id, post_content, post_title, username])
    return

# Returns all posts from the database for rendering on the main page
def get_posts():
    results = sql_select("SELECT * FROM posts ORDER BY id DESC", [])
    return results

# Queries database for details of post for editing
def post_editor(post_id):
    results = sql_select("SELECT * FROM posts WHERE id = %s", [post_id])
    return results

# updates current post using image url of image if it already exists
def update_post(post_id, title, content, image_url):
    sql_write("UPDATE posts SET post_title = %s, post_content = %s, imageurl = %s WHERE id = %s", [title, content, image_url, post_id])
    return 

# if a new image is uploaded then it will replace the current image url using the Cloudinary response
def update_post_with_new_image(post_id, title, content, uploading_img):
    sql_write("UPDATE posts SET post_title = %s, post_content = %s, imageurl = %s WHERE id = %s", [title, content, uploading_img, post_id])
    return 

# Takes ID of post that is currently in editing page and deletes from database
def delete_post(id_to_delete):
    sql_write("DELETE FROM posts WHERE id = (%s)", [id_to_delete])
    return

# gets the user id from database for use with sessions
def getusername(user_id):
    results = sql_select("SELECT username FROM users WHERE id = %s", [user_id])
    return results