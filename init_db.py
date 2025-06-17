import sqlite3

conn = sqlite3.connect('expenses.db')
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    category TEXT NOT NULL,
    amount REAL NOT NULL,
    description TEXT
)
''')
conn.commit()
conn.close()
print("✅ expenses.db created.")
