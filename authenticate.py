# projects/basic_programs/authenticate.py

import sys


def ask_username():
    """Ask the user for a username with validation."""
    raw_username = input("Username: ")

    # Remove spaces and other whitespace at the beginning and end
    username = raw_username.strip()

    # 1. Too short?
    if len(username) < 3:
        print("The username is too short (minimum 3 characters).")
        sys.exit(1)

    # 2. Contains spaces or tabs?
    if " " in username or "\t" in username:
        print("The username may not contain spaces or tabs.")
        sys.exit(42)

    # Otherwise the username is valid
    return username


def ask_password(username):
    """Ask the user for a password with validation."""
    password = input("Password: ")

    # 1. Too short?
    if len(password) < 5:
        print("The password should be at least length 5.")
        sys.exit(46)

    # 2. Same as username?
    if password == username:
        print("Password may not be equal to username.")
        sys.exit(45)

    return password


def is_welcome(name, passwd):
    """Return True only for Bob/secret and Alice/12345."""
    if name == "Bob" and passwd == "secret":
        return True
    if name == "Alice" and passwd == "12345":
        return True
    return False


def main():
    username = ask_username()
    password = ask_password(username)

    if is_welcome(username, password):
        message = f"Welcome {username}."
    else:
        message = f"Not allowed, {username}."
    print(message)
    sys.exit(0)


if __name__ == "__main__":
    main()
