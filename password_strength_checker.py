import math
import re

def load_rockyou(file_path="rockyou.txt"):
    print("Loading rockyou.txt password list (this may take a moment)...")
    with open(file_path, "r", encoding="latin-1") as f:
        passwords = set(line.strip() for line in f)
    print(f"Loaded {len(passwords)} passwords from rockyou.txt")
    return passwords

def calculate_entropy(password):
    charset_size = 0
    if re.search(r'[a-z]', password):
        charset_size += 26
    if re.search(r'[A-Z]', password):
        charset_size += 26
    if re.search(r'[0-9]', password):
        charset_size += 10
    if re.search(r'[^a-zA-Z0-9]', password):
        charset_size += 32  # Approximate for special chars
    
    if charset_size == 0:
        return 0

    entropy = len(password) * math.log2(charset_size)
    return entropy

def check_password_strength(password, common_passwords):
    feedback = []

    # Check if in common password list first
    if password.lower() in common_passwords:
        feedback.append("Password is in the common passwords list (rockyou.txt). Very weak! Change it.")
        entropy = calculate_entropy(password)
        feedback.append(f"Entropy: {entropy:.2f} bits (ignored due to common password)")
        return entropy, feedback

    # Company password standards:
    if len(password) < 12:
        feedback.append("Password should be at least 12 characters long.")

    if not re.search(r'[A-Z]', password):
        feedback.append("Include at least one uppercase letter.")

    if not re.search(r'[a-z]', password):
        feedback.append("Include at least one lowercase letter.")

    if not re.search(r'[0-9]', password):
        feedback.append("Include at least one digit.")

    if not re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
        feedback.append("Include at least one special character (e.g., !@#$%^&*).")

    entropy = calculate_entropy(password)

    if entropy < 28:
        feedback.append("Entropy is low: password is weak.")
    elif entropy < 36:
        feedback.append("Entropy moderate: password strength is fair.")
    elif entropy < 60:
        feedback.append("Entropy good: strong password.")
    else:
        feedback.append("Entropy excellent: very strong password.")

    if not feedback:
        feedback.append("Password meets all criteria and is strong.")

    return entropy, feedback

def main():
    common_passwords = load_rockyou()
    pwd = input("Enter a password to check: ")
    entropy, feedback = check_password_strength(pwd, common_passwords)
    print(f"\nEntropy: {entropy:.2f} bits")
    print("Feedback:")
    for f in feedback:
        print(f" - {f}")

if __name__ == "__main__":
    main()
