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
        self.__exposed = False

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

    name = property(get_name, set_name)
    inventory = property(get_inventory, None)
    rig = property(get_rig, None)
    trace_level = property(get_trace_level, set_trace_level)

    def acquire_rig(self):
        for asset in self.__inventory:
            if asset.name == "CryptoToken":
                self.__inventory.remove(asset)
                self.__rig = Rig("BeginnerRig")
                print(f"{self.__name} acquired the BeginnerRig")
                return
        print("The Rig was not acquired: No CryptoToken available")

    def launch_data_spikes(self, target_rig):
        if self.__rig is None:
            print("No rig is available to attack from")
            return

        for asset in self.__rig.storage:
            if asset.name == "Data Spike" and not asset.encrypted:
                self.__rig.storage.remove(asset)
                target_rig.take_hits()
                self.__trace_level += 1
                print(f"{self.__name} launched a Data Spike. Trace level: {self.__trace_level}")
                if self.__trace_level >= 5:
                    self.__exposed = True
                    print(f"{self.__name} exposed due to high trace level")
                return

        print(f"No data spike found for {self.__name}")


    def extract_assets(self, target_rig):
        if not target_rig.broken:
            print("Target rig is not broken yet. No assets will be extracted.")
            return
        removable_drive_available = False
        for asset in list(self.__inventory):
            if asset.name == "Removable Drive":
                self.__inventory.remove(asset)
                removable_drive_available = True
                print("Removable drive is available and used for extraction")
                break

        if not removable_drive_available:
            print("No removable drive found in the inventory")
            return

        for a in list(target_rig.storage):
            if not a.encrypted:
                self.__inventory.append(a)
                target_rig.storage.remove(a)
        print(f"{self.__name} extracted unsecured assets from {target_rig.name}'s inventory")

    def encrypt_asset(self, asset_name):
        security_chip_available = False
        for a in self.__inventory:
            if a.name == "Security Chip":
                security_chip_available = True
                break
        if not security_chip_available:
            print("No security chip found in the inventory")
            return

        for objects in self.__inventory:
            if objects.name == asset_name:
                objects.encrypted = True
                print(f"{asset_name} encrypted")
                return

        if self.__rig is not None:
            for items in self.__rig.storage:
                if items.name == asset_name:
                    items.encrypted = True
                    print(f"{asset_name} encrypted in Rig's storage")
                    return

        print(f"{asset_name} not found in inventory")

    def decrypt_asset(self, asset_name):
        security_chip_available = False
        for a in self.__inventory:
            if a.name == "Security Chip":
                security_chip_available = True
                break
        if not security_chip_available:
            print("No security chip found in the inventory")
            return

        for objects in self.__inventory:
            if objects.name == asset_name:
                objects.encrypted = False
                print(f"{asset_name} has been decrypted")
                return

        if self.__rig is not None:
            for items in self.__rig.storage:
                if items.name == asset_name:
                    items.encrypted = False
                    print(f"{asset_name} decrypted in Rig's storage")
                    return
        print(f"{asset_name} not found in inventory")

    def upgrade_rig(self):
        if self.__rig is None:
            print("No rig is available to upgrade")
            return

        for asset in self.__inventory:
            if asset.name == "Hardware Patch":
                self.__inventory.remove(asset)
                self.__rig.upgrade()
                print(f"{asset.name} upgraded")
                return

        print("No Hardware Patch found in the inventory")

    def store_asset(self, asset_name):
        if self.__rig is None:
            print("No rig is available to store")
            return

        for a in self.__inventory:
            if a.name == asset_name:
                if not a.encrypted:
                    self.__inventory.remove(a)
                    self.__rig.storage.append(a)
                    print(f"{asset_name} stored in Rig's storage")
                else:
                    print(f"{asset_name} is encrypted. Cannot store.")
                return
        print(f"{asset_name} not found in rig's storage")

    def retrieve_asset(self, asset_name):
        if self.__rig is None:
            print("No rig is available to store")
            return

        for a in self.__rig.storage:
            if a.name == asset_name:
                if not a.encrypted:
                    self.__rig.storage.remove(a)
                    self.__inventory.append(a)
                    print(f"{asset_name} retrieved from Rig's storage")
                    return
                else:
                    print(f"{asset_name} is encrypted. Cannot retrieve.")
                    return
        print(f"{asset_name} not found in rig's storage")

    def scan_inventory(self, asset_name):
        for a in self.__inventory:
            if a.name == asset_name:
                self.__inventory.remove(a)
                print(f"{asset_name} removed from inventory")
                return
        print(f"{asset_name} not found in inventory")


    def __str__(self):
        rig_name = self.__rig.name if self.__rig else "No Rig"
        total_items = ",".join(str(a) for a in self.__inventory)
        return f"Hacker: {self.__name} | Rig: {rig_name} | Trace: {self.__trace_level} | Inventory: {total_items}"


