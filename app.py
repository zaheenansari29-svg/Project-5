from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Database Setup Function
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# 1. HOME ENDPOINT
@app.route('/')
def home():
    return jsonify({"message": "Welcome to Python REST API Project"})

# 2. GET ALL USERS (Read)
@app.route('/users', methods=['GET'])
def get_users():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return jsonify({"users": users})

# 3. ADD USER (Create)
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
    conn.commit()
    conn.close()
    return jsonify({"message": "User added successfully!"}), 201

if __name__ == '__main__':
    init_db()
    app.run(debug=True)