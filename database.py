import sqlite3
conn=sqlite3.connect("database.db")
cursor = conn.cursor()
cursor.execute("""
              CREATE TABLE IF NOT EXISTS resume(
               id INTEGER PRIMERY KEY,
               name TEXT,
               email,TEXT,
               score INTEGER
               )
               """)
conn.commit()
conn.close()