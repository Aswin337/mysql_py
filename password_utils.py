print("Loaded password_utils!")
from cryptography.fernet import Fernet
class Fakestr(str):
    def __str__(self):
        return "******"
    def __repr__(self):
        return "******"
def load_key():
    return open("secret.key","rb").read()
def encrypt_password(password):
    key=load_key()
    f=Fernet(key)
    return f.encrypt(password.encode())
def decrypt_password(encrypted_password):
    key=load_key()
    f=Fernet(key)
    decrypt=f.decrypt(encrypted_password).decode()
    return Fakestr(decrypt) 
def get_decrypt_password():
    encrypted_password=b'gAAAAABoYBkaP3uJFtIU80RHjcCNW7KLE7uC6rc-Jxzwej7c9G2p1fzPFOnb-uCSZMRFadou48nMWwG8WNKIs8yXB8QM0Xkw7A=='
    return decrypt_password(encrypted_password)