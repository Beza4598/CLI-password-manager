from cryptography.fernet import Fernet
from typing import Optional
import string
import random

class PasswordEncryption:

    def __int__(self, master_key: Optional[str]):
        self.master_key = master_key

    def generate_master_key(self) -> str:
        key = Fernet.generate_key()
        return key

    def encrypt_login_details(self, info):

        f = Fernet(self.master_key)
        return f.encrypt(info)

    def decrypt_login_details(self, encrypted_token):

        f = Fernet(self.master_key)
        return f.decrypt(encrypted_token)

    def generate_password(self):
        # define password length
        length = 16

        # define characters to use in password
        characters = string.ascii_letters + string.digits + string.punctuation

        while True:
            password = ''.join(random.choice(characters) for i in range(length))
            if (any(char.isupper() for char in password)
                    and any(char.islower() for char in password)
                    and any(char.isdigit() for char in password)
                    and any(char in string.punctuation for char in password)):
                break

        return password