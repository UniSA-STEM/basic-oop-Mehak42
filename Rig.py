"""
File: Rig.py
Description: This class represents a rig (computer) used by a hacker.
Author: Mehakdeep Kaur Tiwana
ID: 110397073
Username: TIWMY001
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import random
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
    def set_upgrade_level(self, value):
        self.__upgrade_level = value

    name = property(get_name, set_name)
    damage = property(get_damage, set_damage)
    broken = property(get_broken, set_broken)
    upgrade_level = property(get_upgrade_level, set_upgrade_level)
    storage = property(get_storage, set_storage)

    def repair(self):
        pass

    def upgrade(self):
        pass

    def take_hits(self):
        self.__damage += 1
        if self.__damage >= 2:
            self.__broken = True

    def generate_assets(self):
        """Generates new assets and adds it to the storage"""
        spawn_assets = random.randint(1, 3)
        if spawn_assets == 1:
            new_asset = Asset("Data Spike", "Used in battles")
            print(f"{self.__name} generated a Data Spike.")
        elif spawn_assets == 2:
            new_asset = Asset("Removable Drive", "Used for extraction")
            print(f"{self.__name} generated a Removable Drive.")
        elif spawn_assets == 3:
            new_asset = Asset("Security Chip", "Used for encryption and decryption")
            print(f"{self.__name} generated a Security Chip.")

    def store_assets(self, asset):
        """stores new assets inside rig's storage if it's not encrypted"""
        if asset.encrypted:
            print(f"Cannot store {asset.name} : asset is encrypted.")
        else:
            self.__storage.append(asset)
            print(f"{asset.name} stored in {self.__name}")

    def release_asset(self, asset_name):
        """releases asset from rig's storage if it's not encrypted"""
        for asset in self.__storage:
            if asset.name == asset_name:
                if asset.encrypted:
                    print(f"Cannot release asset {asset.name} : asset is encrypted.")
                    return None
                else:
                    self.__storage.remove(asset)
                    print(f"{asset.name} released from {self.__name}")
                    return asset
        else:
            print(f"{asset.name} asset {self.__name} not found.")
            return None



