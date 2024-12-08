def caesar_cipher(text, shift, operation):
    result = ""
    if operation == "decrypt":
        shift = -shift  # Reverse the shift for decryption

    for char in text:
        if char.isalpha():
            # Preserve case (uppercase/lowercase)
            start = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            # Non-alphabetic characters remain unchanged
            result += char
    return result


# User interaction
print("Caesar Cipher Program")
message = input("Enter your message: ")
shift_value = int(input("Enter the shift value: "))
choice = input("Choose 'encrypt' or 'decrypt': ").lower()

if choice in ['encrypt', 'decrypt']:
    output = caesar_cipher(message, shift_value, choice)
    print(f"Result: {output}")
else:
    print("Invalid choice. Please select 'encrypt' or 'decrypt'.")
