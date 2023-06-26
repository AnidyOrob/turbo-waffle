import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('instruments.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM instruments")
    instruments = cursor.fetchall()
    conn.close()
    
    return render_template('index.html', instruments=instruments)

if __name__ == '__main__':
    app.run(debug=True)
