import string
import secrets

def generate_password(length=12):
    symbols = string.ascii_letters + string.digits + string.punctuation# Define characters for the password

    
    password = ''.join(secrets.choice(symbols) for _ in range(length))# Use secrets module for better randomness
    
    return password

def main():
    password_length = int(input("Enter the length of the password: "))
    generated_password = generate_password(password_length)
    
    print(f"Generated Password: {generated_password}")

if __name__ == "__main__":
    main()
