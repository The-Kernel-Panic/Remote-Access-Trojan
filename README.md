# Remote-Access-Trojan
A Remote Access Trojan written in python

There are two files:
1. The Trojan.py which you'll send to the victim.
2. The Payload_Generator.py which you'll use to create an encrypted payload for the Trojan.

The Trojan.py consists of 3 parts:
1. A normal code (Add any non-malicious python code here to make the victim run your code)
2. A decryption engine (It will automactically decrypt the encrypted payload)
3. An encrypted payload (Currently its a reverse shell but you can change this using the 'Payload_Generator.py' program)

Note:
1. You can use the 'key = Fernet.generate_key()' option to generate a new key to replace the old one incase the code gets flagged by AV software.
2. The reverse shell is currently set on localhost. Change it to your own ip and regenerate the payload using the Payload_Generator.py before using on a victim.
