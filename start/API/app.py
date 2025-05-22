from flask import Flask, request, jsonify, render_template
import psycopg2
from datetime import datetime

app = Flask(__name__)

# PostgreSQL connection setup
def get_db_connection():
    return psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="bcmch",
        host="localhost",
        port=5432
    )

@app.route('/',methods=['GET'])
def home_page():
      return render_template("welcome.html")

@app.route('/patients', methods=['POST'])
def add_patient():
    data = request.get_json()

    name = data.get("name")
    age = data.get("age")
    gender = data.get("gender")
    
    if not name:
        return jsonify({"error": "Name is required"}), 400

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO patient (name, age, gender, created_at) VALUES (%s, %s, %s, %s) RETURNING id;",
        (name, age, gender, datetime.now())
    )
    patient_id = cur.fetchone()[0]
    conn.commit()

    cur.close()
    conn.close()

    return jsonify({"id": patient_id, "message": "Patient added"}), 201

if __name__ == '__main__':
    app.run(debug=False, port=5000)
