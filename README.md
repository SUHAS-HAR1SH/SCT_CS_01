# SCT_CS_01
A Python program to encrypt and decrypt text using the Caesar Cipher algorithm. It supports encryption, decryption, case sensitivity, and handles non-alphabetic characters. Ideal for learning cryptography basics and improving Python skills. User-friendly and perfect for beginners!
🚀 Features
Encryption: Converts plain text into cipher text using a user-defined shift value.
Decryption: Restores the original message by reversing the shift.
Case Sensitivity: Maintains uppercase and lowercase characters.
Non-Alphabet Support: Leaves symbols, numbers, and spaces unaltered.
User-Friendly: Command-line interface with clear prompts for input.
📋 How It Works
The Caesar Cipher shifts each letter in the input text by a fixed number of places in the alphabet. For example:

Encrypt: "HELLO" with a shift of 3 becomes "KHOOR".
Decrypt: "KHOOR" with the same shift returns "HELLO".
This program uses modular arithmetic to wrap around the alphabet and ensures all characters are processed correctly.

🛠️ Installation & Usage
Prerequisites
Python 3.x installed on your system.
Steps
Clone this repository:
bash
Copy code
git clone https://github.com/your-username/caesar-cipher-tool.git
cd caesar-cipher-tool
Run the program:
bash
Copy code
python caesar_cipher.py
Follow the prompts:
Input your message.
Provide the shift value.
Choose whether to encrypt or decrypt.
👨‍💻 Example
Input:

plaintext
Copy code
Enter your message: Hello World  
Enter the shift value: 3  
Choose 'encrypt' or 'decrypt': encrypt  
Output:

plaintext
Copy code
Result: Khoor Zruog  
📚 Concepts Covered
Substitution ciphers and cryptographic basics.
Python string manipulation and control structures.
Modular arithmetic for alphabet wrapping.
🤝 Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue if you have suggestions for improvements, bugs, or new features.

🛡️ License
This project is licensed under the MIT License. See the LICENSE file for details.

🌟 Acknowledgments
Wikipedia: Caesar Cipher Algorithm
Python Documentation: String Handling
