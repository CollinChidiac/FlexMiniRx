import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
import webbrowser

# Constants
PYTHON_DOWNLOAD_URL = "https://www.python.org/downloads/"
FIRMWARE_DOWNLOAD_URL = "https://ui.com/download/software/usw-flex-mini"
WEBSERVER_DIR = r"C:\webserver"
FIRMWARE_NAME = "fwupdate.bin"

# GUI
def main():
    root = tk.Tk()
    root.title("USW-Flex-Mini Firmware Server Setup")
    root.geometry("520x370")
    root.configure(bg="#2b2b2b")

    def open_python_url():
        webbrowser.open(PYTHON_DOWNLOAD_URL)

    def open_firmware_url():
        webbrowser.open(FIRMWARE_DOWNLOAD_URL)

    def verify_python():
        try:
            output = subprocess.check_output(["python", "-V"], stderr=subprocess.STDOUT).decode().strip()
            messagebox.showinfo("Python Found", f"{output} is installed.")
            return True
        except Exception as e:
            messagebox.showerror("Python Not Found", "Python is not installed or not added to PATH.")
            return False

    def create_webserver_dir():
        try:
            os.makedirs(WEBSERVER_DIR, exist_ok=True)
            messagebox.showinfo("Directory Created", f"Directory created at: {WEBSERVER_DIR}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create directory: {e}")

    def select_firmware_file():
        file_path = filedialog.askopenfilename(title="Select Firmware File")
        if file_path:
            try:
                dest_path = os.path.join(WEBSERVER_DIR, FIRMWARE_NAME)
                shutil.copy(file_path, dest_path)
                messagebox.showinfo("Success", f"Firmware copied and renamed to {dest_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to move firmware: {e}")

    def start_webserver():
        confirm = messagebox.askyesno("Start Web Server", "Start the Python HTTP server on port 80?")
        if confirm:
            try:
                os.chdir(WEBSERVER_DIR)
                subprocess.Popen(["python", "-m", "http.server", "80"], creationflags=subprocess.CREATE_NEW_CONSOLE)
                messagebox.showinfo("Web Server Running", "Python HTTP server is now running on port 80.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to start server: {e}")

    # UI Layout
    header_frame = tk.Frame(root, bg="#2b2b2b")
    header_frame.pack(pady=10)

    header_label1 = tk.Label(
        header_frame,
        text="IMPORTANT:",
        fg="red",
        bg="#2b2b2b",
        font=("Segoe UI", 10, "bold")
    )
    header_label1.pack(anchor="w")

    header_label2 = tk.Label(
        header_frame,
        text="This tool only works with Python 3.x. Select 'Add Python to PATH' during install.\n"
             "Make sure to change your computer IP to a static 192.168.1.99!!!",
        fg="white",
        bg="#2b2b2b",
        font=("Segoe UI", 10),
        justify="left",
        wraplength=460
    )
    header_label2.pack(anchor="w")

    tk.Button(root, text="1. Download Python", command=open_python_url, width=40).pack(pady=5)
    tk.Button(root, text="2. Verify Python Installation", command=verify_python, width=40).pack(pady=5)
    tk.Button(root, text="3. Create Webserver Directory", command=create_webserver_dir, width=40).pack(pady=5)
    tk.Button(root, text="4. Download Firmware", command=open_firmware_url, width=40).pack(pady=5)
    tk.Button(root, text="5. Select and Move Firmware File", command=select_firmware_file, width=40).pack(pady=5)
    tk.Button(root, text="6. Start Web Server", command=start_webserver, width=40).pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
