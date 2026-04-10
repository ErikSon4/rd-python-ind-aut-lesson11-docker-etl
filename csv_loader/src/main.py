from pathlib import Path

import time
import pandas as pd
import mysql.connector

def connect_with_retry():
    while True:
        try:
            print("Connecting to database...")
            connection = mysql.connector.connect(
                host="db",
                port=3306,
                user="root",
                password="root",
                database="mydb"
            )
            print("Database connection established.")
            return connection
        except Exception as e:
            print(f"DB not ready yet: {e}")
            time.sleep(2)


def main():
    print("Loading CSV...")

    project_root = Path(__file__).parent.parent
    csv_path = project_root / "data.csv"

    df = pd.read_csv(csv_path)

    print("Data loaded:")
    print(df)

    connection = connect_with_retry()
    cursor = connection.cursor()

    for _, row in df.iterrows():
        cursor.execute(
            "INSERT INTO data (id, name, value) VALUES (%s, %s, %s)",
            (int(row["id"]), row["name"], int(row["value"]))
        )

    connection.commit()
    print("Data inserted into the database.")

    cursor.close()
    connection.close()
    print("Database connection closed.")

if __name__ == "__main__":
    main()