from fastapi import FastAPI
from backend.database import cursor, conn
from backend.recognition import recognize_face

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Face Recognition Attendance System"}

@app.get("/attendance")
def get_attendance():
    cursor.execute("SELECT id, name, timestamp, status FROM attendance")
    rows = cursor.fetchall()
    data = [
        {"id": r[0], "name": r[1], "timestamp": str(r[2]), "status": r[3]}
        for r in rows
    ]
    return {"attendance": data}

@app.post("/recognize")
def recognize():
    success = recognize_face()
    return {"status": "Recognition finished", "recognized": success}
