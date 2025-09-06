import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",         # 🔹 your MySQL username
    password="root", # 🔹 your MySQL password
    database="attendance_db"
)
cursor = conn.cursor()

def mark_attendance(name: str):
    """
    Insert attendance record for given name.
    Prevents multiple entries for the same person on the same day.
    """
    cursor.execute(
        "SELECT * FROM attendance WHERE name=%s AND DATE(timestamp)=CURDATE()",
        (name,)
    )
    if cursor.fetchone() is None:  # Only insert once per day
        cursor.execute(
            "INSERT INTO attendance (name, timestamp, status) VALUES (%s, NOW(), %s)",
            (name, "Present")
        )
        conn.commit()
        print(f"[DB] Attendance marked for {name}")
    else:
        print(f"[DB] {name} already marked today.")
