# Run "python main.py", then enter the `text` to be encrypted or decrypted,
# enter the `shift`(any integer works) and whether you want to encrypt or decrypt(y/n).

# Your encrypted/decypted text should be highlighted red. 
# It's automatically copied to clipboard so you can share the encrypted message,
# or decrypt it, by running the program again, choosing the same `shift` and choosing decrypt(`n`).

# You can play around with random strings of letters and try and decrypt them into a meaningful message.

import pyperclip

def caeser_cipher(text, shift, mode):
    # type checking
    if not type(text) == str:
        raise TypeError("Input must be a string")
    
    if not type(shift) == int:
        raise TypeError("Shift must be an integer")
    
    if not type(text) == str or mode not in ["y", "n"]:
        raise ValueError("Mode must be either 'y' (encrypt) or 'n' (decrypt)")

    text = text.lower()
    shift = abs(shift)

    # adjust shift for decryption
    if mode == "n":  
        shift = -shift

    # alphanumerical reference
    reference = "abcdefghijklmnopqrstuvwxyz0123456789,./;'\"[]\\-=~!@#$%^&*()"

    result = ""

    for i in text:
        if i not in reference:
            result += i
            continue
        
        # generates a shifted index based on given shift
        shifted_index = (reference.index(i) + shift)
        
        # appends a shifted character to result. modulo(%) is to prevent overflow
        result += reference[shifted_index] % len(reference)

    return result

text = input("Enter text to encrypt/decrypt: ")
shift = int(input("Enter shift:  "))
mode = input("Are you encrypting or decrypting? (y for encrypt, n for decrypt): ").strip().lower()

result = caeser_cipher(text, shift, mode)

# `\033[31m` for red color text, `\033[0` to reset the color to normal
print(f"Result: \033[31m{result}\033[0m has been copied to clipboard for sharing and decryption")
pyperclip.copy(result)
