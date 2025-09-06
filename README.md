# Face Recognition Attendance System

## Pre-Setup Requirements

### 1. Database Setup (MySQL)

- Install MySQL Server (https://dev.mysql.com/downloads/installer/)
- Create a database named `attendance_db`.
- Create the attendance table:

  ```sql
  CREATE DATABASE attendance_db;
  USE attendance_db;

  CREATE TABLE attendance (
  		id INT AUTO_INCREMENT PRIMARY KEY,
  		name VARCHAR(100) NOT NULL,
  		timestamp DATETIME NOT NULL,
  		status VARCHAR(20) NOT NULL
  );
  ```

- (Optional) For student details:
  ```sql
  CREATE TABLE students (
  		id INT AUTO_INCREMENT PRIMARY KEY,
  		name VARCHAR(100) NOT NULL,
  		image_path VARCHAR(255)
  );
  ```
- Update your MySQL username and password in `backend/database.py` if needed.

### 2. Python Libraries

Install all required libraries (preferably in a virtual environment) with:

```
pip install -r requirements.txt
```

### 3. Folder Structure

- Ensure a `faces/` directory exists in the root.
- Place `.jpg` images of known people here. The filename (without extension) is used as the person's name.
  - Example: `faces/manav.jpg` will recognize as "manav".

## How to Run

1. **Start the FastAPI backend:**
   ```
   cd backend
   uvicorn main:app --reload
   ```
2. **Launch the GUI:** (in a new terminal)
   ```
   cd ../gui
   python attendance_gui.py
   ```
3. **Add face images:** Place `.jpg` images in the `faces/` folder before running recognition.

## Notes

- The backend must be running before starting the GUI.
- The webcam is required for face recognition.
- Attendance is marked only once per person per day.
- All attendance records are stored in the MySQL database.
