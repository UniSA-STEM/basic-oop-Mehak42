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
    def set_name(self, name):
        self.__name = name
    def set_damage(self, damage):
        self.__damage = max(0, int(damage))
    def set_broken(self, broken):
        self.__broken = bool(broken)
    def set_storage(self, storage):
        self.__storage = storage
    def set_upgrade_level(self, upgrade_level):
        self.__upgrade_level = upgrade_level

    name = property(get_name, set_name)
    damage = property(get_damage, set_damage)
    broken = property(get_broken, set_broken)
    upgrade_level = property(get_upgrade_level, set_upgrade_level)
    storage = property(get_storage, set_storage)

    def repair(self):
        if self.__broken:
            self.__damage = 0
            self.__broken = False
            print(f"{self.__name} has been repaired")
        else:
            print(f"{self.__name} does not need repair")

    def upgrade(self):
        self.__upgrade_level += 1

    def take_hits(self):
        """increases damage by 1. if damage reaches 2, rig becomes broken"""
        self.__damage += 1
        if self.__damage >= 2:
            self.__broken = True

    def generate_assets(self):
        """Generates new assets and adds it to the storage"""
        new_asset = None
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

        self.__storage.append(new_asset)

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

        print(f"{asset_name} asset {self.__name} not found.")
        return None

    def rig_condition(self):
        """returns rig's condition based on damage and upgrade level"""
        if self.__broken:
            return f"Broken (Level {self.__upgrade_level})"
        return f"Pristine (Level {self.__upgrade_level})"

    def __str__(self):
        """prints rig's name, condition, upgrade level and stored assets"""
        total_assets = ", ".join(str(asset) for asset in self.__storage)
        return f"{self.__name} - {self.rig_condition()} | Stored Assets: {total_assets}"



