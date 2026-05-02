# Cyber-Security-project

# 🛡️ Cyper Studio

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GUI](https://img.shields.io/badge/GUI-CustomTkinter-orange.svg)](https://github.com/TomSchimansky/CustomTkinter)

**Cyper Studio** is a modern, high-performance cryptography application built with Python and CustomTkinter. It provides a sleek, user-friendly interface for encrypting and decrypting text and files using a variety of classical cryptographic algorithms.

---

## ✨ Features

- 🎨 **Modern UI:** Built with CustomTkinter for a premium, high-DPI desktop experience.
- 🌓 **Dynamic Themes:** Supports Dark, Light, and System appearance modes.
- 🔐 **Secure Access:** Integrated login system to protect your workspace.
- 📝 **Text Encryption:** Quickly encrypt and decrypt text strings with real-time feedback.
- 📁 **File Encryption:** Secure entire text files with just a few clicks.
- ⚙️ **Modular Design:** Highly organized codebase for easy extension and maintenance.

## 🚀 Supported Algorithms

Cyper Studio includes custom implementations of the following ciphers:

- **Caesar Cipher:** Classic substitution cipher.
- **Vigenere Cipher:** Polyalphabetic substitution using a keyword.
- **Playfair Cipher:** Bigram substitution using a 5x5 matrix.
- **Hill Cipher:** Linear algebra-based polygraphic substitution (2x2 matrix).
- **Rail Fence Cipher:** Transposition cipher based on a "zigzag" pattern.
- **Columnar Transposition:** Key-based transposition cipher.
- **ROT13:** A special case of the Caesar cipher.

---

## 🛠️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/cyper-studio.git
cd cyper-studio
```

### 2. Install dependencies
Ensure you have Python 3.8+ installed. Install the required libraries using pip:
```bash
pip install -r requirements.txt
```

---

## 📖 Usage

### Launch the Application
Run the main script to start the application:
```bash
python gui_app.py
```

### How to use:
1. **Login:** Use the default credentials (`admin` / `admin`) to enter.
2. **Select Cipher:** Choose your desired algorithm from the sidebar.
3. **Set Key:** Enter the secret key required for the chosen cipher.
4. **Encrypt/Decrypt:** 
   - Paste text into the "Input Text" area and click **Encrypt ➔**.
   - Or, select a file using the **📁 Select File** button and use the **🔐 Encrypt File** option.

---

## 📂 Project Structure

```text
cyper/
├── core_ciphers.py      # Implementation of all cryptographic algorithms
├── cipher_wrapper.py    # Interface for handling different cipher types
├── gui_app.py           # Main application entry and GUI logic
├── requirements.txt     # List of project dependencies
└── README.md            # Project documentation
```

## 🤝 Contributing

Contributions are welcome! If you have ideas for new ciphers or UI improvements:
1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## ⚖️ License

Distributed under the MIT License. See `LICENSE` for more information.

---

<p align="center">
  Developed with ❤️ for secure communication.
</p>
