from models.database import sql_select
import bcrypt
import os
import psycopg2

DB_URL = os.environ.get("DATABASE_URL", "dbname=projectheroku")

# Password validator for login page - checks that the email exists that has been entered and then checks the password of that user
# against the password hash usingg bcrypt
def validate_password(email, password):
    user_found = sql_select("SELECT * FROM users WHERE email = %s", [email])
    if user_found == []:
        return False
    else:
        password_hash = user_found[0][5]
        return bcrypt.checkpw(password.encode(), password_hash.encode())

# Finds the user based on email provided
def user_id(email):
    results = sql_select("SELECT * FROM users WHERE email = %s", [email])
    return results

