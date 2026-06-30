from cryptography.fernet import Fernet
import os
import random
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import base64

def confirm_overwrite(filepath):
    if os.path.exists(filepath):
        response = input(f"{filepath} slow down playa you might delete something important do you wish to overwrite y/n: ")
        return response.lower() == 'y'
    return True

def password_to_key(password: str, salt: bytes = b"mysalt123"):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key
def generate_password(length=32):
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "1234567890"
    symbol = "`~!@#$%^&*()_-+={|}:;,<?/>"

    all_chars = lowercase + uppercase + numbers + symbol

    password_chars = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(numbers),
        random.choice(symbol)
    ]

    for _ in range(length - 4):
        password_chars.append(random.choice(all_chars))

    random.shuffle(password_chars)
    return "".join(password_chars)

# Define the key
def write_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load the key
def load_key():
    return open("secret.key", "rb").read()

# Encrypt the file

def encrypt_file(filename, key):
    f = Fernet(key)
    # Read the file
    with open(filename, "rb") as file:
        data = file.read()
        
    encrypted = f.encrypt(data)
    out_file = filename + ".encrypted"

    # Check yourself before you wreck yourself
    if not confirm_overwrite(out_file):
        print("Encryption canceled")
        return
    
    with open(out_file, "wb") as file:
        file.write(encrypted)

# Decrypt the file

def decrypt_file(filename, key):
    f = Fernet(key)
    # Read encrypted file
    with open(filename, "rb") as file:
        encrypted_data = file.read()

    decrypted =f.decrypt(encrypted_data)
    out_file = filename.replace(".encrypted", "")

    if not confirm_overwrite(out_file):
        print("Decryption canceled")
        return
    
    with open(out_file, "wb") as file:
        file.write(decrypted)

# User Input for Encrypt/Decrypt
print("1. Generate a key")
print("2. Encrypt a file")
print("3. Decrypt a file")
print("4. Generate a password-based key")
print("5. Encrypt/Decrypt using Master Password")

choice = input("Choose an option: ")

if choice == "1":
    write_key()
    print("Key generated and saved to secret.key")
elif choice == "2":
    filename = input("File to encrypt: ")
    key = load_key()
    encrypt_file(filename, key)
    print("File Encrypted")
elif choice == "3":
    filename = input("File to decrypt: ")
    key = load_key()
    decrypt_file(filename, key)
    print("File decrypted!")
elif choice == "4":
    password = generate_password()
    print("Generated password:", password)

    key = password_to_key(password)
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

    print("Password-based key saved to secret.key")
elif choice == "5":
    password = input("Enter your master password: ")
    key = password_to_key(password)
    action = input("Encrypt (E) or Decrypt (D)? ").lower()

    if action == "e":
        filename = input("File to encrypt: ")
        encrypt_file(filename, key)
        print("File encrypted with master password")

    elif action == "d":
        filename = input("File to decrypt: ")
        decrypt_file(filename, key)
        print("File decrypted with master password")
        