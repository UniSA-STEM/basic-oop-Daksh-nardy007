"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: Daksh Narang
ID: 110402115
Username: nardy007
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import random
from Asset import Asset

class Rig:

    def __init__(self, name):
        # Initialize basic rig stats and default assets
        self.__name = name
        self.__damage = 0
        self.__broken = False
        self.__upgrade_level = 0
        self.__storage = [
            Asset("Data Spike", "Used in battles."),
            Asset("Data Spike", "Used in battles."),
            Asset("Removable Drive", "Found in rigs and used for extraction."),
        ]

    def name(self):
        # Return rig name
        return self.__name

    def damage(self):
        # Return rig damage value
        return self.__damage

    def broken(self):
        # Return True if rig is broken
        return self.__broken

    def upgrade_level(self):
        # Return upgrade level
        return self.__upgrade_level

    def storage(self):
        # Return stored assets
        return self.__storage

    def take_hit(self):
        # Increase damage, break rig at 2 hits for level 0
        self.__damage +=1
        if self.__damage >=2 and self.__upgrade_level ==0:
            self.__broken = True

    def repair(self):
        # Reset rig to pristine if damaged
        if self.__damage == 0 and not self.__broken:
            print("No repair is needed.")
            return
        self.__damage =0
        self.__broken = False
        print("Repaired successfully.")

    def upgrade(self, patch_asset):
        # Upgrade level by 1 using a Hardware Patch
        if patch_asset.name() == "Hardware Patch":
            self.__upgrade_level += 1
            print("Upgrade the level by 1")

    def store(self,asset):
        # Add unencrypted asset to storage
        if asset.encrypted():
            print("Decrypt asset to store it.")
            return
        self.__storage.append(asset)
        print("Asset stored successfully.")

    def release(self,name):
        # Remove and release an asset from storage
        for asst in self.__storage:

            if asst.name()==name:
                if not asst.encrypted():
                    self.__storage.remove(asst)
                    print("Asset released successfully.")
                    return True
                else:
                    print("Decrypt asset to release it.")
                    return False
        print("Asset not found in storage.")
        return False

    def generate_asset(self):
        # Generate one random asset from available types
        Asset_List = [
            ("CryptoToken", "Used to acquire or repair rigs."),
            ("Data Spike", "Used in battles."),
            ("Removable Drive", "Found in rigs and used for extraction."),
            ("Security Chip", "Used to encrypt or decrypt assets."),
            ("Hardware Patch", "Used to upgrade rigs."),
        ]
        name, description = random.choice(Asset_List)
        return Asset(name, description)

    def condition(self):
        # Return condition
        if self.__broken:
            return f"Broken (Level{self.__upgrade_level})"

        if self.__damage == 0:
            return f"Pristine (Level {self.__upgrade_level})"

        return f"Damages ({self.__damage}) (Level {self.__upgrade_level})"

    def __str__(self):
        # Print full rig status and stored assets
        if not self.__storage:
            str_Item = "Empty Rig"
        else:
            str_Item =""
            x=0
            for asst in self.__storage:
                str_Item += asst.__str__()
                if x < len(self.__storage)-1:
                    str_Item += ", "
                x+=1
        return f"Rig Name:{self.__name} | {self.condition()} | Assets stored: {str_Item}"


