@echo off
setlocal

chcp 65001 >nul

REM:: Vérifier si pip est déjà installé
python-3.7.9\python.exe -m pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [*] pip non détecté. Installation en cours...

    python-3.7.9\python.exe get-pip.py
) else (
    echo [*] pip déja installer.
)

REM:: Vérifier si PyBluez est déjà installé
python-3.7.9\python.exe -c "import bluetooth" >nul 2>&1
if %errorlevel% neq 0 (
    echo [*] PyBluez non installé. Installation via la wheel...

    python-3.7.9\python.exe -m pip install PyBluez-0.23-cp37-cp37m-win_amd64.whl
) else (
    echo [*] PyBluez déja installer.
)

@REM echo [*] Lancement du scan Bluetooth...
python-3.7.9\python.exe scan_bt.py

pause