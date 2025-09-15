import hashlib
import getpass
import sqlite3

# Connect to SQLite database (creates it if it doesn't exist)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create table for users if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
''')

def hash_password(password):
    """Hash a password using SHA-256 for demonstration purposes."""
    return hashlib.sha256(password.encode()).hexdigest()

def check_password(stored_password, provided_password):
    """Check if a provided password matches the stored hashed password."""
    return stored_password == hash_password(provided_password)

def register_user():
    """Register a new user."""
    username = input("Enter username: ")
    if cursor.execute('SELECT * FROM users WHERE username =?', (username,)).fetchone():
        print("Username already exists. Please choose another.")
        return

    password = getpass.getpass("Enter password: ")
    confirm_password = getpass.getpass("Confirm password: ")

    if password!= confirm_password:
        print("Passwords do not match. Registration failed.")
        return

    # Hash the password before storing
    hashed_password = hash_password(password)
    
    cursor.execute('INSERT INTO users (username, password) VALUES (?,?)', (username, hashed_password))
    conn.commit()
    print("User registered successfully.")

def login_user():
    """Login an existing user."""
    username = input("Enter username: ")
    cursor.execute('SELECT password FROM users WHERE username =?', (username,))
    stored_password = cursor.fetchone()
    
    if stored_password is None:
        print("Username does not exist.")
        return

    provided_password = getpass.getpass("Enter password: ")
    if check_password(stored_password[0], provided_password):
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
    conn.close()  # Close the database connection

