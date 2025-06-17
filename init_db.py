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

# Sample data
c.execute("INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?)",
          ('2025-06-01', 'Food', 120.50, 'Lunch at restaurant'))
c.execute("INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?)",
          ('2025-06-02', 'Travel', 60.00, 'Bus fare'))
conn.commit()
conn.close()
