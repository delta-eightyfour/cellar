# PYTHON WRITTEN BY DELTA84, PLZ GIVE CREDIT IF YOU USE THIS CODE ANYWHERE ELSE!!
import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont
import hashlib
import os

# 🔐 Hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# 📂 Load users from file
def load_users():
    users = {}
    if os.path.exists("users.txt"):
        with open("users.txt", "r") as f:
            for line in f:
                if ':' in line:
                    user, hashed = line.strip().split(":", 1)
                    users[user] = hashed
    return users

# 📝 Save new user
def save_user(username, password):
    with open("users.txt", "a") as f:
        f.write(f"{username}:{hash_password(password)}\n")

# 🖼️ Set window icon
def _set_window_icon(root):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    repo_name = os.path.basename(base_dir)
    home = os.path.expanduser('~')
    candidates = [
        base_dir,
        os.path.join(home, 'OneDrive', 'Desktop', repo_name),
        os.path.join(home, 'OneDrive - Personal', 'Desktop', repo_name),
        os.path.join(home, 'Desktop', repo_name),
    ]
    seen = set()
    candidate_dirs = []
    for p in candidates:
        try:
            np = os.path.normpath(p)
        except Exception:
            continue
        if np not in seen:
            seen.add(np)
            candidate_dirs.append(np)
    try:
        for d in candidate_dirs:
            png_path = os.path.join(d, 'cellar.png')
            if os.path.exists(png_path):
                try:
                    root.iconphoto(True, tk.PhotoImage(file=png_path))
                    return True
                except Exception:
                    return False
    except Exception:
        return False
    return False

# 🚪 Cancel
def on_cancel():
    root.destroy()

# 🔑 Submit
def on_submit():
    username = entry_username.get()
    password = entry_password.get()
    users = load_users()
    if username not in users or users[username] != hash_password(password):
        messagebox.showinfo("Login To Cellar", "Login Failed! Invalid Username or Password.")
    else:
        messagebox.showinfo(
            "Login To Cellar",
            f"Login Successful!\n\nUsername: {username}\nPassword: {'*' * len(password)}"
        )

# ❓ Forgot Password
def on_forgot_password():
    messagebox.showinfo("Forgot Password", "To reset your password, contact support")

# 🆕 Create Account
def on_create_account():
    win = tk.Toplevel(root)
    win.title("Create Account")
    win.resizable(False, False)
    frm = tk.Frame(win, padx=12, pady=12)
    frm.pack()

    tk_label = tk.Label
    tk_label(frm, text="New Username:").grid(row=0, column=0, sticky="e", pady=4)
    entry_new_user = tk.Entry(frm, width=25)
    entry_new_user.grid(row=0, column=1, pady=4)

    tk_label(frm, text="New Password:").grid(row=1, column=0, sticky="e", pady=4)
    entry_new_pass = tk.Entry(frm, show="*", width=25)
    entry_new_pass.grid(row=1, column=1, pady=4)

    def create():
        newu = entry_new_user.get()
        newp = entry_new_pass.get()
        users = load_users()
        if not newu or not newp:
            messagebox.showwarning("Create Account", "Please enter both username and password.")
            return
        if newu in users:
            messagebox.showwarning("Create Account", "Username already exists.")
            return
        save_user(newu, newp)
        messagebox.showinfo("Create Account", f"Account created for {newu}.")
        win.destroy()

    btn_create = tk.Button(frm, text="Create Account", width=20, command=create)
    btn_create.grid(row=2, column=0, columnspan=2, pady=(10, 0))

# 👁️ Toggle password visibility
password_visible = False

def toggle_password():
    global password_visible
    if password_visible:
        entry_password.config(show="*")
        btn_toggle.config(text="Show")
        password_visible = False
    else:
        entry_password.config(show="")
        btn_toggle.config(text="Hide")
        password_visible = True

# 🖼️ Build GUI
def build_gui():
    global root
    root = tk.Tk()
    root.title("Cellar v0.21 - Login")
    root.resizable(False, False)
    root.tk.call('tk', 'scaling', 1.25)
    default_font = tkfont.nametofont("TkDefaultFont")
    default_font.configure(size=11)
    root.geometry("500x300")
    root.protocol("WM_DELETE_WINDOW", on_cancel)
    _set_window_icon(root)
    root.bind('<Escape>', lambda e: on_cancel())
    root.bind('<Return>', lambda e: on_submit())

    main_frame = tk.Frame(root, padx=16, pady=16)
    main_frame.pack(fill=tk.BOTH, expand=True)

    georgia_title = tkfont.Font(family="Georgia", size=24, weight="bold")
    georgia_tagline = tkfont.Font(family="Georgia", size=10)
    georgia_version = tkfont.Font(family="Georgia", size=10)

    tk.Label(main_frame, text="Cellar", font=georgia_title).pack(pady=(0, 0))
    tk.Label(main_frame, text="V0.21", font=georgia_tagline).pack(pady=(0, 25))

    frame = tk.Frame(main_frame)
    frame.pack()

    tk_label = tk.Label

    # Username
    tk_label(frame, text="Username:").grid(row=0, column=0, sticky="e", pady=4)
    global entry_username
    entry_username = tk.Entry(frame, width=36)
    entry_username.grid(row=0, column=1, pady=4)

    # Password
    tk_label(frame, text="Password:").grid(row=1, column=0, sticky="e", pady=4)
    global entry_password
    entry_password = tk.Entry(frame, show="*", width=30)
    entry_password.grid(row=1, column=1, pady=4, sticky="w")

    global btn_toggle
    btn_toggle = tk.Button(frame, text="Show", width=5, command=toggle_password)
    btn_toggle.grid(row=1, column=2, padx=(5, 0))

    # Submit and Cancel
    tk.Button(frame, text="Submit", width=14, command=on_submit).grid(row=2, column=0, pady=(12, 0))
    tk.Button(frame, text="Cancel", width=14, command=on_cancel).grid(row=2, column=1, pady=(12, 0))

    # Links
    tk.Button(frame, text="Forgot Password", relief='flat', fg='blue', cursor='hand2', command=on_forgot_password).grid(row=3, column=0, columnspan=2, pady=(8, 0))
    tk.Button(frame, text="Create New Account", relief='flat', fg='blue', cursor='hand2', command=on_create_account).grid(row=4, column=0, columnspan=2, pady=(6, 0))

    tk.Label(root, text="V0.21", font=georgia_version, fg="gray").pack(side=tk.BOTTOM, pady=4)

    return root

# 🚀 Launch
if __name__ == '__main__':
    app = build_gui()
    
    
# see? i knew you'd read the code! just hope you dont steal it as your own though..
#           -delta84