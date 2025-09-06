import sys
import requests
from PyQt5 import QtWidgets, QtCore


API_BASE = "http://127.0.0.1:8000"


class AttendanceGUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Face Recognition Attendance")
        self.resize(600, 400)

        # --- Widgets ---
        self.start_btn = QtWidgets.QPushButton("Start Recognition")
        self.refresh_btn = QtWidgets.QPushButton("Refresh Attendance")
        self.status_label = QtWidgets.QLabel("Status: Ready")

        # Table
        self.table = QtWidgets.QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Timestamp", "Status"])
        self.table.horizontalHeader().setStretchLastSection(True)

        # Layout
        btn_layout = QtWidgets.QHBoxLayout()
        btn_layout.addWidget(self.start_btn)
        btn_layout.addWidget(self.refresh_btn)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addLayout(btn_layout)
        layout.addWidget(self.table)
        layout.addWidget(self.status_label)

        # --- Signals ---
        self.start_btn.clicked.connect(self.start_recognition)
        self.refresh_btn.clicked.connect(self.load_attendance)

        # Auto-refresh every 30s
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.load_attendance)
        self.timer.start(30000)

        # Load initial
        self.load_attendance()

    def load_attendance(self):
        try:
            resp = requests.get(f"{API_BASE}/attendance", timeout=10)
            data = resp.json().get("attendance", [])
            self.table.setRowCount(len(data))

            for row_idx, row in enumerate(data):
                self.table.setItem(row_idx, 0, QtWidgets.QTableWidgetItem(str(row.get("id", ""))))
                self.table.setItem(row_idx, 1, QtWidgets.QTableWidgetItem(str(row.get("name", ""))))
                self.table.setItem(row_idx, 2, QtWidgets.QTableWidgetItem(str(row.get("timestamp", ""))))
                self.table.setItem(row_idx, 3, QtWidgets.QTableWidgetItem(str(row.get("status", ""))))

            self.status_label.setText(f"Status: Loaded {len(data)} records.")
        except Exception as e:
            self.status_label.setText(f"Error loading attendance: {e}")


    def start_recognition(self):
        try:
            self.status_label.setText("Status: Starting recognition...")
            resp = requests.post(f"{API_BASE}/recognize", timeout=120)  # POST, not GET
            if resp.status_code == 200:
                self.status_label.setText("Status: Recognition completed.")
                self.load_attendance()
            else:
                self.status_label.setText(f"Error: {resp.text}")
        except Exception as e:
            self.status_label.setText(f"Recognition failed: {e}")



def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = AttendanceGUI()
    gui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
