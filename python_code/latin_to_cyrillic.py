import tkinter as tk
from tkinter import messagebox

# Dictionary for transliteration based on your provided rules
# The dictionary is reversed for Latin-to-Cyrillic conversion.
LATIN_TO_CYRILLIC_DICT = {
    'a': 'а', 'b': 'б', 'v': 'в', 'g': 'г', 'd': 'д',
    'e': 'е', 'zh': 'ж', 'z': 'з', 'i': 'и', 'k': 'к',
    'l': 'л', 'm': 'м', 'n': 'н', 'o': 'о', 'p': 'п',
    'r': 'р', 's': 'с', 't': 'т', 'u': 'у', 'f': 'ф',
    'kh': 'х', 'ts': 'ц', 'ch': 'ч', 'sh': 'ш', 'shch': 'щ',
    '”': 'ъ', 'y': 'ы', '’': 'ь', 'iu': 'ю', 'ia': 'я',
    'A': 'А', 'B': 'Б', 'V': 'В', 'G': 'Г', 'D': 'Д',
    'E': 'Е', 'ZH': 'Ж', 'Z': 'З', 'I': 'И', 'K': 'К',
    'L': 'Л', 'M': 'М', 'N': 'Н', 'O': 'О', 'P': 'П',
    'R': 'Р', 'S': 'С', 'T': 'Т', 'U': 'У', 'F': 'Ф',
    'Kh': 'Х', 'Ts': 'Ц', 'Ch': 'Ч', 'Sh': 'Ш', 'SHCH': 'Щ',
    'Y': 'Ы', 'Iu': 'Ю', 'Ia': 'Я'
}

# The following rules are for multi-character sequences, handled separately
# to avoid incorrect substitutions. Order is important (longest first).
MULTI_CHAR_SEQUENCES = {
    'shch': 'щ', 'Shch': 'Щ', 'SHCH': 'Щ',
    'kh': 'х', 'Kh': 'Х',
    'ts': 'ц', 'Ts': 'Ц',
    'ch': 'ч', 'Ch': 'Ч',
    'sh': 'ш', 'Sh': 'Ш',
    'zh': 'ж', 'Zh': 'Ж',
    'iu': 'ю', 'Iu': 'Ю',
    'ia': 'я', 'Ia': 'Я'
}


def latin_to_cyrillic(text):
    """
    Converts text from Latin to Cyrillic based on the specified rules.
    Handles multi-character Latin sequences.
    """
    # Replace multi-character sequences first
    for latin_seq, cyrillic_char in MULTI_CHAR_SEQUENCES.items():
        text = text.replace(latin_seq, cyrillic_char)

    # Then replace single characters
    cyrillic_text = ''.join(LATIN_TO_CYRILLIC_DICT.get(char, char) for char in text)

    return cyrillic_text


def convert_text():
    """Function to perform text conversion and update the output field."""
    latin_text = text_input.get("1.0", tk.END)
    cyrillic_text = latin_to_cyrillic(latin_text)

    text_output.delete("1.0", tk.END)
    text_output.insert("1.0", cyrillic_text)

    # Show a confirmation message
    messagebox.showinfo("Transliteration Complete", "The text has been transliterated.")


def copy_to_clipboard():
    """Copies the text from the output text box to the clipboard."""
    text_to_copy = text_output.get("1.0", tk.END).strip()
    if text_to_copy:
        root.clipboard_clear()
        root.clipboard_append(text_to_copy)
        messagebox.showinfo("Done", "Text copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "Nothing to copy.")


# Create the main application window
root = tk.Tk()
root.title("Latin-to-Cyrillic Transliteration")
root.geometry("600x600")

# Create and place widgets
label_input = tk.Label(root, text="Enter Latin text:", font=("Helvetica", 12))
label_input.pack(pady=(10, 5))

text_input = tk.Text(root, width=60, height=10, font=("Helvetica", 12))
text_input.pack(pady=5)

convert_button = tk.Button(root, text="Transliterate", command=convert_text, font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white")
convert_button.pack(pady=10)

label_output = tk.Label(root, text="Result (Cyrillic):", font=("Helvetica", 12))
label_output.pack(pady=(10, 5))

text_output = tk.Text(root, width=60, height=10, font=("Helvetica", 12))
text_output.pack(pady=5)

copy_button = tk.Button(root, text="Copy", command=copy_to_clipboard, font=("Helvetica", 10))
copy_button.pack(pady=10)

# Run the main application loop
root.mainloop()
