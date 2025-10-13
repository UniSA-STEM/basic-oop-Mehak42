"""
File: Hacker.py
Description: Hacker who owns rig and inventory of assets
Author: Mehakdeep Kaur Tiwana
ID: 110397073
Username: TIWMY001
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Rig import Rig
from Asset import Asset

class Hacker:
    def __init__(self, name):
        self.__name = name
        self.__inventory = []
        self.__rig = None
        self.__trace_level = 0

        self.__inventory.append(Asset("CryptoToken", "Used to acquire or repair rigs"))

    def get_name(self):
        return self.__name
    def get_inventory(self):
        return self.__inventory
    def get_rig(self):
        return self.__rig
    def get_trace_level(self):
        return self.__trace_level
    def set_name(self, name):
        self.__name = name
    def set_trace_level(self, trace_level):
        self.__trace_level = max(0, int(trace_level))

