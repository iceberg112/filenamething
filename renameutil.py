import os
import tkinter as tk
from tkinter import messagebox

def remove_text_from_filenames():
    # ctext
    text_to_remove = entry.get()
    
    if not text_to_remove:
        messagebox.showwarning("Input Error", "Please enter the text to remove.")
        return
    
    # direcotery
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # checikng
    for filename in os.listdir(current_dir):
        # checking more
        if text_to_remove in filename:
            # filenam
            new_filename = filename.replace(text_to_remove, "")
            
            # get payhs
            old_file_path = os.path.join(current_dir, filename)
            new_file_path = os.path.join(current_dir, new_filename)
            
            # rename
            os.rename(old_file_path, new_file_path)
    
    messagebox.showinfo("Success", "Text has been removed from filenames!")

# window
root = tk.Tk()
root.title("Remove Text from Filenames")

label = tk.Label(root, text="Enter text to remove from filenames:")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

button = tk.Button(root, text="Remove Text", command=remove_text_from_filenames)
button.pack(pady=20)

# start gui
root.mainloop()
