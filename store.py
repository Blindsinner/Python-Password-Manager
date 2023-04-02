import os
import getpass
from cryptography.fernet import Fernet
import base64
import hashlib

def main():
    if not os.path.isfile("passwords.txt"):
        manager_password = getpass.getpass("Set a password for the password storage manager: ")

        key = hashlib.sha256(manager_password.encode()).digest()
        cipher_suite = Fernet(base64.urlsafe_b64encode(key))
        encrypted_manager_password = cipher_suite.encrypt(manager_password.encode()).decode()

        with open("passwords.txt", "w") as f:
            f.write(encrypted_manager_password)

    while True:
        entered_password = getpass.getpass("Enter the password for the password storage manager: ")

        with open("passwords.txt", "r") as f:
            encrypted_saved_password = f.readline().strip()

        key = hashlib.sha256(entered_password.encode()).digest()
        cipher_suite = Fernet(base64.urlsafe_b64encode(key))
        decrypted_saved_password = cipher_suite.decrypt(encrypted_saved_password.encode()).decode()

        if entered_password == decrypted_saved_password:
            break
        else:
            print("Wrong password! Try again.")

    while True:
        print("\n1. Save a new password")
        print("2. View saved passwords")
        print("3. Delete a password")
        print("4. Exit")
        choice = input("Enter your choice (1, 2, 3 or 4): ")

        if choice == "1":
            input_password = getpass.getpass("Enter your derived password: ")
            input_salt = input("Enter the stored salt: ")

            password_name = input("What is the name for the generated password? ")

            key = hashlib.sha256(entered_password.encode()).digest()
            cipher_suite = Fernet(base64.urlsafe_b64encode(key))
            encrypted_password = cipher_suite.encrypt(input_password.encode()).decode()

            with open("passwords.txt", "a") as f:
                f.write(f"\n{password_name}: {encrypted_password}, {input_salt}")
            print("Password saved. Exiting...")
            break
        elif choice == "2":
            with open("passwords.txt", "r") as f:
                lines = f.readlines()
                print("\nYour saved passwords:")
                for line in lines[1:]:
                    parts = line.strip().split(": ")
                    if len(parts) == 2:
                        password_name, encrypted_password_and_salt = parts
                        encrypted_password, salt = encrypted_password_and_salt.split(', ')
                        decrypted_password = ""
                        try:
                            encrypted_password = encrypted_password.encode()
                            key = hashlib.sha256(entered_password.encode()).digest()
                            cipher_suite = Fernet(base64.urlsafe_b64encode(key))
                            decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
                        except:
                            decrypted_password = "******"
                        print(f"{password_name}: {decrypted_password}, {salt}")
                    else:
                        print(f"Invalid password format: {line}")
            break
        elif choice == "3":
            with open("passwords.txt", "r") as f:
                lines = f.readlines()
                print("\nYour saved passwords:")
                for i, line in enumerate(lines[1:]):
                    print(f"{i+1}. {line.strip().split(':')[0]}")
            password_number = int(input("Enter the number of the password you want to delete (or 0 to cancel): "))
            if password_number == 0:
                continue
            elif 1 <= password_number <= len(lines) - 1:
                with open("passwords.txt", "w") as f:
                    for i, line in enumerate(lines):
                        if i != password_number:
                            f.write(line)
                print("Password deleted.")
            else:
                print("Invalid choice. Please enter a valid option.")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
