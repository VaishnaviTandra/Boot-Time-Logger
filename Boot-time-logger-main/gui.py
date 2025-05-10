# # gui.py
# import tkinter as tk
# from tkinter import messagebox
# import os
# import app

# def view_text_log():
#     try:
#         os.startfile("boot_logs.txt")
#     except FileNotFoundError:
#         messagebox.showerror("Error", "Text log not found!")

# def view_excel_log():
#     try:
#         os.startfile("boot_logs.xlsx")
#     except FileNotFoundError:
#         messagebox.showerror("Error", "Excel log not found!")

# def trigger_logger():
#     try:
#         app.boot_time()
#         messagebox.showinfo("Success", "Boot time logged and WhatsApp sent!")
#     except PermissionError as e:
#         messagebox.showerror("File Locked", str(e))
#     except Exception as e:
#         messagebox.showerror("Error", f"An unexpected error occurred:\n{e}")

# window = tk.Tk()
# window.title("Boot Time Logger")
# window.geometry("320x200")
# window.resizable(False, False)

# tk.Label(window, text="Boot Logger Dashboard", font=("Helvetica", 14)).pack(pady=10)
# tk.Button(window, text="📄 View Text Log", command=view_text_log,  width=25).pack(pady=5)
# tk.Button(window, text="📊 View Excel Log", command=view_excel_log, width=25).pack(pady=5)
# tk.Button(window, text="⚡ Log & Send WhatsApp", command=trigger_logger,
#           width=25, bg="green", fg="white").pack(pady=10)

# window.mainloop()



# import tkinter as tk
# from tkinter import messagebox
# import os
# import app  # Import the app.py file


# def view_text_log():
#     try:
#         os.startfile("boot_logs.txt")  # Opens in Notepad
#     except FileNotFoundError:
#         messagebox.showerror("Error", "Text log not found!")


# def view_excel_log():
#     try:
#         os.startfile("boot_logs.xlsx")  # Opens in Excel if installed
#     except FileNotFoundError:
#         messagebox.showerror("Error", "Excel log not found!")


# def trigger_logger():
#     try:
#         app.boot_time()  # Calls boot_time() function from app.py
#         messagebox.showinfo("Success", "Boot time logged and WhatsApp sent!")
#     except PermissionError as e:
#         messagebox.showerror("File Locked", str(e))
#     except Exception as e:
#         messagebox.showerror("Error", f"Something went wrong: {e}")


# # ----------------------
# # UI Window
# # ----------------------
# window = tk.Tk()
# window.title("Boot Time Logger")

# # Full-screen window
# window.attributes("-fullscreen", True)

# # Background color
# window.configure(bg="#2E3B55")

# # Add a stylish label with a custom font
# tk.Label(window, text="Boot Logger Dashboard", font=("Helvetica", 24, "bold"), fg="white", bg="#2E3B55").pack(pady=30)

# # Add a stylish button with rounded corners, custom colors
# button_style = {"font": ("Helvetica", 14), "width": 25, "bd": 5, "relief": "solid", "fg": "white", "bg": "#4CAF50"}

# # Buttons for Text and Excel logs
# tk.Button(window, text="📄 View Text Log", command=view_text_log, **button_style).pack(pady=10)
# tk.Button(window, text="📊 View Excel Log", command=view_excel_log, **button_style).pack(pady=10)

# # Button to Log and Send WhatsApp with custom color
# log_button_style = button_style.copy()
# log_button_style.update({"bg": "#FF5733", "fg": "white"})  # Red color for action

# tk.Button(window, text="⚡ Log & Send WhatsApp", command=trigger_logger, **log_button_style).pack(pady=20)

# # Start the main event loop for the Tkinter window
# window.mainloop()


import tkinter as tk
from tkinter import messagebox
import os
import app  # Import the app.py file


# Button hover effects
def on_enter(button, color):
    button.config(bg=color)


def on_leave(button, color):
    button.config(bg=color)


def view_text_log():
    try:
        os.startfile("boot_logs.txt")  # Opens in Notepad
    except FileNotFoundError:
        messagebox.showerror("Error", "Text log not found!")


def view_excel_log():
    try:
        os.startfile("boot_logs.xlsx")  # Opens in Excel if installed
    except FileNotFoundError:
        messagebox.showerror("Error", "Excel log not found!")


def trigger_logger():
    try:
        app.boot_time()  # Calls boot_time() function from app.py
        messagebox.showinfo("Success", "Boot time logged and WhatsApp sent!")
    except PermissionError as e:
        messagebox.showerror("File Locked", str(e))
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")


# Exit Function
def wrong_button():
    messagebox.showinfo("You’ve been tricked!", "Just kidding! But you're exiting anyway.")
    window.quit()


# ----------------------
# UI Window
# ----------------------
window = tk.Tk()
window.title("Boot Time Logger")

# Full-screen window
window.attributes("-fullscreen", True)

# Gradient Background (2-color gradient)
window.configure(bg="#2E3B55")

# Add a stylish label with a custom font
tk.Label(window, text="Boot Logger Dashboard", font=("Helvetica", 28, "bold"), fg="white", bg="#2E3B55").pack(pady=50)

# Add a stylish button with rounded corners, custom colors
button_style = {"font": ("Helvetica", 16), "width": 30, "bd": 3, "relief": "flat", "fg": "white", "bg": "#4CAF50", "height": 2}

# Buttons for Text and Excel logs
text_log_button = tk.Button(window, text="📄 View Text Log", command=view_text_log, **button_style)
text_log_button.pack(pady=20)
text_log_button.bind("<Enter>", lambda e: on_enter(text_log_button, "#45a049"))
text_log_button.bind("<Leave>", lambda e: on_leave(text_log_button, "#4CAF50"))

excel_log_button = tk.Button(window, text="📊 View Excel Log", command=view_excel_log, **button_style)
excel_log_button.pack(pady=20)
excel_log_button.bind("<Enter>", lambda e: on_enter(excel_log_button, "#45a049"))
excel_log_button.bind("<Leave>", lambda e: on_leave(excel_log_button, "#4CAF50"))

# Button to Log and Send WhatsApp with custom color
log_button_style = button_style.copy()
log_button_style.update({"bg": "#FF5733", "fg": "white"})  # Red color for action

log_and_send_button = tk.Button(window, text="⚡ Log & Send WhatsApp", command=trigger_logger, **log_button_style)
log_and_send_button.pack(pady=40)
log_and_send_button.bind("<Enter>", lambda e: on_enter(log_and_send_button, "#e74c3c"))
log_and_send_button.bind("<Leave>", lambda e: on_leave(log_and_send_button, "#FF5733"))

# The "Wrong Button" that closes the app with a message
wrong_button_style = button_style.copy()
wrong_button_style.update({"bg": "#F44336", "fg": "white"})  # Bright red for danger

wrong_button = tk.Button(window, text="❌ Exit (Wrong Button)", command=wrong_button, **wrong_button_style)
wrong_button.pack(pady=10)
wrong_button.bind("<Enter>", lambda e: on_enter(wrong_button, "#e74c3c"))
wrong_button.bind("<Leave>", lambda e: on_leave(wrong_button, "#F44336"))

# Start the main event loop for the Tkinter window
window.mainloop()

