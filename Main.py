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


main()