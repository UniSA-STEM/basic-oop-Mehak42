# """
# File: main.py
# Description: Testing hacker, rig and asset class
# Author: Mehakdeep Kaur Tiwana
# ID: 110397073
# Username: TIWMY001
# This is my own work as defined by the University's Academic Misconduct Policy.
# """

from Asset import Asset
from Hacker import Hacker
from Rig import Rig

# Creating two hackers
attacker = Hacker("Alpha")
defender = Hacker("Beta")

attacker.acquire_rig()
defender.acquire_rig()

print("Initial:")
print(attacker)
print(defender)

# --- Prepare attacker inventory ---
attacker.inventory.append(Asset("Data Spike", "Used in battles."))
attacker.inventory.append(Asset("Data Spike", "Used in battles."))
attacker.inventory.append(Asset("Removable Drive", "Used for extraction."))
attacker.inventory.append(Asset("Security Chip", "Used to encrypt/decrypt assets."))
attacker.inventory.append(Asset("Hardware Patch", "Used to upgrade rigs."))

# Put one encrypted and one unencrypted asset into defender's rig
defender.rig.storage.append(Asset("Data Spike", "Used in battles."))
secret = Asset("Encrypted data - secret", "Very sensitive info.")
secret.encrypted = True
defender.rig.storage.append(secret)

#After populating inventories / rigs:
print("Attacker:", attacker)
print("Defender:", defender)

# Attack prep : filling up Attacker's storage with data spikes which are gonna be used for attacking
attacker.store_asset("Data Spike")
attacker.store_asset("Data Spike")

#Attacker after storing spikes into own rig:
print(attacker)

# --- Attack done: launch Data Spikes until defender's rig is broken ---
while not defender.rig.broken:
    # check if attacker has any Data Spike in their rig
    if not any(a.name == "Data Spike" for a in attacker.rig.storage):
        print("Attacker has no Data Spikes left in rig to launch.")
        break
    attacker.launch_data_spikes(defender.rig)

#After attack
print("Defender rig condition:", defender.rig.rig_condition())
print(defender)

#  Extraction: attacker extracts unsecured assets (requires Removable Drive) ---
print("\n--- Extraction ----")
attacker.extract_assets(defender.rig)

# If encrypted assets remain in defender's rig and attacker has a Security Chip, decrypt them then extract again.
if any(a.name == "Security Chip" for a in attacker.inventory):
    print("\nAttacker has a Security Chip — decrypting encrypted assets in Defender's rig...")
    for asset in list(defender.rig.storage):
        if asset.encrypted:
            asset.encrypted = False
            print(f"Decrypted {asset.name} in Defender's rig.")
else:
    print("\nAttacker does not have a Security Chip, no decryption needed.")

print("\n--- Extraction (after decryption) ---")
attacker.extract_assets(defender.rig)

print("\nResult after extraction:")
print("Attacker:", attacker)
print("Defender:", defender)

# --- Upgrade attacker's rig with Hardware Patch if present ---
print("\n--- Upgrade step ---")
attacker.upgrade_rig()
print("\nFinal attacker state:")
print(attacker)
