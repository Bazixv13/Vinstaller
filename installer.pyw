import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
import time
import os
import shutil
import sys

a = True
j = False

def bar1_progress(ui=""):
    if ui == "click once again to install" or ui == "click once again to uninstall":
        percent_label1.config(text=f"{ui}")
        progress_bar1['value'] = 0
        root.update_idletasks()
    else:
        percent_label1.config(text=f"{ui} 0%")
        root.update_idletasks()
        os.chdir("C:/Program Files")
        try:
            os.mkdir("Velocitify")
        except PermissionError:
            messagebox.showerror("ERROR", "This file must be opened as admin")
            root.destroy()
        except FileExistsError:
            pass
        except:
            messagebox.showerror(""
                                 ""
                                 "ERROR", "Unknown error")
            root.destroy()
        for i in range(50):
            progress_bar1['value'] = i
            percent_label1.config(text=f"{ui} {i}%")
            root.update_idletasks()
            time.sleep(0.001)
        # installation script here:
        os.chdir("Velocitify")
        os.system('curl https://github.com/Bazixv13/all-in-one/releases/download/0.0.2/all-in-one-final.zip --ssl-no-revoke -L -O --silent')
        os.system('tar -xf "all-in-one-final.zip"')
        os.remove("all-in-one-final.zip")

        for i in range(51):
            progress_bar1['value'] = 50 + i
            percent_label1.config(text=f"{ui} {50 + i}%")
            root.update_idletasks()
            time.sleep(0.0000001)
        messagebox.showinfo(" ", "Installation completed successfully.")
        root.destroy()



def bar2_progress(ui=""):
    if ui == "click once again to install" or ui == "click once again to uninstall":
        percent_label1.config(text=f"{ui}")
        progress_bar1['value'] = 0
        root.update_idletasks()
    else:
        for i in range(50):
            progress_bar1['value'] = i
            percent_label1.config(text=f"{ui} {i}%")
            root.update_idletasks()
            time.sleep(0.00001)
        # uninstallation script here:
        try:
            shutil.rmtree("C:/Program Files/Velocitify")
        except FileNotFoundError:
            messagebox.showerror(" ", "Unable to locate program files")
            root.destroy()

        for i in range(51):
            progress_bar1['value'] = 50 + i
            percent_label1.config(text=f"{ui} {50 + i}%")
            root.update_idletasks()
            time.sleep(0.00000000000000001)
        messagebox.showinfo(" ", "Uninstallation completed successfully.")
        root.destroy()


def install():
    global a
    # Add your installation code here
    if a:
        loading_frame.grid(row=0, column=1, padx=10, pady=10)
        bar1_progress(ui="click once again to install")
        a = False
    else:
        if add_shortcut_var.get():
            # Add your code to create a shortcut on the desktop here
            pass
        bar1_progress(ui="installing")
        loading_frame.grid(row=0, column=1, padx=10, pady=10)


def uninstall():
    global a
    # Add your installation code here
    if add_shortcut_var.get():
        # Add your code to create a shortcut on the desktop here
        pass
    if a:
        loading_frame.grid(row=0, column=1, padx=10, pady=10)
        bar2_progress(ui="click once again to uninstall")
        a = False
    else:
        bar2_progress(ui="uninstalling")
        loading_frame.grid(row=0, column=1, padx=10, pady=10)


def cancel():
    result = messagebox.askyesno("Warning", "This will close installer. Do you wish to continue?")
    if result == True:
        root.destroy()
    else:
        pass


current_dir = os.path.dirname(os.path.realpath(sys.argv[0]))

# Determine the path to the executable (needed for PyInstaller)
if hasattr(sys, '_MEIPASS'):
    # Running as PyInstaller executable
    base_dir = sys._MEIPASS
else:
    # Running as normal Python script
    base_dir = os.path.abspath(os.path.dirname(__file__))

root = tk.Tk()
root.title("Installer/Uninstaller")
root.protocol("WM_DELETE_WINDOW", cancel)
root.resizable(False, False)
root.iconbitmap(os.path.join(base_dir, "TEMPsayudbh432.ico"))
root.wm_iconbitmap(os.path.join(base_dir, "TEMPsayudbh432.ico"))

frame = ttk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=10)

add_shortcut_var = tk.IntVar()
add_shortcut_checkbox = ttk.Checkbutton(frame, text="Add Shortcut", variable=add_shortcut_var, cursor="hand2")
add_shortcut_checkbox.grid(row=0, column=0, sticky="w", padx=20, pady=5)

install_button = ttk.Button(frame, text="Install", command=install)
install_button.grid(row=1, column=0, pady=5)

uninstall_button = ttk.Button(frame, text="Uninstall", command=uninstall)
uninstall_button.grid(row=2, column=0)

loading_frame = ttk.Frame(root)
loading_frame.grid(row=0, column=1, padx=10, pady=10)
loading_frame.grid_remove()

loading_label = ttk.Label(loading_frame, text="Progressbars:", font=("Helvetica", 12))
loading_label.grid(row=0, column=0, sticky="w", padx=20, pady=5)

progress_bar1 = ttk.Progressbar(loading_frame, orient="horizontal", length=200, mode="determinate")
progress_bar1.grid(row=1, column=0, padx=20, pady=5)
percent_label1 = ttk.Label(loading_frame, text="0%")
percent_label1.grid(row=1, column=1, padx=10)

root.update_idletasks()
root.geometry(
    f"+{(root.winfo_screenwidth() - root.winfo_width()) // 2}+{(root.winfo_screenheight() - root.winfo_height()) // 2}")


root.mainloop()
