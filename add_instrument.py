import sqlite3
from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/add_instrument', methods=['POST'])
def add_instrument():
    song_name = request.form['song_name']
    instrument_name = request.form['instrument_name']
    
    conn = sqlite3.connect('instruments.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO instruments (song_name, instrument_name) VALUES (?, ?)", (song_name, instrument_name))
    conn.commit()
    conn.close()
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
