# Cellar

WRITTEN BY THE ONE AND ONLY DELTA84 HIMSELF, DONT SNATCH THE CODE WITHOUT CREDITING!
------------------------------------------
License
------------------------------------------
Cellar is licensed under the GNU General Public License v3.0 (GPLv3). See the LICENSE file for full details.
------------------------------------------
Contributing
------------------------------------------
Pull requests are welcome! Please open an issue first to discuss major changes. Make sure to update tests and docs as needed.
------------------------------------------

## What is Cellar?
Cellar is a (prototype) cloud storage app written in Python + Tkinter.  (soon will be made in java or C++. contribs with these languages must be in THIS repo!!)
It currently provides login/account creation and builds into a standalone Windows executable.  
Future roadmap includes file upload/download, replication across independent servers, and entropy‑based encryption (Yes, we're using lava lamps. We took it from CloudFlare because why not).
------------------------------------------
[x] Login GUI with account creation

[x] Windows build script with PyInstaller

[ ] Use C++ Or Another PGL Instead of Python

[ ] File upload/download to server

[ ] Replication across multiple independent servers

[ ] Entropy‑based encryption 

[ ] Hardened Debian server deployment

------------------------------------------

## Current Requirements (THIS WILL CHANGE!!)
- Python
- tk
- pillow

------------------------------------------

## Install Guide
1. Run the PS1 file! (`build-windows.ps1`)
2. Say Y To The Prompt!
3. Wait
4. And ur done. exe file is in  
   `C:\Users\user\directory\Cellar_V\dist\Cellar.exe`!

------------------------------------------

## What the build does
- Upgrades pip
- Installs dependencies (Pillow, PyInstaller)
- Runs PyInstaller to package your app into a standalone Windows executable
- Embeds the icon (`cellar.ico`) so it shows sharp in taskbar and start menu
- Output: `dist\Cellar.exe`

------------------------------------------

## Run in Dev Mode
To run the app WITHOUT building an EXE:
python cellar_python_win64.py
-------------------------------------------
Post-Build Notes
If you pinned the old EXE to taskbar, unpin it first, then pin the new one (Windows caches icons)

Icon still blurry? Restart WinExplorer or reboot your system.

If antivirus flags it: it's normal for unsigned EXEs; consider code signing to avoid warnings
-------------------------------------------
Missing modules at runtime? Edit Cellar.spec and add them to hiddenimports=[...]

Need to include extra files? Add them to datas in Cellar.spec

Force clean rebuild: python -m PyInstaller --clean Cellar.spec





