import hashlib
import getpass

# Simple in-memory storage (replace with a database for production use)
users = {}

def hash_password(password):
    """Hash a password using SHA-256 for demonstration purposes."""
    return hashlib.sha256(password.encode()).hexdigest()

def check_password(stored_password, provided_password):
    """Check if a provided password matches the stored hashed password."""
    return stored_password == hash_password(provided_password)

def register_user():
    """Register a new user."""
    username = input("Enter username: ")
    if username in users:
        print("Username already exists. Please choose another.")
        return

    password = getpass.getpass("Enter password: ")
    confirm_password = getpass.getpass("Confirm password: ")

    if password!= confirm_password:
        print("Passwords do not match. Registration failed.")
        return

    # Hash the password before storing
    hashed_password = hash_password(password)
    
    users[username] = {
        'username': username,
        'password': hashed_password
    }
    print("User registered successfully.")

def login_user():
    """Login an existing user."""
    username = input("Enter username: ")
    if username not in users:
        print("Username does not exist.")
        return

    password = getpass.getpass("Enter password: ")
    if check_password(users[username]['password'], password):
        print("Login successful.")
    else:
        print("Incorrect password.")

def main():
    while True:
        print("\nUser Authentication Menu:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            register_user()
        elif choice == '2':
            login_user()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()

