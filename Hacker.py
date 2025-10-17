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
            if asset.name == "DataSpike" and not asset.encrypted:
                self.__rig.storage.remove(asset)
                target_rig.take_hits()
                self.__trace_level += 1
                print(f"{self.__name} launched a Data Spike. Trace level: {self.__trace_level}")
                if self.__trace_level >= 5:
                    self.__exposed = True
                    print(f"{self.__name} exposed due to high trace level")
                return

        print(f"No data spike found for {self.__name}")


