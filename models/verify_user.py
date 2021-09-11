from test_heroku.models.database import sql_select
import bcrypt
import os
import psycopg2

DB_URL = os.environ.get("DATABASE_URL", "dbname=projectheroku")

def validate_password(email, password):
    user_found = sql_select("SELECT * FROM users WHERE email = %s", [email])
    if user_found == []:
        return False
    else:
        password_hash = user_found[0][4]
        return bcrypt.checkpw(password.encode(), password_hash.encode())

def user_id(email):
    results = sql_select("SELECT id FROM users WHERE email = %s", email)
    return results