
# Password Manager

This is a simple password manager command-line application written in Python that allows you to securely store and retrieve your passwords. It uses a user-defined master password to encrypt and decrypt the password database file.

## Features

-   Store passwords with labels and URLs.
-   Passwords are encrypted using the master password with a strong hashing algorithm (SHA-512) and a random salt.
-   View passwords in the terminal or copy them to the clipboard.
-   Delete passwords from the database. (Password will store in a local .txt file with encryption)

## Installation

1.  Clone the repository: `git clone https://github.com/Blindsinner/Python-Password-Manager.git`
2.  Install the required dependencies: `pip install -r requirements.txt`
3.  Run the application: `python store.py`

## Usage

1.  On first run, you will be prompted to set a master password.
2.  Use the menu to add, view, or delete passwords.
3.  When viewing a password, you can choose to copy it to the clipboard or exit to the menu.
4.  To exit the program, choose "Exit" from the menu.

## License

This project is licensed under the [MIT License].

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

