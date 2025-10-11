"""
File: Asset.py
Description: Represents the digital assets used by Hackers and Rigs
Author: Mehakdeep Kaur Tiwana
ID: 110397073
Username: TIWMY001
This is my own work as defined by the University's Academic Misconduct Policy.
"""

"""This class represents the digital assets such has CrptoToken, Data Spike or hardware patch"""
class Asset:
    def __init__(self,name,description):
        self.name = name
        self.description = description
        self.encrypted = False

"""getters and setters defined """
    def get_name(self):
        return self.name
    def get_description(self):
        return self.description
    def get_encrypted(self):
        return self.encrypted
    def set_name(self,value):
        self.name = value
    def set_description(self,value):
        self.description = value
    def set_encrypted(self,value):
        self.encrypted = bool(value)





