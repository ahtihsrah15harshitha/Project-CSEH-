# Project-CSEH-
 🔐 Password Strength Analyzer & Custom Wordlist Generator

A Python-based tool to analyze password strength and generate custom wordlists using user-defined inputs. Supports both **GUI (Tkinter)** and **CLI (argparse)** modes. Ideal for security testing, password audits, and ethical hacking practice.
YOU CAN ALSO DOWNLOAD THE .EXE FILE TO SEE THE DEMO

---

## 🚀 Features

- ✅ Analyze password strength using `zxcvbn`
- ✅ Generate custom wordlists based on:
  - Name, DOB, pet name, extra keywords
  - Capitalized and leetspeak versions
  - Year patterns (e.g., `word2023`, `2022word`)
- ✅ Save the wordlist as `.txt` for use with password cracking tools
- ✅ Dual Interface: GUI using Tkinter and CLI with argparse
- ✅ Modular, well-structured code

---

## 🗂️ File Overview

| File Name             | Purpose                                       |
|----------------------|-----------------------------------------------|
| `gui_pa.py`           | GUI application using Tkinter                 |
| `cli_interface.py`    | Command-line interface using argparse         |
| `custom_wordlist.py`  | Wordlist generator with leetspeak and years   |
| `password_strength.py`| Analyzes password strength using `zxcvbn`     |
| `save_file.py`        | Exports the generated wordlist to `.txt`      |
| `README.md`           | Project documentation                         |

Documentation of my project and its insights are provided in pdf format
Check out for implementation !!

---

## 🖥️ Usage
-- To analyze the strength of the password on a scale of 0-4
-- To generate wordlist of various combinations using the input values(name,pet,dob,extra)
-- To save the generated wordlist into a readable text file
### ▶️ GUI Mode
```bash
python gui_pa.py
Enter password, name, DOB, pet name, and extra words

Click Submit

Wordlist will be saved and confirmation shown

▶️ CLI Mode

python cli_interface.py -p <password> -n <name> -d <dob> -pet <petname> -e word1 
