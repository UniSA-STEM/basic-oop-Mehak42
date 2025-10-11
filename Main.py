"""
File: main.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
# Testing Asset class
from Asset import Asset

token = Asset("CryptoToken", "Used to acquire or repair rigs")
print(token)

token.switch_encryption()
print(token)

print("Encrypted state:", token.encrypted)
token.encrypted = False
print("After decrypting :", token)