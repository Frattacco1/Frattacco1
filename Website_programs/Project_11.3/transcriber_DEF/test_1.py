import time
import threading
from tkinter.ttk import Progressbar
import tkinter as tk

def converter_1():
    # Your conversion code here
    time.sleep(5)

def update_progress_bar():
    while converter_1_thread.is_alive():
        progress_bar.step(5)
        root.update_idletasks()
        time.sleep(0.2)

root = tk.Tk()
root.title("Program Progress")
progress_bar = Progressbar(root, length=500, mode="indeterminate")
progress_bar.pack()

converter_1_thread = threading.Thread(target=converter_1)
progress_thread = threading.Thread(target=update_progress_bar)

progress_thread.start()  # Start the progress bar update thread
converter_1_thread.start()  # Start the converter thread

root.mainloop()  # Keep the GUI event loop running
