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
from Hacker import Hacker
from Rig import Rig

# token = Asset("CryptoToken", "Used to acquire or repair rigs")
# print(token)
#
# token.switch_encryption()
# print(token)
#
# print("Encrypted state:", token.encrypted)
# token.encrypted = False
# print("After decrypting :", token)

# test_rig = Rig("Alpha")
# print(test_rig)

test_hacker = Hacker("Alpha")
print(test_hacker)

test_hacker.acquire_rig()
print(test_hacker)
