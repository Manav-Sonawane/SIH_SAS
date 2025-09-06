@echo off
:: Activate virtual environment
call .venv\Scripts\activate

:: Start backend (FastAPI) in new terminal window
start cmd /k "uvicorn backend.main:app --reload"

:: Wait 3 seconds for backend to boot
timeout /t 3 > nul

:: Start PyQt GUI
python gui\attendance_gui.py
