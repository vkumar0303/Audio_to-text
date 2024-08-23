#!/usr/bin/env python
# coding: utf-8

# # **Importing Libraries**

# In[4]:


import speech_recognition as sr
import tkinter as tk
from tkinter import filedialog, messagebox


# # **Convert Audio To Text**

# In[5]:


def convert_audio_to_text_pocketsphinx(audio_path):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_sphinx(audio)
            return text
    except sr.UnknownValueError:
        messagebox.showerror("Error", "Pocketsphinx could not understand the audio.")
        return None
    except sr.RequestError as e:
        messagebox.showerror("Error", f"Could not request results from Pocketsphinx service; {e}")
        return None


# # **Selecting Audio File**

# In[6]:


def select_audio_file():
    audio_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.wav *.flac *.aiff")])
    if audio_path:
        audio_entry.delete(0, tk.END)
        audio_entry.insert(0, audio_path)


# # **Convert**

# In[7]:


def convert():
    audio_path = audio_entry.get()
    if audio_path:
        text = convert_audio_to_text_pocketsphinx(audio_path)
        if text:
            text_output.delete(1.0, tk.END)
            text_output.insert(tk.END, text)
    else:
        messagebox.showwarning("Warning", "Please select an audio file.")


# # **Main Tkinter Window**

# In[8]:


# Create the main window
root = tk.Tk()
root.title("Audio to Text Converter")

# Audio file selection
tk.Label(root, text="Audio File:").grid(row=0, column=0, padx=10, pady=10)
audio_entry = tk.Entry(root, width=50)
audio_entry.grid(row=0, column=1, padx=10, pady=10)
audio_button = tk.Button(root, text="Browse", command=select_audio_file)
audio_button.grid(row=0, column=2, padx=10, pady=10)

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.grid(row=1, column=0, columnspan=3, pady=20)

# Text output area
tk.Label(root, text="Text Output:").grid(row=2, column=0, padx=10, pady=10)
text_output = tk.Text(root, wrap=tk.WORD, width=60, height=15)
text_output.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()


# In[ ]:




