# Cellar

WRITTEN BY THE ONE AND ONLY DELTA84 HIMSELF.  
DON’T SNATCH MY CODE WITHOUT CREDITING.
---


---
ACRONYM MEANINGS: "PGM" IS "PROGRAMMING LANGUAGE" IF YOU ARE WONDERING!
---

## License
Cellar is licensed under the GNU General Public License v3.0 (GPLv3).
See the LICENSE file for full details.

---

## Contributing
Pull requests are welcome!
If you’re planning something major, open an issue first so I don’t think the repo got nuked.
Make sure to update tests and docs. Future Delta84 appreciates it.

---

## What is Cellar?
Cellar is a (prototype) self-hosted cloud storage app written in Python + Tkinter.
(Yes, it will eventually be rewritten in Java or C++. If you contribute in those languages, put the code in THIS repository so things don’t get messy.)

Right now, Cellar includes:
- Login GUI
- Account creation
- Standalone Windows executable build

Future roadmap:
- File upload/download
- Replication across independent servers
- Entropy-based encryption (yes, we’re using lava lamps — Cloudflare did it first, we’re just cooler)
- Hardened Debian server deployment
- Rewriting Python into a Real Programming Language (C++ or another PGL)

---

## Feature Checklist
[x] Login GUI with account creation
[x] Windows build script with PyInstaller
[ ] Rewrite in C++ or another PGL
[ ] File upload/download
[ ] Multi-server replication
[ ] Entropy-based encryption
[ ] Debian hardened server deployment

---

## Current Requirements (THIS WILL CHANGE!!)
- Python
- tkinter
- pillow

---

## Install Guide
1. Run the PS1 file:
   build-windows.ps1
2. Say Y to the prompt
3. Wait
4. Done — your EXE is located at:
   C:\Users\user\directory\Cellar_V\dist\Cellar.exe

---

## What the build script does
- Upgrades pip
- Installs dependencies (Pillow, PyInstaller)
- Runs PyInstaller to package the app into a standalone Windows executable
- Embeds the icon (cellar.ico)
- Outputs to:
  dist\Cellar.exe

---

## Run in Dev Mode
To run the app without building an EXE:

python cellar_python_win64.py

---

## Post-Build Notes
- If you pinned an older EXE to the taskbar, unpin it first before pinning the new one
- Icon still blurry? Restart Windows Explorer or reboot
- Antivirus warnings are normal for unsigned EXEs — code signing helps avoid them

---

## PyInstaller Notes
Missing modules at runtime? Add them to:

hiddenimports=[...]

Need to include extra files? Add them under:

datas=[...]

Force a clean rebuild:

python -m PyInstaller --clean Cellar.spec



