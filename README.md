WELCOME TO THE CELLAR GIT-REPO!
"Infinite Storage, Infinite Possibilites."

DEPENDENCIES AND GUIDE LISTED BELLOW

WHAT YA NEED:
- Python (obviously)
- tk
- pillow

-----------------------------------------

Install Guide!
1. Run The PS1 file! (`build-windows.ps1`)
2. Say Y To The Prompt!
3. Wait
4. And ur done. exe file is in `C:\Users\user\directory\Cellar_V\dist\Cellar.exe`!

-----------------------------------------

What the build does:
- Upgrades pip
- Installs dependencies (Pillow, PyInstaller)
- Runs PyInstaller to package your app into a standalone Windows executable
- Embeds the icon (`cellar.ico`) so it shows sharp in taskbar and start menu
- Output: `dist\Cellar.exe`

-----------------------------------------

To run the app WITHOUT building an EXE (dev mode):
```powershell
python cellar_python_win64.py
```

-----------------------------------------

Post-Build Notes:
- If you pinned the old EXE to taskbar, unpin it first, then pin the new one (Windows caches icons)
- Icon still blurry? Restart Windows Explorer or reboot your system.
- If antivirus flags it: it's normal for unsigned EXEs; consider code signing to avoid warnings

-----------------------------------------

Troubleshooting:
- Missing modules at runtime? Edit `Cellar.spec` and add them to `hiddenimports=[...]`
- Need to include extra files? Add them to `datas` in `Cellar.spec`
- Force clean rebuild:
  ```powershell
  python -m PyInstaller --clean Cellar.spec
  ```

-----------------------------------------

Credit & License:
This code was written by Delta84. Please give credit if you reuse it!


