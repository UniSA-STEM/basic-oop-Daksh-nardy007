"""
File: Hacker.py
Description: Defines Hacker class that manages rigs, assets, encryption, and attacks.
Author: Daksh Narang
ID: 110402115
Username: nardy007
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Asset import Asset
from Rig import Rig

Trace_threshold = 5
class Hacker:

    def __init__(self, name):
        # Initialize hacker with name, zero trace, starter CryptoToken
        self.__name = name
        self.__trace_level = 0
        self.__inventory = [Asset("CryptoToken", "Used to acquire or repair rigs."), ]
        self.__rig = None

    def get_name(self):
        # Return hacker name
        return self.__name

    def get_trace_level(self):
        # Return current trace level
        return self.__trace_level

    def get_inventory(self):
        # Return list of assets in inventory
        return self.__inventory

    def get_rig(self):
        # Return hacker's current rig
        return self.__rig

    def set_trace_level(self, value):
        # Set trace level manually
        self.__trace_level = value

    def set_rig(self, rig):
        # Assign a rig manually
        self.__rig = rig

    def _take_from_inventory(self, name):
        # Remove and return asset by name
        index = 0
        for a in self.__inventory:
            if a.name() == name:
                return self.__inventory.pop(index)
            index += 1
        return None

    def _peek_inventory(self, name):
        # Check if asset exists in inventory
        for a in self.__inventory:
            if a.name() == name:
                return a
        return None

    def _blocked(self):
        # Block actions if trace too high
        return self.__trace_level > Trace_threshold

    def acquire_rig(self, rig_name):
        # Spend CryptoToken to acquire new rig
        if self.__rig:
            return False
        token = self._take_from_inventory("CryptoToken")
        if not token:
            return False
        self.__rig = Rig(rig_name)
        print(f"Rig Activated {rig_name}")
        return True

    def upgrade_rig(self):
        # Use Hardware Patch to upgrade rig level
        if not self.__rig:
            return False
        if self._blocked():
            print("Trace too high")
            return False
        patch = self._take_from_inventory("Hardware Patch")
        if not patch:
            print("No Hardware Patch available")
            return False
        return self.__rig.upgrade(patch)

    def repair_rig(self):
        # Repair rig using CryptoToken
        if not self.__rig:
            return False
        token = self._take_from_inventory("CryptoToken")
        if not token:
            print("No token to repairs.")
            return False
        return self.__rig.repair()

    def retrieve_from_rig(self, name):
        # Retrieve asset from rig to inventory
        if not self.__rig:
            return False
        item_asset = self.__rig.release(name)
        if not item_asset:
            return False
        self.__inventory.append(item_asset)
        return True

    def store_to_rig(self,name):
        # Move asset from inventory to rig
        if not self.__rig:
            return False
        item = self._take_from_inventory(name)
        if not item:
            return False
        self.__rig.store(item)
        return True

    def encrypt_asset(self, where, name):
        # Encrypt or decrypt asset
        target = None
        if not self.__rig:
            return False
        if where == "inventory":
            for asset in self.__inventory:
                if asset.name() == name:
                    target = asset
                    break
        elif where == "rig":
            for asset in self.__rig.storage():
                if asset.name() == name:
                    target = asset
                    break
        else:
            return False

        is_encrypted = target.encrypted()
        if is_encrypted:
            target.decrypt()
            print("Asset decrypted successfully")
        else:
            target.encrypt()
            print("Asset encrypted successfully")
        return True

    def launch_data_spike(self, target: "Hacker"):
        # Attack target's rig and raise trace level
        spike = self.__rig.release("Data Spike")
        self.__trace_level += 1

        if target.get_rig():
            target.get_rig().take_hit()
            print(f"{target.get_name()}'s rig get hit.")

        if target.get_rig().broken():
            self._extract_from_broken(target)
        return True

    def _extract_from_broken(self, target:"Hacker"):
        # Extract unencrypted asset from broken rig
        drive = self.__rig.release("Removable Drive")
        if not drive:
            print("No removable Drive.")
            return False
        index = 0
        for a in target.get_rig().storage():
            if not a.encrypted():
                stolen_asset = target.get_rig().storage().pop(index)
                self.__inventory.append(stolen_asset)
                print("Extraction succeed")
                return True
            index +=1
        return False

    def __str__(self):
        # Display hacker name, rig, trace level, and inventory
        if not self.__inventory:
            invent = "Empty"
        else:
            invent = ""
            for a in self.__inventory:
                invent += a.__str__() + ", "
            invent = invent[:-2]

        if self.__rig:
            rig = self.__rig.name
        else:
            rig = "None"
        return f"Hacker<{self.__name}> rig={rig} trace={self.__trace_level} | Inventory: {invent}"