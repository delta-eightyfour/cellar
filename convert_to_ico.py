"""Create a high-quality multi-resolution `cellar.ico` from `cellar.png`.

This produces an ICO containing multiple sizes (256,128,64,48,32,16) so
Windows can pick the best-sized image for titlebar, taskbar and shortcuts.
Transparency is preserved where present.
"""
import os
import sys
from PIL import Image

base_dir = os.path.dirname(os.path.abspath(__file__))
png_path = os.path.join(base_dir, 'cellar.png')
ico_path = os.path.join(base_dir, 'cellar.ico')

if not os.path.exists(png_path):
    print(f"Error: {png_path} not found")
    sys.exit(1)

try:
    src = Image.open(png_path)
    # Ensure we have an RGBA image so transparency is preserved
    if src.mode != 'RGBA':
        src = src.convert('RGBA')

    # Sizes to include in the ICO (PyInstaller works best with these standard sizes)
    sizes = [(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)]

    # Create a list of resized frames
    frames = []
    for s in sizes:
        img = src.copy()
        img = img.resize(s, Image.Resampling.LANCZOS)
        frames.append(img)

    # Save as ICO with all sizes
    # Save the first frame and use append=True for additional sizes (Pillow 10.0+)
    frames[0].save(ico_path, format='ICO', sizes=sizes)

    print(f"✓ Converted {png_path} → {ico_path}")
    print("  Sizes included:", ", ".join(f"{w}x{h}" for w, h in sizes))
    print("  Rebuild the .exe to embed this ICO for sharp taskbar/titlebar icons.")
    print(f"  File size: {os.path.getsize(ico_path)} bytes")
    sys.exit(0)
except Exception as e:
    print("Error creating ICO:", e)
    import traceback
    traceback.print_exc()
    sys.exit(1)
