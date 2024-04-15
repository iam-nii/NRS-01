from cryptography.fernet import Fernet


KEY = b'4bZCJ0pWMDgVco8ejOR-L9UDMUVEbBjxLCQc5E7t4mY='
print("key:")
print(KEY)

class EncDecPass:
    def __init__(self):
        # generate a key for encryption and decryption
        # You can use fernet to generate the key or use random key generator
        # here I'm using fernet to generate key
        self.key = KEY

        # Instance the Fernet class with the key
        self.fernet = Fernet(self.key)

    def encrypt_password(self, password):
        # then use the Fernet class instance
        # to encrypt the string string must
        # be encoded to byte string before encryption
        return self.fernet.encrypt(password.encode())

    def decrypt_password(self, encoded_password):
        return self.fernet.decrypt(encoded_password)
