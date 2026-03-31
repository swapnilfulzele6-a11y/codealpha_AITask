# Task 1: Language Translation Tool
# Requirements: pip install googletrans==4.0.0-rc1

import tkinter as tk
from googletrans import Translator

def translate_text():
    src_lang = source_lang.get()
    tgt_lang = target_lang.get()
    text = input_text.get("1.0", tk.END).strip()
    
    if text:
        translator = Translator()
        translated = translator.translate(text, src=src_lang, dest=tgt_lang)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated.text)

# UI Setup
root = tk.Tk()
root.title("Language Translation Tool")

# Input Text
tk.Label(root, text="Enter text:").pack()
input_text = tk.Text(root, height=5, width=50)
input_text.pack()

# Source & Target Language
tk.Label(root, text="Source Language (e.g., en, fr, hi):").pack()
source_lang = tk.Entry(root)
source_lang.insert(0, "en")  # default English
source_lang.pack()

tk.Label(root, text="Target Language (e.g., en, fr, hi):").pack()
target_lang = tk.Entry(root)
target_lang.insert(0, "fr")  # default French
target_lang.pack()

# Translate Button
translate_btn = tk.Button(root, text="Translate", command=translate_text)
translate_btn.pack()

# Output Text
tk.Label(root, text="Translated text:").pack()
output_text = tk.Text(root, height=5, width=50)
output_text.pack()

root.mainloop()