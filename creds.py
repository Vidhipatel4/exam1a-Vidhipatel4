from flask import Flask, request, jsonify
import mysql.connector
from creds import DB_CONFIG

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

@app.route('/api/museum/add', methods=['POST'])
def add_art_piece():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = """
        INSERT INTO museum (name, artist, year, description)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(sql, (data['name'], data['artist'], data['year'], data.get('description', '')))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Art piece added successfully"}), 201

@app.route('/api/museum/sell', methods=['PUT'])
def sell_art_piece():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = """
        UPDATE museum
        SET owner = %s, value = %s
        WHERE id = %s AND owner IS NULL
    """
    cursor.execute(sql, (data['owner'], data['value'], data['id']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Art piece sold successfully"})
@app.route('/api/museum/inventory', methods=['GET'])
def get_inventory():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM museum")
    items = cursor.fetchall()
    cursor.execute("SELECT SUM(value) AS totalvalue FROM museum WHERE value IS NOT NULL")
    total_value = cursor.fetchone()["totalvalue"]
    cursor.close()
    conn.close()
    return jsonify({"inventory": items, "totalvalue": total_value})
if __name__ == '__main__':
    app.run(debug=True)