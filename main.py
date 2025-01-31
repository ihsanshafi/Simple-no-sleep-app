import pyautogui
import time
import random
import tkinter as tk
from tkinter import messagebox

running = False
start_time = 0

def start_loop():
    global running, start_time
    try:
        duration = int(duration_entry.get())
        if duration <= 0:
            messagebox.showerror("Error", "Duration must be greater than 0.")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")
        return

    running = True
    start_time = time.time()
    move_mouse(duration)

def move_mouse(duration):
    if not running:
        return

    count_down = time.time() - start_time

    # Move the mouse to a random position
    pyautogui.moveTo(random.randint(0, 1080), random.randint(0, 1080))

    if count_down < duration:
        # Schedule the next move
        root.after(int(delay_slider.get() * 1000), move_mouse, duration)
    else:
        messagebox.showinfo("Done", "Time is up!")
        stop_loop()

def stop_loop():
    global running
    running = False


root = tk.Tk()
root.title("No sleep app")

#duration input
duration_label = tk.Label(root, text="Duration (seconds):")
duration_label.pack(pady=5)
duration_entry = tk.Entry(root)
duration_entry.pack(pady=5)

#delay slider
delay_label = tk.Label(root, text="Delay between moves (seconds):")
delay_label.pack(pady=5)
delay_slider = tk.Scale(root, from_=0.1, to=10, resolution=0.1, orient=tk.HORIZONTAL)
delay_slider.set(5)  # Default delay
delay_slider.pack(pady=5)


start_button = tk.Button(root, text="Start", command=start_loop)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop", command=stop_loop)
stop_button.pack(pady=10)

root.mainloop()