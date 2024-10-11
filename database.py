import sqlite3

con = sqlite3.connect("test_db.db")

cur = con.cursor()

def create_tables():
    cur.execute("CREATE TABLE users(name, password)")
    cur.execute("CREATE TABLE answers(user_id, question, answer)")

response = cur.execute("SELECT * FROM answers")

print(response.fetchall())
