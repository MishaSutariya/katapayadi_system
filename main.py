import tkinter as tk
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
import re

katapayadi_values = {
    '1': ['क', 'ट', 'प', 'य'],
    '2': ['ख', 'ठ', 'फ', 'र'],
    '3': ['ग', 'ड', 'ब', 'ल'],
    '4': ['घ', 'ढ', 'भ', 'व'],
    '5': ['ङ', 'ण', 'म', 'श'],
    '6': ['च', 'त', 'ष'],
    '7': ['छ', 'थ', 'स'],
    '8': ['ज', 'द', 'ह'],
    '9': ['झ', 'ध'],
    '0': ['ञ', 'न',
          'अ', 'आ', 'ऄ', 'ओ', 'औ', 'ऑ', 'ऒ', 'ॲ', 'ॳ', 'ॴ', 'ॵ', 'ॶ', 'ॷ',
          'इ', 'ई', 'उ', 'ऊ', 'ऋ', 'ॠ', 'ऌ', 'ॡ',
          'ए', 'ऐ', 'ऎ', 'ऍ',
          'ॐ'
          ]
}

ignore_pattern = re.compile(r'([क-ह])्')

def convert_to_sanskrit():
    user_input = entry.get()

    source_script = sanscript.ITRANS
    target_script = sanscript.DEVANAGARI

    sanskrit_output1 = transliterate(user_input, source_script, target_script)

    sanskrit_output = ignore_pattern.sub('', sanskrit_output1)


    katapayadi_count = ""
    for char in sanskrit_output:
        for key, value in katapayadi_values.items():
            if char in value:
                katapayadi_count += key
                break

    reversed_katapayadi_count = katapayadi_count[::-1]

    if reversed_katapayadi_count.startswith('0'):
        reversed_katapayadi_count = reversed_katapayadi_count.lstrip('0')

    output_label.config(text=f"Sanskrit Output: {sanskrit_output1}\nKatapayadi Count : {reversed_katapayadi_count}")

root = tk.Tk()
root.title("Katapayadi Counter")

# GUI elements
label = tk.Label(root, text="Enter text:", font=("Arial", 14))
label.pack(pady=15)

entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=15)

convert_button = tk.Button(root, text="Convert", command=convert_to_sanskrit, font=("Arial", 12))
convert_button.pack(pady=15)

output_label = tk.Label(root, text="Sanskrit Output:", font=("Arial", 14))
output_label.pack(pady=15)

root.mainloop()


