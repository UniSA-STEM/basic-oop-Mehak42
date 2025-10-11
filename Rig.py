"""
File: Rig.py
Description: This class represents a rig (computer) used by a hacker.
Author: Mehakdeep Kaur Tiwana
ID: 110397073
Username: TIWMY001
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Asset import Asset

class Rig:
    def __init__(self, name):
        self.__name = name
        self.__damage = 0
        self.__broken = False
        self.__storage = []
        self.__upgrade_level = 0

        """Each rig starts with two Data spikes and one removable drive"""
        self.__storage.append(Asset("Data Spike", "Used in battles"))
        self.__storage.append(Asset("Data Spike", "Used in battles"))
        self.__storage.append(Asset("Removable Drive", "Found in rigs and used for extraction"))

    """getters and setters"""
    def get_name(self):
        return self.__name
    def get_damage(self):
        return self.__damage
    def get_broken(self):
        return self.__broken
    def get_storage(self):
        return self.__storage
    def get_upgrade_level(self):
        return self.__upgrade_level
    def set_name(self, value):
        self.__name = value
    def set_damage(self, value):
        self.__damage = value
    def set_broken(self, value):
        self.__broken = bool(value)
    def set_storage(self, value):
        self.__storage = value

