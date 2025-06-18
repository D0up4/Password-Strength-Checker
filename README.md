# 🎯 Password Strength Checker with Common Password Detection

**Author:** D0up4      
**Last Updated:** 06/2025  
**Project Type:** Cybersecurity / Password Security Tool  

---

## 📘 Description

This is a Python-based password strength checker designed to help users and security professionals evaluate password robustness. It combines traditional strength checks based on company password policies with a check against the well-known `rockyou.txt` list of common passwords.

The tool:

- Flags passwords found in the `rockyou.txt` common password list as very weak.
- Enforces company-style password requirements:
  - Minimum length (default 12 characters)
  - At least one uppercase letter
  - At least one lowercase letter
  - At least one digit
  - At least one special character
- Calculates password entropy to estimate randomness and strength.
- Provides clear, actionable feedback for improving passwords.

This is ideal for personal use, cybersecurity training, or as part of a portfolio demonstrating password security awareness.

---

## ⚙️ Features

- **Common Password Detection:** Uses the `rockyou.txt` password list to identify weak, frequently used passwords.
- **Company Password Policy Checks:** Verifies password meets common corporate security standards.
- **Entropy Calculation:** Estimates password randomness in bits.
- **Detailed Feedback:** Offers step-by-step guidance on strengthening passwords.
- **Lightweight:** Pure Python, no heavy dependencies.

---

## 🚀 Usage

1. Ensure you have the `rockyou.txt` file in the same directory as the script (or update the path in the code).  
   The `rockyou.txt` password list can be downloaded from various public repositories (e.g., SecLists on GitHub).

2. 🧪 Run the script:

   ```bash
   python password_strength_checker.py
