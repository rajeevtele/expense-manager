import sqlite3

conn = sqlite3.connect("expenses.db")
c = conn.cursor()

# Get all table names
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = c.fetchall()

print("Tables in database:")
for table in tables:
    print(f" - {table[0]}")

conn.close()
