
import random
import time
import string
from getpass import getpass

# Function to brute-force the password
def brute_force(usr, char_set):
    """Brute-forces password using the specified character set."""
    crack = ""
    attempts = 0
    while crack != usr:
        crack = ""
        for _ in range(len(usr)):
            crack += random.choice(char_set)
        attempts += 1
        print(f"[Attempt {attempts}] {crack}", end='\r')  # Update on same line for cleaner output
    return crack, attempts

# Password Strength Checker
def check_password_strength(password):
    """Evaluates password strength."""
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)

    # Evaluate password strength
    if length >= 8 and has_upper and has_lower and has_digit and has_symbol:
        return "Strong"
    elif length >= 6 and (has_upper or has_lower) and (has_digit or has_symbol):
        return "Medium"
    else:
        return "Weak"

# Main function to select the brute-forcer
def main():
    usr = getpass("Enter your password: ")

    # Password strength evaluation
    strength = check_password_strength(usr)
    print(f"Password strength: {strength}")

    print("Choose your brute-forcer:")
    print("1. Symbol Brute Forcer")
    print("2. Uppercase Brute Forcer")
    print("3. Number Brute Forcer")
    print("4. Lowercase Brute Forcer")
    print("5. All Combinations Brute Forcer (Lowercase + Uppercase + Symbols + Digits)")
    print("6. Uppercase + Lowercase Brute Forcer")
    print("7. Uppercase + Symbols Brute Forcer")
    print("8. Symbols + Digits Brute Forcer")
    print("9. Lowercase + Symbols Brute Forcer")
    print("10. Lowercase + Digits Brute Forcer")
    print("11. Uppercase + Digits Brute Forcer")

    choice = input("Enter choice (1-11): ")

    # Character sets for different brute-forcers
    if choice == "1":
        char_set = string.punctuation
        print("Using Symbol Brute Forcer...")
    elif choice == "2":
        char_set = string.ascii_uppercase
        print("Using Uppercase Brute Forcer...")
    elif choice == "3":
        char_set = string.digits
        print("Using Number Brute Forcer...")
    elif choice == "4":
        char_set = string.ascii_lowercase
        print("Using Lowercase Brute Forcer...")
    elif choice == "5":
        char_set = string.ascii_letters + string.digits + string.punctuation
        print("Using All Combinations Brute Forcer...")
    elif choice == "6":
        char_set = string.ascii_uppercase + string.ascii_lowercase
        print("Using Uppercase + Lowercase Brute Forcer...")
    elif choice == "7":
        char_set = string.ascii_uppercase + string.punctuation
        print("Using Uppercase + Symbols Brute Forcer...")
    elif choice == "8":
        char_set = string.punctuation + string.digits
        print("Using Symbols + Digits Brute Forcer...")
    elif choice == "9":
        char_set = string.ascii_lowercase + string.punctuation
        print("Using Lowercase + Symbols Brute Forcer...")
    elif choice == "10":
        char_set = string.ascii_lowercase + string.digits
        print("Using Lowercase + Digits Brute Forcer...")
    elif choice == "11":
        char_set = string.ascii_uppercase + string.digits
        print("Using Uppercase + Digits Brute Forcer...")
    else:
        print("Invalid choice!")
        return

    # Start brute-force attack
    print("Starting brute-force attack...")
    time.sleep(2)
    crack, attempts = brute_force(usr, char_set)
    print(f"\nPassword cracked: {crack} in {attempts} attempts!")

# Run the script
if __name__ == "__main__":
    main()
