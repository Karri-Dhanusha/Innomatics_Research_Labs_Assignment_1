"""
Simple Login Authentication System
Validates user credentials against predefined credentials.
"""

# Predefined valid credentials
VALID_USERNAME = "admin"
VALID_PASSWORD = "1234"


def authenticate_user():
    """
    Prompts user for credentials and validates them.
    Returns True if credentials match, False otherwise.
    """
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    return username == VALID_USERNAME and password == VALID_PASSWORD


def main():
    """Main function to handle login flow."""
    if authenticate_user():
        print("Login Successful")
    else:
        print("Invalid Credentials")


if __name__ == "__main__":
    main()