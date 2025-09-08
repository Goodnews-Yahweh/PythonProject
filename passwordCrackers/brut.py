
import random
import time
import string
from getpass import getpass

def brute_force(usr, char_set):
    """Brute-forces password using specified character set."""
    crack = ""
    attempts = 0
    while crack != usr:
        crack = ""
        for _ in range(len(usr)):
            crack += random.choice(char_set)
        attempts += 1
        print(f"[Attempt {attempts}] {crack}")
    return crack, attempts

def main():
    usr = getpass("Enter your password: ")
    print("Choose your brute-forcer:")
    print("1. Symbol Brute Forcer")
    print("2. Uppercase Brute Forcer")
    print("3. Number Brute Forcer")
    print("4. Lowercase Brute Forcer")

    choice = input("Enter choice (1-4): ")

    # Character sets based on user choice
    if choice == "1":
        char_set = string.punctuation
    elif choice == "2":
        char_set = string.ascii_uppercase
    elif choice == "3":
        char_set = string.digits
    elif choice == "4":
        char_set = string.ascii_lowercase
    else:
        print("Invalid choice!")
        return

    print(f"Starting brute-force attack on {usr}...")
    time.sleep(2)
    crack, attempts = brute_force(usr, char_set)
    print(f"Password cracked: {crack} in {attempts} attempts!")

if __name__ == "__main__":
    main()
