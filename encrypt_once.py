from password_utils import encrypt_password
from cryptography.fernet import Fernet
def Generate_key():
    key=Fernet.generate_key()
    with open("secret.key","wb") as file:
        file.write(key)
    print("key saved to secret key !")
if __name__ =="__main__":
#uncomment this only first time
    #Generate_key()
    encrypt=encrypt_password("root")
    print("Encrypted password(copy to this password_util) :")
    print(encrypt)
