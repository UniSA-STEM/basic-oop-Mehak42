"""
File: Asset.py
Description: Represents the digital assets used by Hackers and Rigs
Author: Mehakdeep Kaur Tiwana
ID: 110397073
Username: TIWMY001
This is my own work as defined by the University's Academic Misconduct Policy.
"""

"""This class represents the digital assets such has CryptoToken, Data Spike or hardware patch"""
class Asset:
    def __init__(self,name,description):
        self.__name = name
        self.__description = description
        self.__encrypted = False

    """getters and setters defined """
    def get_name(self):
        return self.__name
    def get_description(self):
        return self.__description
    def get_encrypted(self):
        return self.__encrypted
    def set_name(self, value):
        self.__name = value
    def set_description(self, value):
        self.__description = value
    def set_encrypted(self, value):
        self.__encrypted = bool(value)

    """Using property attribute to make use of getter and setter in the other classes"""
    name = property(get_name,set_name)
    description = property(get_description,set_description)
    encrypted = property(get_encrypted,set_encrypted)

    def switch_encryption(self):
        """switches the encryption from true to false"""
        self.__encrypted = not self.__encrypted

    def __str__(self):
        if self.__encrypted:
            return f"{self.__name}: {self.__description} [Encrypted]"
        else:
            return f"{self.__name}: {self.__description}"




