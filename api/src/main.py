from flask import Flask, jsonify
import mysql.connector
import time

app = Flask(__name__)


def connect_with_retry():
    while True:
        try:
            connection = mysql.connector.connect(
                host="db",
                port=3306,
                user="root",
                password="root",
                database="mydb"
            )
            return connection
        except Exception as e:
            print(f"DB not ready yet: {e}")
            time.sleep(2)


@app.route("/data", methods=["GET"])
def get_data():
    conn = connect_with_retry()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM data")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(rows)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)