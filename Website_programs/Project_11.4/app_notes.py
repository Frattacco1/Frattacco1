import tkinter as tk
from tkinter import font
from tkinter import filedialog

def app():

    def save_notes():
        notes = text.get("1.0", "end-1c")  # Ottieni il testo dalle note
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    
        if file_path:
            with open(file_path, "w") as file:
                file.write(notes)
            save_status.config(text=f"Note saved to {file_path}")



    app = tk.Tk()
    app.title("Appunti Rapidi")

    save_status = tk.Label(app, text="Note")
    save_status.pack()

    # Bottone per salvare le note
    save_button = tk.Button(app, text="Salva", command=save_notes)
    save_button.pack()

    # text stuff
    text = tk.Text(app)
    text.pack()
    custom_font = font.nametofont("TkDefaultFont")
    custom_font.configure(family="Times New Roman", size=16)
    text.config(font=custom_font)


    # Carica le note precedenti se esistono
    try:
        with open("notes.txt", "r") as file:
            notes = file.read()
            text.insert("1.0", notes)
    except FileNotFoundError:
        pass

    app.mainloop()


app()
