import os
import psycopg2

DB_URL = os.environ.get("DATABASE_URL", "dbname=projectheroku")


# Database selector function 
def sql_select(query, params):
  conn = psycopg2.connect(DB_URL)
  cur = conn.cursor()
  cur.execute(query, params)
  results = cur.fetchall()
  cur.close()
  conn.close()
  return results

# Database write function
def sql_write(query, params):
  conn = psycopg2.connect(DB_URL)
  cur = conn.cursor()
  cur.execute(query, params)
  conn.commit()
  conn.close()


