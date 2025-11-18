# Build script for Windows .exe using PyInstaller
# Run from the Cellar_V0.21 folder: .\build-windows.ps1

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt pyinstaller

# Build the .exe (onefile = single executable, windowed = no console)
# Replace 'cellar.ico' with your icon file if available
$icon = if (Test-Path "cellar.ico") { "--icon=cellar.ico" } else { "" }

pyinstaller --noconfirm --onefile --windowed $icon --name "Cellar" cellar_python_win64.py

Write-Host ""
Write-Host "Build complete! The .exe is in the 'dist' folder:"
Write-Host "  dist\Cellar.exe"
Write-Host ""
Write-Host "Optional: Create an installer with Inno Setup (download from https://jrsoftware.org/isdl.php)"
Write-Host "  Edit build-installer.iss and run Inno Setup to package Cellar.exe"
