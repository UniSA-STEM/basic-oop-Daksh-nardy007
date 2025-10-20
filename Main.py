"""
File: main.py
Description: <A brief description of this Python module.>
Author: Daksh Narang
ID: 110402115
Username: nardy007
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Asset import Asset
from Hacker import Hacker

def main():
    print("=== Into the Simulation ===\n")

    # Setup with two hackers with assets
    daksh = Hacker("Daksh")
    narang = Hacker("Narang")

    daksh.get_inventory().append(Asset("Hardware Patch", "Used to upgrade rigs."))
    daksh.get_inventory().append(Asset("Security Chip", "Used to encrypt or decrypt assets."))
    daksh.get_inventory().append(Asset("Removable Drive", "Found in rigs and used for extraction."))
    narang.get_inventory().append(Asset("Security Chip", "Used to encrypt or decrypt assets."))
    narang.get_inventory().append(Asset("Hardware Patch", "Used to upgrade rigs."))

    print(f"{daksh.get_name()} and {narang.get_name()} enter the network.")
    print(f"{daksh.get_name()} has {len(daksh.get_inventory())} assets.")
    print(f"{narang.get_name()} has {len(narang.get_inventory())} assets.\n")

    # Spend CryptoToken to activate a rig for each hacker
    print("Acquiring rigs...")
    daksh.acquire_rig("CyberBlade")
    narang.acquire_rig("SteelFort")

    print(f"{daksh.get_name()}'s rig: {daksh.get_rig().condition()}")
    print(f"{narang.get_name()}'s rig: {narang.get_rig().condition()}\n")

    # Use a Hardware Patch to increase Daksh's rig level
    print("Upgrading Daksh's rig...")
    daksh.upgrade_rig()
    print(f"{daksh.get_name()}'s rig: {daksh.get_rig().condition()}\n")

    # Narang stores and encrypts a CryptoToken in rig storage
    print("Narang stores and encrypts a CryptoToken...")
    narang.get_inventory().append(Asset("CryptoToken", "Used to acquire or repair rigs."))
    narang.store_to_rig("CryptoToken")
    narang.encrypt_asset("rig", "CryptoToken")
    print(narang.get_rig(), "\n")

    # Daksh launches Data Spikes at Narang’s rig until it breaks and trace level increases; Data Spikes are consumed and replenished
    print("Daksh attacks Narang’s rig...")
    while not narang.get_rig().broken():
        daksh.launch_data_spike(narang)
        # Replenish a Data Spike so demo can continue to a break
        if not any(a.name() == "Data Spike" for a in daksh.get_rig().storage()):
            daksh.get_rig().storage().append(Asset("Data Spike", "Used in battles."))
    print(f"{narang.get_name()}'s rig is now {narang.get_rig().condition()}\n")

    # Daksh uses Removable Drive to steal first unencrypted asset
    print("Daksh tries to extract data from the broken rig...")
    daksh._extract_from_broken(narang)
    print(f"{daksh.get_name()}'s inventory:")
    for a in daksh.get_inventory():
        print(" -", a)
    print()

    # Narang repairs with a CryptoToken
    print("Narang repairs his rig...")
    narang.get_inventory().append(Asset("CryptoToken", "Used to acquire or repair rigs."))
    narang.repair_rig()
    print(narang.get_rig(), "\n")

    # Daksh generates and stores a random asset
    print("Daksh generates a new random asset...")
    new_item = daksh.get_rig().generate_asset()
    print("New asset created:", new_item)
    daksh.get_rig().store(new_item)
    print()

if __name__ == "__main__":
    main()
