
import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator
import pyttsx3
import pyperclip

# Initialize translator and TTS engine
translator = Translator()
engine = pyttsx3.init()

def translate_text():
    try:
        text = input_text.get("1.0", tk.END).strip()
        src_lang = src_lang_var.get()
        dest_lang = dest_lang_var.get()

        if not text:
            messagebox.showwarning("Warning", "Please enter some text to translate.")
            return

        result = translator.translate(text, src=src_lang, dest=dest_lang)
        translated_text.delete("1.0", tk.END)
        translated_text.insert(tk.END, result.text)

    except Exception as e:
        messagebox.showerror("Error", f"Translation failed: {e}")

def copy_text():
    text = translated_text.get("1.0", tk.END).strip()
    if text:
        pyperclip.copy(text)
        messagebox.showinfo("Copied", "Translated text copied to clipboard!")

def speak_text():
    text = translated_text.get("1.0", tk.END).strip()
    if text:
        engine.say(text)
        engine.runAndWait()

root = tk.Tk()
root.title("Language Translation Tool")
root.geometry("600x400")

tk.Label(root, text="Enter text:").pack()
input_text = tk.Text(root, height=5)
input_text.pack(fill=tk.X, padx=10)

lang_frame = tk.Frame(root)
lang_frame.pack(pady=5)

src_lang_var = tk.StringVar(value="en")
dest_lang_var = tk.StringVar(value="fr")

tk.Label(lang_frame, text="From").pack(side=tk.LEFT, padx=(0, 5))
src_lang_menu = ttk.Combobox(lang_frame, textvariable=src_lang_var, values=["en", "fr", "es", "de", "ta", "te", "hi"])
src_lang_menu.pack(side=tk.LEFT)

tk.Label(lang_frame, text="To").pack(side=tk.LEFT, padx=(10, 5))
dest_lang_menu = ttk.Combobox(lang_frame, textvariable=dest_lang_var, values=["en", "fr", "es", "de", "ta", "te", "hi"])
dest_lang_menu.pack(side=tk.LEFT)

translate_button = tk.Button(root, text="Translate", bg="green", fg="white", command=translate_text)
translate_button.pack(pady=10)

tk.Label(root, text="Translated text:").pack()
translated_text = tk.Text(root, height=5)
translated_text.pack(fill=tk.X, padx=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

copy_button = tk.Button(button_frame, text="Copy", bg="deepskyblue", fg="white", command=copy_text)
copy_button.pack(side=tk.LEFT, padx=10)

speak_button = tk.Button(button_frame, text="Speak", bg="tomato", fg="white", command=speak_text)
speak_button.pack(side=tk.LEFT, padx=10)

root.mainloop()
