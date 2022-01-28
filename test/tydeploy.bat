@echo off
call ..\venv\Scripts\activate.bat
set PYTHONPATH=..
python -m tydeploy %*
