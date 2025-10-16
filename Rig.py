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


def generate_asset():
    asset_list = [
        ("CryptoToken", "Used to acquire or repair rigs."),
        ("Data Spike", "Used in battles."),
        ("Removable Drive", "Found in rigs and used for extraction."),
        ("Security Chip", "Used to encrypt or decrypt assets."),
        ("Hardware Patch", "Used to upgrade rigs."),
    ]
    name, description = random.choice(asset_list)
    return Asset(name, description)


class Rig:

    def __init__(self, name):
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
        return self.__name

    def damage(self):
        return self.__damage

    def broken(self):
        return self.__broken

    def upgrade_level(self):
        return self.__upgrade_level

    def storage(self):
        return self.__storage

    def take_hit(self):
        self.__damage +=1
        if self.__damage >=2 and self.__upgrade_level ==0:
            self.__broken = True

    def repair(self):
        if self.__damage == 0 and not self.__broken:
            print("No repair is needed.")
            return
        self.__damage =0
        self.__broken = False
        print("Repaired successfully.")

    def upgrade(self, patch_asset):
        if patch_asset.name() == "Hardware Patch":
            self.__upgrade_level += 1
            print("Upgrade the level by 1")

    def store(self,asset):
        if asset.encrypted():
            print("Decrypt asset to store it.")
            return
        self.__storage.append(asset)
        print("Asset stored successfully.")

    def release(self,name):
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

    def condition(self):
        if self.__broken:
            return f"Broken (Level{self.__upgrade_level})"

        if self.__damage == 0:
            return f"Pristine (Level {self.__upgrade_level})"

        return f"Damages ({self.__damage}) (Level {self.__upgrade_level})"


