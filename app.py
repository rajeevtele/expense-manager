from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

DB_FILE = 'expenses.db'

# ✅ Initialize DB with table
def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT NOT NULL,
                    category TEXT NOT NULL,
                    description TEXT,
                    amount REAL NOT NULL
                )''')
    conn.commit()
    conn.close()

# ✅ Automatically called before first request
@app.before_first_request
def setup():
    init_db()

# ✅ Home Page - Show All Expenses
@app.route('/')
def index():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM expenses ORDER BY date DESC")
    expenses = c.fetchall()
    conn.close()
    return render_template('index.html', expenses=expenses)

# ✅ Add New Expense
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        date = request.form['date']
        category = request.form['category']
        description = request.form['description']
        amount = request.form['amount']
        
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute("INSERT INTO expenses (date, category, description, amount) VALUES (?, ?, ?, ?)",
                  (date, category, description, amount))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add.html')

# ✅ Edit Expense
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    if request.method == 'POST':
        date = request.form['date']
        category = request.form['category']
        description = request.form['description']
        amount = request.form['amount']
        c.execute("UPDATE expenses SET date = ?, category = ?, description = ?, amount = ? WHERE id = ?",
                  (date, category, description, amount, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    else:
        c.execute("SELECT * FROM expenses WHERE id = ?", (id,))
        expense = c.fetchone()
        conn.close()
        return render_template('edit.html', expense=expense)

# ✅ Delete Expense
@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("DELETE FROM expenses WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# ✅ Run locally (optional)
if __name__ == '__main__':
    app.run(debug=True)
