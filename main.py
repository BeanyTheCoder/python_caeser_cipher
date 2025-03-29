def caeser_cipher(text, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for i in text:
        if not i in alphabet:
            result += i
            continue
        
        shiftedIndex = alphabet.index(i) + shift
        result += alphabet[shiftedIndex % 26]
        
    return result

text = input("Enter text to encrypt/decrypt: ")
shift = input("Enter shift:  ")

print(caeser_cipher(text, int(shift)))
