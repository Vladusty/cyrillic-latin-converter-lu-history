import tkinter as tk
from tkinter import messagebox

# Dictionary for transliteration based on your provided rules
CYRILLIC_TO_LATIN_DICT = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
    'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i',
    'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
    'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
    'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch',
    'ш': 'sh', 'щ': 'shch', 'ъ': '”', 'ы': 'y', 'ь': '’',
    'э': 'e', 'ю': 'iu', 'я': 'ia',
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D',
    'Е': 'E', 'Ё': 'E', 'Ж': 'ZH', 'З': 'Z', 'И': 'I',
    'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
    'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
    'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts', 'Ч': 'Ch',
    'Ш': 'Sh', 'Щ': 'SHCH', 'Ъ': '”', 'Ы': 'Y', 'Ь': '’',
    'Э': 'E', 'Ю': 'Iu', 'Я': 'Ia'
}


def cyrillic_to_latin(text):
    """Converts text from Cyrillic to Latin based on the specified rules."""
    return ''.join(CYRILLIC_TO_LATIN_DICT.get(char, char) for char in text)


def copy_to_clipboard():
    """Copies the text from the output text box to the clipboard."""
    text_to_copy = text_output.get("1.0", tk.END).strip()
    if text_to_copy:  # Prevent copying an empty string
        root.clipboard_clear()
        root.clipboard_append(text_to_copy)
        messagebox.showinfo("Done", "Text copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "Nothing to copy.")


def convert_text():
    """Function to perform text conversion, update the output field, and copy the result."""
    # Get all text from the input text box
    cyrillic_text = text_input.get("1.0", tk.END)
    latin_text = cyrillic_to_latin(cyrillic_text)

    # Clear and insert the new text into the output text box
    text_output.delete("1.0", tk.END)
    text_output.insert("1.0", latin_text)

    # Automatically copy the converted text to the clipboard
    root.clipboard_clear()
    root.clipboard_append(latin_text.strip())
    #messagebox.showinfo("Transliteration Complete", "The text has been transliterated and automatically copied to your clipboard.")


# Create the main application window
root = tk.Tk()
root.title("Cyrillic-to-Latin Transliteration")
root.geometry("600x600")

# Create and place widgets
label_input = tk.Label(root, text="Enter Cyrillic text:", font=("Helvetica", 12))
label_input.pack(pady=(10, 5))

# Use Text widget for multi-line input
text_input = tk.Text(root, width=60, height=10, font=("Helvetica", 12))
text_input.pack(pady=5)

convert_button = tk.Button(root, text="Transliterate", command=convert_text, font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white")
convert_button.pack(pady=10)

label_output = tk.Label(root, text="Result (Latin):", font=("Helvetica", 12))
label_output.pack(pady=(10, 5))

# Use Text widget for multi-line output
text_output = tk.Text(root, width=60, height=10, font=("Helvetica", 12))
text_output.pack(pady=5)

copy_button = tk.Button(root, text="Copy", command=copy_to_clipboard, font=("Helvetica", 10))
copy_button.pack(pady=10)

# Run the main application loop
root.mainloop()
